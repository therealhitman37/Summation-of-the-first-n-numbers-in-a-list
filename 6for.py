#Summation of the first n numbers in a list

l = list(map(int, input(" Enter the list: ").split(",")))

n = int(input("Enter n: "))

def sums(l):
    sum = 0
    i = 0
    for x in l:
        if x > 0 and i < n:
            sum += x
            i += 1
    return sum

print(sums(l))