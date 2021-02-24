with open("aspell.txt","r") as f:
    l=f.readlines()
    f.close()

# Function which returns subset or r length from n
from itertools import combinations


def rSubset(arr, r):
    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))



arr = [i/100 for i in range(0,510,10)]
arr = arr+arr+arr+arr+arr
r = 5
constants = rSubset(arr, r)

from searching_alg import search

bconst = []
best = 0

print("Testing Constants")
for const in constants:
    points = 0
    for word in l:
        correct, wrong = word.split()
        answer = search(wrong, *const)
        if answer in correct:
            points+=20
        if len(correct)<3:
            points+=15

    if points>=best:
        print(best, bconst)
        bconst.append(const)

print("Best")
print(bconst)





