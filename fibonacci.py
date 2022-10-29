seq = [0,1]
fib1 = (len(seq)-1)
fib2 = (len(seq) -2)
print (fib1, fib2)

iterations = int(input("How long fib sequence?"))

for x in range(iterations):
    fib1 = (len(seq) - 1)
    fib2 = (len(seq) - 2)
    nextFib = (seq[fib1] + seq[fib2])
    seq.insert(len(seq),nextFib)

print('Fib Sequence:', seq)

