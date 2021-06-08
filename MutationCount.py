def Hamming(String1, String2):
	i = 0
	mut = 0 
	for i in range(1, len(String1)):
		if String1[i] != String2[i]:
			mut += 1
		i += 1
	return mut	

String1 = str(input('Insert the first nucleotide sequence:'))
String2 = str(input('Insert the second nucleotide sequence:'))

if len(String1) != len(String2):
	print('Sequences lenght must be the same...')
	exit()
else:
	print('The sequences are OK...')	 

result = Hamming(String1, String2)
print(f'These sequences have {result} mutation')			


