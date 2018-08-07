import os.path
import sys
import hashlib
import os
import time

def calculate_hash(filename):
    blocksize = 65536
    hashfunc = hashlib.sha1()
    with open(filename, 'rb') as f1:
        buf = f1.read(blocksize)
        while len(buf) > 0:
            hashfunc.update(buf)
            buf = f1.read(blocksize)
    hash1 = hashfunc.hexdigest()
    return hash1

#The function search_files finds files by name file_name with hash, hash_file_name
# in directory and sub-directories of path_to_search
def search_files(file_name,hash_file_name,path_to_search):
    res = []
    for entry in os.scandir(path_to_search):
        if ( not entry.name.startswith('.') ) and entry.is_file() and file_name == entry.name:
            h2 = calculate_hash(os.path.join(path_to_search,file_name))
            if hash_file_name == h2:
                res_add = os.path.join(path_to_search,file_name)
                try:
                    found = res.index(res_add)
                except ValueError:
                    found = -1 # not present in res
                if found == -1:
                    res.append(res_add)
        else:
            if ( not entry.name.startswith('.') ) and entry.is_dir():
                ret_list = search_files(file_name,hash_file_name,os.path.join(path_to_search,entry.name))
                if len(ret_list) > 0:
                    for l in range(0, len(ret_list)):
                        try:
                            found = res.index(ret_list[l])
                        except ValueError:
                            found = -1  # not present in res
                        if found == -1:
                            res.append(ret_list[l])
    return res

def main(argv):
    if len(argv) <= 1:
        print("Usage : ", argv[0], "directories")
        exit(0)
    print("This version of the diskclean program generates a report of duplicate files at the following directories - ")
    for i in range(1, len(argv)):
        print((argv[i]))
    print("Final Results in Report.txt")
    #checking if passed parameters are valid
    for i in range(1,len(argv)):
        if not os.path.isdir(argv[i]):
            print("Directory", argv[i], "does not exist!")
    fo = open("Report.txt", "w")
    #fo.write(" ---------------------------------------------------------------\n")
    #fo.write("| Duplicate File Report generated on ")
    #fo.write(time.asctime(time.localtime(time.time())))
    #fo.write("    |\n ---------------------------------------------------------------")
    #fo.write("\n\nDirectories searched for duplicates - \n")
    for i in range(1, len(argv)):
        fo.write("\t")
        fo.write('{}'.format(i))
        fo.write(".  ")
        fo.write(argv[i])
        fo.write("\n")
    num_dirs = len(argv)-1
    #Now, start handling the inputs
    dup_file_hashes = []#will hold hash of files which have been found to have duplicates

    for i in range(1,num_dirs+1):
       for dirpath, dirnames, files in os.walk(argv[i]):
            for search_filename in files:
                res = []
                file_abs_path = os.path.join(dirpath,search_filename)
                hash_file = calculate_hash(file_abs_path)
                try:
                    found = dup_file_hashes.index(hash_file)
                except ValueError:
                    found = -1  # not searched earlier
                if found != -1:
                    continue  # Do not handle this file since it has been found to have duplicates earlier!
                for j in range(1, num_dirs + 1):
                    ret_list = search_files(search_filename, hash_file, argv[j])
                    if len(ret_list) > 0:
                        for l in range(0, len(ret_list)):
                            try:
                                found = res.index(ret_list[l])
                            except ValueError:
                                found = -1  # not present in res
                            if found == -1:
                                res.append(ret_list[l])
                if len(res) > 0:
                    try:
                        found = res.index(file_abs_path)
                    except ValueError:
                        found = -1  # not present in res
                    if found == -1:
                        res.append(file_abs_path)
                    if len(res) > 1 :
                        fo.write("\n\n")
                        fo.write(search_filename)
                        dup_file_hashes.append(hash_file)
                        for l in range(0, len(res)):
                            fo.write("\n|\n|_____")
                            fo.write(res[l].rsplit('/', 1)[0])
                    res=[]
    fo.write("\n")
    fo.close()

if __name__ == "__main__":
    main(sys.argv)
