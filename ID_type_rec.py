#!/usr/bin/python -tt

#HOW TO RUN on bash
#python ID_type_rec.py inputfile

import re
import sys


# Reads line by line,humble does not lock memory.
def file_work(filename):
  f = open(filename, 'rU')
  for line in f:
    columns = line.strip().split("|") #if delimiter is "|"
    id_column = (columns[4]) #when value is in 5th column
    CSP_9 = re.search(r'^[A-Za-z@0-9#\*]{8}[0-9]$', id_column) #CUSIP with check digit
    RIC = re.search(r'\.', id_column) #RIC
    ISIN = re.search(r'^[A-Za-z]{2}\w{9}[0-9]$', id_column) #ISIN
    TCR = re.search(r'^[A-Za-z]{1,5}$', id_column) #TICKER
    QCK = re.search(r'^[0-9]{4}$', id_column) #QUICK CODE - JAPAN ID TYPE
    SDL = re.search(r'^[0-9BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]{6}[0-9]$', id_column) #SEDOL with check digit
    SDL_6 = re.search(r'^[0-9BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]{6}$', id_column) #SEDOL without check digit
    QCK_5 = re.search(r'^[0-9]{5}$', id_column) #QUICK CODE - JAPAN ID TYPE
    TCR_C = re.search(r'^[A-Za-z]{1,5}[0-9]{1,2}$', id_column) #TICKER wariation
    CSP_8 = re.search(r'^[A-Za-z@0-9#\*]{8}$', id_column) #CUSIP without check digit
    if CSP_9:
      out = "CSP_9" + "|" + str(line) #adding id to the rest of row
      outf = open(filename + "_" + "CSP_9", 'a') #creating file with id name as file name. Each matching row will be added to this file 'a'.
      outf.write(out)
    elif RIC:
      out = "RIC" + "|" + str(line)
      outf = open(filename + "_" + "RIC", 'a')
      outf.write(out)
    elif ISIN:
      out = "ISIN" + "|" + str(line)
      outf = open(filename + "_" + "ISIN", 'a')
      outf.write(out)
    elif TCR:
      out = "TCR" + "|" + str(line)
      outf = open(filename + "_" + "TCR", 'a')
      outf.write(out)
    elif QCK:
      out = "QCK" + "|" + str(line)
      outf = open(filename + "_" + "QCK", 'a')
      outf.write(out)
    elif SDL:
      out = "SDL" + "|" + str(line)
      outf = open(filename + "_" + "SDL", 'a')
      outf.write(out)
    elif SDL_6:
      out = "SDL_6" + "|" + str(line)
      outf = open(filename + "_" + "SDL_6", 'a')
      outf.write(out)
    elif QCK_5:
      out = "QCK_5" + "|" + str(line)
      outf = open(filename + "_" + "QCK_5", 'a')
      outf.write(out)
    elif TCR_C:
      out = "TCR_C" + "|" + str(line)
      outf = open(filename + "_" + "TCR_C", 'a')
      outf.write(out)
    elif CSP_8:
      out = "CSP_8" + "|" + str(line)
      outf = open(filename + "_" + "CSP_8", 'a')
      outf.write(out)
    else:
      out = "REM" + "|" + str(line)
      outf = open(filename + "_" + "REM", 'a')
      outf.write(out)
  f.close()
  outf.close()

def main():
  file_work(sys.argv[1])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()