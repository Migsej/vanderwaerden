from itertools import permutations, combinations, product

def has_arithmetic_progression(group, k):
    group = sorted(group)
    for i in combinations(group, k):
        step = i[1] - i[0]
        for j in range(2, k):
            if i[j] - i[j - 1] != step:
                break
        else:
            return True
    return False
                


def generaterrest(sum, length):
    if length  - 1 == 0:
        return [[sum]]

    result = []
    for start in range(sum + 1):
        rests = generaterrest(sum - start, length - 1)
        for i in rests:
            end = [start]    
            end.extend(i)
            end.sort()
            if end not in result:
                result.append(end)
    return result
   
def iteratecombined(numbers, sizes):
    for size in sizes:
        for number in numbers:
            yield (number, size)



def W(r,k):
    N = k

    while True: 
        numbers = list(permutations([i +1 for i in range(N)]))
        sizes = generaterrest(N, r)
        found = True
        for (number, size) in product(numbers, sizes):
            lastindex = 0
            inddeling = 0
            for v in size:
                group = number[lastindex:lastindex+v]
                if has_arithmetic_progression(group, k):
                    inddeling += 1
                lastindex = v

            if inddeling == 0:
                found = False
                break

        if found:
            return N
        print(N)
        N += 1

if __name__ == "__main__":
    print(W(2,3))
