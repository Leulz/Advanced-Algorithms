n = int(raw_input())
stones = [int(x) for x in raw_input().split()]
sum_stones = [0 for x in range(n)]
sum_stones[0]=stones[0]

def first_question(l,r):
    if l==1:
        return sum_stones[r-1]
    if l==r:
        return stones[r-1]
    return sum_stones[r-1]-sum_stones[l-2]

def second_question(l,r):
    if l==1:
        return sum_sorted[r-1]
    if l==r:
        return stones_sorted[r-1]
    return sum_sorted[r-1]-sum_sorted[l-2]

for i in range(1,n):
    sum_stones[i] = stones[i]+sum_stones[i-1]

stones_sorted = [x for x in stones]
stones_sorted.sort()
sum_sorted = [0 for x in range(n)]
sum_sorted[0] = stones_sorted[0]

for i in range(1,n):
    sum_sorted[i] = stones_sorted[i]+sum_sorted[i-1]

m = int(raw_input())

for i in range(m):
    entrada = [int(x) for x in raw_input().split()]
    if entrada[0]==1:
        print first_question(entrada[1],entrada[2])
    else:
        print second_question(entrada[1],entrada[2])
