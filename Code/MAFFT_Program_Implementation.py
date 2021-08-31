# MAFFT MSA Program Implementation
# A program implementation that uses the MAFFT MSA Program and times how long it takes
# to align sequences
#
# Justin Thai
# 20 May 2020

import time
from io import StringIO
from Bio import AlignIO
from Bio.Align.Applications import MafftCommandline

# MAFFT Program was retrieved from: https://mafft.cbrc.jp/alignment/software/
# Go to README.txt for more references

# Uncomment line below if using the alternative method
#mafft_exe = "PASTE DIRECTORY OF MAFFT PROGRAM FILE HERE"

# A method to run the MAFFT program and print out the MSA results (default method)
#
# @param directory the directory at which the MAFFT program is found 
# @param fastaFile the FASTA file that contains the sequences to be aligned 
def MAFFT_seq_align(directory, fastaFile):
    mafft_cline = MafftCommandline(directory, input = fastaFile)
    stdout, stderr = mafft_cline()
    align = AlignIO.read(StringIO(stdout), "fasta")
    print(align)

# NOTE: To use MAFFT_seq_align2, some changes to the code needs to be made. Go to
# README.txt for directions on how to set up for use of this alternative method
#
# A method to run the MAFFT program and print out the MSA results (alternative method)
#
# @param fastaFile the FASTA file that contains the sequences to be aligned
def MAFFT_seq_align2(fastaFile):
    mafft_cline = MafftCommandline(mafft_exe, input = fastaFile)
    stdout, stderr = mafft_cline()
    align = AlignIO.read(StringIO(stdout), "fasta")
    print(align)

# User is asked for MAFFT program directory and FASTA file so the alignment results
# and total time can be printed (default method)
# Comment next 6 lines if using the alternative method
userDirectory = input("Please enter directory of the MAFFT program file: ")
userInput = input("Please enter directory of FASTA file with desired sequences: ")
start_time = time.time()   # Timer is started
MAFFT_seq_align(userDirectory, userInput)
total_time = "%s seconds" % (time.time() - start_time)  # Timer ends
print("\n" + "Time taken to align sequences: " + total_time)   # Total time is printed

# User is asked for FASTA file so the alignment results and total time can be printed
# (alternative method)
# Uncomment next 5 lines if using the alternative method
#userInput = input("Please enter directory of FASTA file with desired sequences: ")
#start_time = time.time()    # Timer is started
#MAFFT_seq_align2(userInput)
#total_time = "%s sconds" % (time.time() - start_time)   # Timer ends
#print("\n" + "Time taken to align sequences: " + total_time)    # Total time is printed
