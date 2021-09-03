#1
print("Hello World")


#2
print("강한친구 대한육군")


#3
print("\    /\\")
print(" )  ( \')")
print("(  /  )")
print(" \\(__)|")


#4
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")


#5
from sys import stdin

A, B = map(int, stdin.readline().split())

C = A + B

print(C)


#6
from sys import stdin

A, B = map(int, stdin.readline().split())

C = A - B

print(C)


#7
from sys import stdin

A, B = map(int, stdin.readline().split())

C = A * B

print(C)


#8
from sys import stdin

A, B = map(int, stdin.readline().split())

C = A / B

print(C)


#9
from sys import stdin

A, B = map(int, stdin.readline().split())

C = A + B
D = A - B
E = A * B
F = A // B
G = A % B

print(C)
print(D)
print(E)
print(F)
print(G)


#10
from sys import stdin

A, B, C = map(int, stdin.readline().split())

D = (A+B)%C
E = ((A%C) + (B%C))%C
F = (A*B)%C
G = ((A%C) * (B%C))%C

print(D)
print(E)
print(F)
print(G


#11
from sys import stdin

A = int(stdin.readline())
B = stdin.readline()

C = A * int(B[2])
D = A * int(B[1])
E = A * int(B[0])
F = A * int(B)

print(C)
print(D)
print(E)
print(F)