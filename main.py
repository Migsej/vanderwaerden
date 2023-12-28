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
    N = k

    while True: 
        numbers = list(permutations([i +1 for i in range(N)]))
        sizes = generaterrest(N, r)
        found = True
        #print(list(numbers), sizes)
        for (number, size) in iteratecombined(numbers, sizes):
            lastindex = 0
            inddeling = []
            for v in size:
                group = list(number[lastindex:lastindex+v])
                if has_arithmetic_progression(group, k):
                    inddeling.append(group)
                lastindex = v

            if len(inddeling) == 0:
                found = False
                break

        if found:
            return N
        print(N)
        N += 1

if __name__ == "__main__":
    print(W(2,3))
