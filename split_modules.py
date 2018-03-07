# -*- coding: utf8 -*-
import os
import time

#################################################
# This module contains all subroutines and functions called from split0307_rawdata.py

#One File Version
def mkOneSubFile(lines,head,srcName,sub, part1, part2):
    [des_filename, extname] = os.path.splitext(srcName)
    filename  = des_filename + '_' + str("{0:02d}".format(part1+1)) + '_' + str("{0:02d}".format(part2+1)) + extname
    #print( 'make file: %s' %filename)
    fout = open(filename,'w')
    try:
#        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()

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

#split file into 60 sub files having ratio as 1:3:3:3  - OneFile Version
def splitOneFile (filename):
    #Get the number of lines of input file
    num_lines = sum(1 for line in open(filename,'r'))

    print("num_lines is %d" % num_lines)

    #Inputファイル行数の1/600を計算
    num_unit = round(num_lines/150)+1    #1/600, 無条件＋１
    print("num_unit is %d" % num_unit)

    #unitは６０ファイルの各ファイルの件数、最初の１５件と残りの４５件は１：３の比例
    unit = []
    for i in range(0,60) :
        unit.append(num_unit)

        #16個目から３倍する
        if i==14:
            num_unit = num_unit * 3
        else:
            pass

        print(i, unit[i],)

    fin = open(filename,'r')
    try:
    #    head = fin.readline()
        head = ""
        buf = []
        sub = 1
        i=0
        part1=0; part2=0;
        for line in fin:
            buf.append(line)
            if len(buf) == unit[i]:
                part1,part2 = divmod(i,15)
                sub = mkOneSubFile(buf,head,filename,sub, part1, part2)
                buf = []
                i += 1
        if len(buf) != 0:
            part1,part2 = divmod(i,15)
            sub = mkOneSubFile(buf,head,filename,sub, part1, part2)
    finally:
        fin.close()

    return num_lines

#split file into 60 sub files in 4 sets having ratio as 1:3:3:3
def splitSourceFile (filename):
    #Get the number of lines of input file
    num_lines = sum(1 for line in open(filename,'r'))

    print("num_lines is %d" % num_lines)


    #Inputファイル行数の1/600を計算
    num_unit = round(num_lines/150)+1    #1/600, 無条件＋１
    print("num_unit is %d" % num_unit)

    #unitは６０ファイルの各ファイルの件数、最初の１５件と残りの４５件は１：３の比例
    unit = []
    for i in range(0,60) :
        unit.append(num_unit)

        #16個目から３倍する
        if i==14:
            num_unit = num_unit * 3
        else:
            pass

        print(i, unit[i],)

#    summ = 0
#    for i in range(0,60):
#        summ += unit[i]
#
#    print ("sum is %d:" % summ)

    fin = open(filename,'r')
    try:
    #    head = fin.readline()
        head = ""
        buf = []
        sub = 1
        i=0
        for line in fin:
            buf.append(line)
            if len(buf) == unit[i]:
                sub = mkSubFile(buf,head,filename,sub)
                buf = []
                i += 1
        if len(buf) != 0:
            sub = mkSubFile(buf,head,filename,sub)
    finally:
        fin.close()


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

#重複契約を削除する
def getUnifiedFile (filename):
    fin = open(filename, 'r')
    try:
        head = ""
        buf = []
        sub = 1
        for line in fin :
            if line not in buf:
                buf.append(line)
                sub += 1

        print("total records are %d" % sub)
    finally:
        fin.close()
