#Given: Positive integers n≤100n and m≤20.
#Return: The total number of pairs of rabbits that will remain after the nn-th month if all rabbits live for mm months.

import sys
nMonths= int(sys.argv[1])
lifespan=int(sys.argv[2])


def recurmeth2d(stagearray,count):
	if count<nMonths:
		newborn=sum(stagearray[1:])
		for i in range(lifespan-1,0,-1):
			stagearray[i]=stagearray[i-1]
		stagearray[0]=newborn
		count+=1
		recurmeth2d(stagearray,count)
	else:
		print sum(stagearray)

stages=[0]*lifespan
stages[0]=1
recurmeth2d(stages,1)