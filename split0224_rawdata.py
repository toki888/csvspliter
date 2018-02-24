# -*- coding: utf8 -*-
import os
import time

###############################################
# 分割ファイル数
numFiles = 60

###############################################
# Source Files and Path
srcPath = "C:\Temp\P17-0052\\"
srcfile1 = 'C:\Temp\P17-0052\\resv_per_pol_TS.csv'
srcfile2 = 'C:\Temp\P17-0052\\resv_per_pol_Oth2.csv'
srcfile3 = 'C:\Temp\P17-0052\\resv_per_pol_Oth1.csv'
srcfile4 = 'C:\Temp\P17-0052\\resv_per_pol_C10.csv'
#outPath = "C:\Temp\P17-0052\out\"

###############################################
# Source Files Prefix
srcPrefix1 = 'resv_per_pol_TS_'
srcPrefix2 = 'resv_per_pol_Oth2'
srcPrefix3 = 'resv_per_pol_Oth1'
srcPrefix4 = 'resv_per_pol_C10'


#srcfile = "C:\MyProjects\P17-0052\work\test\policy_list_1709.csv"
srcfile = "C:\Temp\policy_list_1709.csv"

def mkSubFile(lines,head,srcName,sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename  = des_filename + '_' + str(sub) + extname
    print( 'make file: %s' %filename)
    fout = open(filename,'w')
    try:
#        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()

def getNumOfLines(filename, num):
    num_lines = sum(1 for line in open(filename,'r'))
    num_perfile = round(num_lines/num)+1    #無条件＋１
    #print('total number of lines is ' % num_lines)
    return num_perfile


def splitByLineCount(filename,count):
    fin = open(filename,'r')
    try:
    #    head = fin.readline()
        head = ""
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf,head,filename,sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf,head,filename,sub)   
    finally:
        fin.close()

def getOutFiles(filenames, srcPrefix):
        for item in filenames:
            loc = item.find(srcPrefix)
            if loc == -1:
                filenames.remove(item)
                #filenames.pop()
                print('removed item: ' + item)
            else:
                print(loc)

        return filenames

if __name__ == '__main__':
    begin = time.time()

    #resv_per_pol_TS
    #count=getNumOfLines(srcfile1,numFiles)
    #splitByLineCount(srcfile1,count)

    srcfiles=os.listdir(srcPath)
    #srcfiles=getOutFiles(srcfiles,srcPrefix1)
    #srcfiles=getOutFiles(srcfiles,srcPrefix1)
    #srcfiles = [filter(item.index(srcPrefix1)>=0,item) for item in srcfiles]  
    #a = [v for v in a if not str(v).isdigit()]
    srcfiles = [item for item in srcfiles if not item.find(srcPrefix1)]

#    for item in srcfiles:
#        print(item)




    end = time.time()
    print('time is %d seconds ' % (end - begin))
