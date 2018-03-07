# -*- coding: utf8 -*-
import os
import time

import split_modules as myfun

###############################################
numFiles = 1               # 分割ファイル数

###############################################
# Source Files and Path
srcPath = "C:\Temp\P17-0052-1\\"
srcfile = srcPath + 'allinone_origin.csv'
srcfile_uni = srcPath + 'allinone.csv'
srcfile1 = srcPath + 'resv_per_pol_TS.csv'
srcfile2 = srcPath + 'resv_per_pol_Oth2.csv'
srcfile3 = srcPath + 'resv_per_pol_Oth1.csv'
srcfile4 = srcPath + 'resv_per_pol_C10.csv'
outputPath = "C:\Temp\P17-0052-1\out\\"

###############################################
# Source Files Prefix
srcPrefix1 = 'resv_per_pol_TS_'
srcPrefix2 = 'resv_per_pol_Oth2_'
srcPrefix3 = 'resv_per_pol_Oth1_'
srcPrefix4 = 'resv_per_pol_C10_'
# Output files Prefix
outputPrefix = 'inputFile_'
outputSuffix = '.csv'


##############################################################
# Main Program
#
if __name__ == '__main__':
    begin = time.time()

    num_orginlines = sum(1 for line in open(srcfile,'r'))
    print("The total number of origin file with duplicate. %d" % num_orginlines)

    #Remove duplicates from allinone.csv file
    myfun.removedup(srcfile, srcfile_uni)

    count1 = myfun.splitOneFile(srcfile_uni)
    print("Total number is %d" % count1)

    end = time.time()
    print('time is %d seconds ' % (end - begin))
