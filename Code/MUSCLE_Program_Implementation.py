# MUSCLE MSA Program Implementation
# A program implementation that uses the MUSCLE MSA program and times how long it takes
# to align sequences
#
# Justin Thai
# 20 May 2020

import time
from io import StringIO
from Bio import AlignIO
from Bio.Align.Applications import MuscleCommandline

# MUSCLE Program retreived from: https://drive5.com/muscle/
# Go to README.txt for more references

# If there is an error with running the code, refer to README.txt to see how to fix it.
muscle_exe = "muscle3.8.31_i86win32.exe"

# A method to run the MUSCLE program and print out the MSA results
#
# @param fastaFile the FASTA file that contains the sequences to be aligned 
def MUSCLE_seq_align(fastaFile):
    muscle_cline = MuscleCommandline(muscle_exe, input = fastaFile)
    stdout, stderr = muscle_cline()
    align = AlignIO.read(StringIO(stdout), "fasta")
    print(align)

# User is asked for FASTA file so the alignment results and total time can be printed
userInput = input("Please enter location of FASTA file with desired sequences: ")
start_time = time.time()    # Timer is started
MUSCLE_seq_align(userInput)
total_time = "%s seconds" % (time.time() - start_time)  # Timer ends
print("\n" + "Time taken to align sequences: " + total_time) # Total time is printed
