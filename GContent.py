# Change the nt sequence as you wish.
sum = 0
seq = 'ATGCATGCTTTTTGATCGATC'
seq = list(seq)
for i in seq:
    if i == 'C':
        sum += 1
    elif i == 'G':
        sum += 1

calc = ((sum / len(seq)) * 100)
print(f'The GC content is {calc}.')
