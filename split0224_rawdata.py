# -*- coding: utf8 -*-
import os
import time

###############################################
numFiles = 60               # 分割ファイル数

###############################################
# Source Files and Path
srcPath = "C:\Temp\P17-0052\\"
srcfile1 = 'C:\Temp\P17-0052\\resv_per_pol_TS.csv'
srcfile2 = 'C:\Temp\P17-0052\\resv_per_pol_Oth2.csv'
srcfile3 = 'C:\Temp\P17-0052\\resv_per_pol_Oth1.csv'
srcfile4 = 'C:\Temp\P17-0052\\resv_per_pol_C10.csv'
outputPath = "C:\Temp\P17-0052\out\\"

###############################################
# Source Files Prefix
srcPrefix1 = 'resv_per_pol_TS_'
srcPrefix2 = 'resv_per_pol_Oth2_'
srcPrefix3 = 'resv_per_pol_Oth1_'
srcPrefix4 = 'resv_per_pol_C10_'
# Output files Prefix
outputPrefix = 'inputFile_'
outputSuffix = '.csv'


#srcfile = "C:\MyProjects\P17-0052\work\test\policy_list_1709.csv"
srcfile = "C:\Temp\policy_list_1709.csv"

def mkSubFile(lines,head,srcName,sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename  = des_filename + '_' + str("{0:02d}".format(sub)) + extname
    #print( 'make file: %s' %filename)
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

##############################################################333
if __name__ == '__main__':
    begin = time.time()

    if(0>1):
        #File1:     resv_per_pol_TS
        #
        count=getNumOfLines(srcfile1,numFiles)
        splitByLineCount(srcfile1,count)

        #File2:     resv_per_pol_Oth2
        #
        count=getNumOfLines(srcfile2,numFiles)
        splitByLineCount(srcfile2,count)

        #File3:     resv_per_pol_Oth1
        #
        count=getNumOfLines(srcfile3,numFiles)
        splitByLineCount(srcfile3,count)

        #File4:     resv_per_pol_C10
        #
        count=getNumOfLines(srcfile4,numFiles)
        splitByLineCount(srcfile4,count)

#生成した４種類の中間ファイルを配列に
    srcfiles=os.listdir(srcPath)
    #a = [v for v in a if not str(v).isdigit()]
    srcfiles1 = [item for item in srcfiles if not item.find(srcPrefix1)]
    srcfiles2 = [item for item in srcfiles if not item.find(srcPrefix2)]
    srcfiles3 = [item for item in srcfiles if not item.find(srcPrefix3)]
    srcfiles4 = [item for item in srcfiles if not item.find(srcPrefix4)]

    #Output total 60 files to subfolder - out
    numOutput = 1
    for item1, item2, item3, item4 in zip(srcfiles1, srcfiles2,srcfiles3,srcfiles4):
        item1 = srcPath + item1
        item2 = srcPath + item2
        item3 = srcPath + item3
        item4 = srcPath + item4
        outputfile = outputPath + outputPrefix + str("{0:02d}".format(numOutput)) + outputSuffix
        cmdCopy = 'copy/b ' + item1 + ' + ' + item2 + ' + ' + item3 + ' + ' + item4 + ' ' + outputfile
        os.system(cmdCopy)
        numOutput += 1

    end = time.time()
    print('time is %d seconds ' % (end - begin))
