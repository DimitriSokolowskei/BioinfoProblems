sum = 0
seq = 'XXXXXXXXXXXXXXXXXXXX'
seq = list(seq)
for i in seq:
    if i == 'C':
        sum += 1
    elif i == 'G':
        sum += 1

print('The GC content is {:.2f}.'.format((sum / len(seq)) * 100)
