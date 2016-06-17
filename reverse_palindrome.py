#Given: A DNA string of length at most 1 kbp in FASTA format.

#Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

import sys
from Bio import SeqIO

f=open(sys.argv[1])
seq= str(SeqIO.read(f,'fasta').seq).upper()
f.close()

compdict={"A":"T","T":"A","C":"G","G":"C"}
answerlist=[]
for sz in range(4,14,2):
	for i in range(0,len(seq)):
		sub=seq[i:i+sz]
		half= sub[:sz/2]
		revcomphalf= ''.join(map(compdict.get, half[::-1]))
		if revcomphalf==sub[sz/2:]:
			answerlist.append((str(i+1),str(sz)))
flout= open("rosalind21out.txt","w")

for each in answerlist:
	flout.write(' '.join(each)+'\n')
flout.close()