from math import factorial

def print_permutations_lexicographic_order(s,n):
    seq = list(s)
    arr = []

    for _ in range(factorial(len(seq))):
        arr.append("".join(seq))
        p = len(seq) - 1

        while p > 0 and seq[p - 1] > seq[p]:
            p -= 1
        seq[p:] = reversed(seq[p:])

        if p > 0:
            q = p
            while seq[p - 1] > seq[q]:
                q += 1
            seq[p - 1], seq[q] = seq[q], seq[p - 1]

    print(arr[n-1])

s = '0123456789'
print_permutations_lexicographic_order(s,1000000)

