#Given: A DNA string ss (of length at most 1 kbp) and a collection of substrings of ss acting as introns. All strings are given in FASTA format.

#Return: A protein string resulting from transcribing and translating the exons of ss. (Note: Only one solution will exist for the dataset provided.)
#
import sys
from Bio import SeqIO
codontable= {"UUU":"F","UUC":"F","UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L","AUU":"I","AUC":"I","AUA":"I","AUG":"M", "GUU":"V","GUC":"V","GUA":"V","GUG":"V","UCU":"S","UCC":"S","UCA":"S","UCG":"S","CCU":"P","CCC":"P","CCA":"P","CCG":"P","ACU":"T","ACC":"T","ACA":"T","ACG":"T","GCU":"A","GCC":"A","GCA":"A","GCG":"A","UAU":"Y","UAC":"Y","UAA":"X","UAG":"X","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q","AAU":"N","AAC":"N", "AAA":"K","AAG":"K","GAU":"D","GAC":"D","GAA":"E","GAG":"E","UGU":"C","UGC":"C","UGA":"X","UGG":"W","CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGU":"S","AGC":"S","AGA":"R","AGG":"R","GGU":"G","GGC":"G","GGA":"G","GGG":"G"}
f=open(sys.argv[1])
sequences= list(SeqIO.parse(f,'fasta'))
f.close()
dnaseq=str(sequences[0].seq)
for each in sequences[1:]:
	dnaseq=dnaseq.replace(str(each.seq),'XX')
dnaseq=dnaseq.replace("XX","")
transcript=dnaseq.replace("T","U")
translated=[]
for i in range(0,len(transcript),3):
	codon=transcript[i:i+3]
	translated.append(codontable.get(codon))
flout=open('rosalind22out.txt','w')
flout.write(''.join(translated[:-1]))
flout.close()