#!/usr/bin/env python
import os, sys

def fileList(path):
    files = []
    for item in os.listdir(path):
        item = path+"/"+item
        if (os.path.isdir(item)==True):
            files = files + fileList(item)
        else:
            files.append(item)
    return files;

def matchName (name, dstFiles):
    for item in dstFiles:
        dstName = item.split("/")[-1];
        if name == dstName:
            return item
    return False

def matchChecksum (src, dst):
    return 0

def matchNames(srcFiles, dstFiles):
    notFounds = []
    for item in srcFiles:
        name = item.split("/")[-1];
        if (matchName(name, dstFiles)==False):
            notFounds.append(item)
    return notFounds

def main():
    print("find missing files in the dst directory")
            
    if (len(sys.argv)<3):
        print "usage: missingfiles.py <src_dir> <dst_dir>"
        exit(0)
    
    srcFiles=fileList(sys.argv[1]);
    dstFiles=fileList(sys.argv[2]);

    notFounds=matchNames(srcFiles, dstFiles);

    print notFounds

if __name__ == "__main__":
    main()
