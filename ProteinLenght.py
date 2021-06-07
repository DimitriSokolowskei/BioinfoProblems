# Change the sequences as you wish
defen_seq = ['KTCENLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC','ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF','ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN','ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN',
'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN','ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR', 'ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF', 'ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF']

# Finding the shortest peptide/protein sequence
comp = []
for i in defen_seq:
    comp.append(len(i))

count = 0
for n in comp:
    if n == min(comp):
        count += 1
        index = comp.index(n)
defen_short = defen_seq[index:index + count]
print(defen_short)

for m in range(count):
    print(len(defen_short[m]))

# Finding the Longest peptide/protein sequence
comp = []
for i in defen_seq:
    comp.append(len(i))

count = 0
for n in comp:
    if n == max(comp):
        count += 1
        index = comp.index(n)
defen_short = defen_seq[index:index + count]
print(defen_short)

for m in range(count):
    print(len(defen_short[m]))
 
# Finding the mean lenght of peptide/protein sequences
comp = []
for i in defen_seq:
    comp.append(len(i))
print(comp)

count = 0
sum = 0
for n in comp:
    count += 1
    sum += n

media = sum  / count
print(media)

# Finding the median of peptide/protein sequences
from statistics import median

comp = []
for i in defen_seq:
    comp.append(len(i))

x = median(comp)
print(x) 
