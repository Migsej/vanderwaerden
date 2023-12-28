from itertools import permutations, combinations

def has_arithmetic_progression(group, k):
    group.sort()
    for i in list(combinations(group, k)):
        step = i[1] - i[0]
        for j in range(2, k):
            if i[j] - i[j - 1] != step:
                break
        else:
            return True
    return False
                


def generaterrest(sum, length):
    result = []
 
    if length  - 1 == 0:
        return [[sum]]

    for start in range(sum + 1):
        rests = generaterrest(sum - start, length - 1)
        for i in rests:
            end = [start]    
            end.extend(i)
            result.append(end)
    uniqueresult = []
    for i in range(len(result)):
        result[i].sort()
        if result[i] not in uniqueresult:
            uniqueresult.append(result[i])

    return uniqueresult
   
def iteratecombined(numbers, sizes):
    for size in sizes:
        for number in numbers:
            yield (number, size)

print(generaterrest(2, 2))

duplicates = {}

def W(r,k):
    N = 1

    while True: 
        numbers = permutations([i +1 for i in range(N)])
        sizes = generaterrest(N, r)
        found = True
        #print(list(numbers), sizes)
        for (number, size) in iteratecombined(list(numbers), sizes):
            inddeling = [[] for _ in size]
            lastindex = 0
            for i, v in enumerate(size):
                inddeling[i] = list(number[lastindex:lastindex+v])
                lastindex = v
            bla = list(filter(lambda x: x, map(lambda group: has_arithmetic_progression(group, k), inddeling)))
            if len(bla) != 0:
                pass
            else:
                found = False
                #break

        if found:
            return N
        print(N)
        N += 1

if __name__ == "__main__":
    print(W(2,3))
