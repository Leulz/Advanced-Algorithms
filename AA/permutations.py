n = int(raw_input())
 
def perms(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results
 
for i in range(n):
    string = raw_input()
     
    permutations = perms(string)
     
    permutations.sort()
     
    for j in range(len(permutations)):
        print permutations[j]
    print ""
