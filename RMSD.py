from math import sqrt

def atomN (list1, list2):
	resultN = []
	for i in range(0, 3):
		N = ((list1[0][i] - list2[0][i]) ** 2)
		resultN.append(N)
	return resultN	

def atomCA (list1, list2):
	resultCA = []
	for i in range(0, 3):
		N = ((list1[1][i] - list2[1][i]) ** 2)
		resultCA.append(N)
	return resultCA

def atomC (list1, list2):
	resultC= []
	for i in range(0, 3):
		N = ((list1[2][i] - list2[2][i]) ** 2)
		resultC.append(N)
	return resultC

def atomO (list1, list2):
	resultO = []
	for i in range(0, 3):
		N = ((list1[3][i] - list2[3][i]) ** 2)
		resultO.append(N)
	return resultO
		
# x, y, z coordinates of glycine atoms N, CA, C and O, respectively
list1 = [[108.304, 100.827, 67.992],[108.477, 100.389, 69.362],[109.907, 100.555, 69.817],[110.821, 100.799, 69.027]]
list2 = [[107.670, 101.359, 70.074],[108.477, 100.389, 69.362],[109.513, 101.011, 68.450],[110.667, 100.572, 68.425]]

reN = sum(atomN(list1, list2))
reCA = sum(atomCA(list1, list2))
reC = sum(atomC(list1, list2))
reO = sum(atomO(list1, list2))

x = [reN, reCA, reC, reO]
total = sum(x)
quoc = abs(total) / len(list1)
rmsd = sqrt(quoc)

print(f'The RMSD between the x, y, z coordinates of two glycine residues is: {rmsd}')
