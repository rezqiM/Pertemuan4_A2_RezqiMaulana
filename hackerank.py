# LATIHAN 1
A = input()
A = A.split()

if A[0] == "[]" and A[1] == "8<":
    print("Pemain B menang")
elif A[0] == "()" and A[1] == "[]":
    print("Pemain B menang")
elif A[0] == "8<" and A[1] == "()":
    print("Pemain B menang")
elif A[0] == "()" and A[1] == "8<":
    print ("Pemain A menang")
elif A[0] == "[]" and A[1] == "()":
    print("Pemain A menang")
elif A[0] == "8<" and A[1] == "[]":
    print("Pemain A menang")
else :
    print("Draw")

# LATIHAN 2
a = int(input())
b = int(input())
c = int(input())

avr = (a+b+c)//3

if avr >= 50:
    print("LULUS")
else :
    print("GAGAL")

# LATIHAN 3
a = int(input())
b = int(input())
c = int(input())

z = [a,b,c]
z.sort()
print(z[1])

# LATIHAN 4
txt = input()
a = txt.count('a')
i = txt.count('i')
u = txt.count('u')
e = txt.count('e')
o = txt.count('o')
A = txt.count('A')
I = txt.count('I')
U = txt.count('U')
E = txt.count('E')
O = txt.count('O')
print (a+i+u+e+o+A+I+U+E+O)