MULTIPLE SEQUENCE ALIGNMENT (MSA) PROGRAM IMPLEMENTATIONS INSTRUCTIONS AND GUIDE

CS 123A PROJECT
BY: JUSTIN THAI
20 MAY 2020
--------------------------------------------------------------------------------------------
TABLE OF CONTENTS

1. Description of Datasets Used 
2. Set Up for Use of the Alternative Method of the MAFFT Program Implementation 
3. How to Use the MAFFT Program Implementation (default method)
4. How to Use the MAFFT Program Implementation (alternative method)
5. Handling Errors in the MUSCLE Program Implementation
6. How to Use the MUSCLE Program Implementation 
7. References

--------------------------------------------------------------------------------------------
1. Description of Datasets Used

	For this project, 18 mRNA sequences of the hemoglobin subunit beta (HBB) protein 
were taken from the NCBI database (https://www.ncbi.nlm.nih.gov/). With these 18 sequences, 
three different test cases were used to test the MSA program implementations. The cases are:
	a. Test Case #1: 3 different mRNA sequences
	b. Test Case #2: 9 different mRNA sequences
	c. Test Case #3: 18 different mRNA sequences
Each of these test cases is provided as text documents in FASTA format and are located in
the "Datasets" folder. The "Datasets" folder is included in the project folder. The MSA
program implementations also accept other FASTA files of DNA/RNA sequences that the user
wants to input for alignment. 

--------------------------------------------------------------------------------------------
2. Set Up for Use of the Alternative Method of the MAFFT Program Implementation

	The alternative method gives the user a way to not copy the directory of the MAFFT
program file every time the program implementation runs. If the user wants to use the 
alternative method of the MAFFT program implementation, follow these steps to be able to run
and use the method. 
	Steps:
	1) Open MAFFT_Program_Implementation.py.
	2) Uncomment the indicated sections of code. There will be comments in the code that
	   will show which lines of code to uncomment. 
		- Can be found at lines 17 and 54-58 
	3) Comment the indicated sections of code. There will be comments in the code that 
	   will show which lines of code to comment.
		- Can be found at lines 44-49
	4) Copy the directory of the MAFFT program file found in the folder 
	   "mafft-7.467-win64-signed" (should be a .bat file).
	5) Find the line of code that starts with "mafft_exe" (should be line 17).
		- Paste the directory of the MAFFT program file between the quotations
		  (indicated by the words "PASTE DIRECTORY OF MAFFT PROGRAM FILE HERE")
		- Make sure that the directory of the MAFFT program file is in quotations
	6) Save MAFFT_Program_Implementation.py.	

--------------------------------------------------------------------------------------------
3. How to Use the MAFFT Program Implementation (default method)

	Steps:
	1) Open MAFFT_Program_Implementataion.py.
	2) Run the module.
	3) The console will ask for the directory of the MAFFT program file. Copy the
	   directory for the MAFFT program file (should be a .bat file) and paste the 
	   directory to the console. Press ENTER.
		- The MAFFT program file can be found in the folder 
		"mafft-7.467-win64-signed"
	4) The console will ask for the directory of the FASTA file with the desired 
	   sequences. Copy the directory of the FASTA file of the sequences and paste it
	   to the console. Press ENTER.
	5) The program should run and print out the alignment results and time taken to 
	   complete the alignment.

--------------------------------------------------------------------------------------------
4. How to Use the MAFFT Program Implementation (alternative method)

NOTE: Make sure the setup of the alternative method (go to Part 2) has been done before 
using this version of the MAFFT Program Implementation.
	Steps: 
	1) Open MAFFT_Program_Implementation.py.
	2) Run the module.
	3) The console will ask for the directory of the FASTA file with the desired 
	   sequences. Copy the directory of the FASTA file of the sequences and paste it
	   to the console. Press ENTER.
	4) The program should run and print out the alignment results and time taken to 
	   complete the alignment.

--------------------------------------------------------------------------------------------
5. Handling Errors in the MUSCLE Program Implementation
	
	In the case where the error message "'muscle3.8.31_i86win32.exe' is not recognized 
as an internal or external command," appears after the FASTA file is given, follow these 
steps to solve the error.
	Steps: 
	1) Open MUSCLE_Program_Implementation.py.
	2) Copy the directory of the MUSCLE program file (the file should be called 
	   "muscle3.8.31_i86win32.exe").
	3) Go to the line that starts with "muscle_exe" (should be line 17).
		- Replace the MUSCLE program file name currently written with the directory
		of the MUSCLE program file. 
		- Make sure that the directory of the MUSCLE program file is in quotations.
	4) Save MUSCLE_Program_Implementation.py.

--------------------------------------------------------------------------------------------
6. How to Use the MUSCLE Program Implementation

	Steps: 
	1) Open MUSCLE_Program_Implementation.py.
	2) Run the module.
	3) The console will ask for the directory of the FASTA file with the desired 
	   sequences. Copy the directory of the FASTA file of the sequences and paste it
	   to the console. Press ENTER.
	4) The program should run and print out the alignment results and time taken to 
	   complete the alignment.

--------------------------------------------------------------------------------------------
7. References

Chang, J., Chapman, B., Friedberg, I., Hamelryck, T., de Hoon, M., Cock, P., Antao, T., 
	Talevich, E., & Wilczynski, B. (2019). Biopython tutorial and cookbook. 
	http://biopython.org/DIST/docs/tutorial/Tutorial.html
Edgar, R.C. (2004). MUSCLE: A multiple sequence alignment with high accuracy and high
	throughput. Nucleic Acids Research, 32(5), 1792-1797. 
	https://drive5.com/muscle/
Katoh, K. (2013). MAFFT (Version 7.467). Kazutaka Katoh. 
	https://mafft.cbrc.jp/alignment/software/