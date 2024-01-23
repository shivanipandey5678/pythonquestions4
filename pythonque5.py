//1
tc=int(input())
for i in range(tc):
    N=int(input())
    mat=[]
    for i in range(N):
        arr=list(map(int,input().split()))
        mat.append(arr)
    for i in range(N-1):
        print(mat[0][i],end=" ")
    for i in range(N):
        for j in range(N):
            if i+j==N-1:
                print(mat[i][j],end=" ")
    for i in range(1,N):
        print(mat[N-1][i],end=" ")
    print()

//2
n=3
mat=[]
for i in range(n):
    arr=list(map(str,input().split()))
    mat.append(arr)
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[0][0]=="o" and mat[0][1]=="o" and mat[0][2]=="o":
            print("o")
            break
        elif mat[1][0]=="o" and mat[1][1]=="o" and mat[1][2]=="o":
            print("o")
            break
        elif mat[2][0]=="o" and mat[2][1]=="o" and mat[2][2]=="o":
            print("o")
            break
        elif mat[0][0]=="x" and mat[0][1]=="x" and mat[0][2]=="x":
            print("x")
            break
        elif mat[1][0]=="x" and mat[1][1]=="x" and mat[1][2]=="x":
            print("x")
            break
        elif mat[2][0]=="x" and mat[2][1]=="x" and mat[2][2]=="x":
            print("x")
            break
        #col
        elif mat[0][0]=="o" and mat[1][0]=="o" and mat[2][0]=="o":
            print("o")
            break
        elif mat[0][1]=="o" and mat[1][1]=="o" and mat[2][1]=="o":
            print("o")
            break
        elif mat[0][2]=="o" and mat[1][2]=="o" and mat[2][2]=="o":
            print("o")
            break
        elif mat[0][0]=="x" and mat[1][0]=="x" and mat[2][0]=="x":
            print("x")
            break
        elif mat[0][1]=="x" and mat[1][1]=="x" and mat[2][1]=="x":
            print("x")
            break
        elif mat[0][2]=="x" and mat[1][2]=="x" and mat[2][2]=="x":
            print("x")
            break
        elif mat[0][0]=="o" and mat[1][1]=="o" and mat[2][2]=="o":
            print("o")
            break
        elif mat[0][0]=="x" and mat[1][1]=="x" and mat[2][2]=="x":
            print("x")
            break
        if i+j==n-1:
            if mat[i][j]=="o":
                print("o")
                break
            elif mat[i][j]=="x":
                print("x")
                break
            
        
    break
//3
tc=int(input())
for _ in range(tc):
    mat=[]
    N=int(input())
    for i in range(N):
        arr=list(map(int,input().split()))
        mat.append(arr)
    for i in range(N):
        for j in range(N):
            print(mat[i][j]+1,end=" ")
        print()
//4
tc=int(input())

for i in range(tc):
    mat=[]
    N,M=map(int,input().split())
    for i in range(N):
        arr=list(map(int,input().split()))
        mat.append(arr)
    for i in range(N):
        for j in range(M):
            print(mat[i][j]+1,end=" ")
        print()