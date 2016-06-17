#Given: Two DNA strings ss and tt (each of length at most 1 kbp) in FASTA format.

#Return: One collection of indices of ss in which the symbols of tt appear as a subsequence of ss. If multiple solutions exist, you may return any one.



import sys
records=[]
f=open(sys.argv[1])
records = [line.rstrip('\n') for line in f]
f.close()

master=records[0]
sub=records[1]
start=0
sub_pos=[]
for i in sub:
	sub_i_pos= master.find(i,start)
	sub_pos.append(str(sub_i_pos+1))
	start=sub_i_pos+1
sub_pos=' '.join(sub_pos)


f= open('rosalind30out.txt','w')
print>>f, sub_pos
f.close()