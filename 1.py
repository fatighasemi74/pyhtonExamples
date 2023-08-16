n = int(input("Enter a number:"))
def multiples(num):
    list_n=[]
    i = 1
    sum = 0
    while i < num:
        if (i % 3 == 0) or (i % 5 == 0) :
            sum = sum + i
            list_n.append(sum)
        i += 1
    return list_n

print(multiples(n))
