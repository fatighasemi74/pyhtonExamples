n = int(input("Enter a number:"))
def multiples(num):
    i = 1
    sum = 0
    while i < num:
        if (i % 3 == 0) or (i % 5 == 0) :
            sum = sum + i
        i += 1
    return sum

print(multiples(n))
