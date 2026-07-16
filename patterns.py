import sys
import os

# This automatically redirects input and output if the files exist
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def print10(n):
    for i in range(1,2*n):
        stars=i
        if i>n:
            stars=2*n-i
        for j in range(1,stars+1):
            print("*",end="")
        print("")
def print11_own(n):
    for i in range(1,n+1):
        if i%2==0:
            for j in range(i):
                if j%2==0:
                    print("0",end="")
                else:
                    print("1",end="")
            print()
        else:
            for j in range(i):
                if j%2==0:
                    print("1",end="")
                else:
                    print("0",end="")
            print()
def print11(n):
    start=1
    for i in range(n):
        if i%2==0: start=1
        else: start=0
        for j in range(i+1):
            print(start,end="")
            start=1-start
        print()
def print12(n):
    space=n*2
    for i in range(1,n+1):
        num=i
        space=space-2
        for j in range(1,num+1):
            print(j,end="")
        for j in range(space):
            print("_",end="")
        for j in range(num,0,-1):
            print(j,end="")
        print()
def print13(n):
    num=0
    for i in range(1,n+1):
        for j in range(i):
            num=num+1
            print(num,end=" ")
        print()
def print14(n):
    for i in range(1,n+1):
        num=65
        for j in range(i):
            print(chr(num),end=" ")
            num+=1
        print()


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print14(n)