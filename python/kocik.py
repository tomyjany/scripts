def is_Factor(f,n):
    return n%f==0

f = int(input("Zadejte delitele f: "))
n = int(input("Zadejte cislo n: "))
print(is_Factor(f,n))

