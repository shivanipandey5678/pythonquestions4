//1
def solve(n,arr):
    for i in range(n):
        left=True
        right=True
        for j in range(0,i):
            if (arr[i]<arr[j]):
                left=False
        for j in range(i+1,n):
            if (arr[i]>arr[j]):
                right=False
        if (left==True and right==True):
            return arr[i]
    return -1
def inp():
    n=int(input())
    arr=list(map(int,input().split()))
    print(solve(n,arr))
inp()
//2
N=int(input())
for i in range(N):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    res=""
    for i in range(len(arr)):
        if arr[0]==0:
            for j in range(i+1,n):
                if arr[j]!=0:
                    arr[i],arr[j]=arr[j],arr[i]
                    break
   
    
    for i in range(len(arr)):
        res+=str(arr[i])
    print(res)
//3
tc=int(input())

for i in range(tc):
    A,B,C=map(int,input().split())
    ans=(A-B)%C
    print(ans)
//4
def Tom(N,array):
  count_zero=0
  count_one=0
  for i in range(N):
      if(array[i]==0):
          count_zero+=1
      elif(array[i]==1):
          count_one+=1
  if(count_zero<count_one):
      print("Tom")
  elif(count_zero>count_one):
      print("Jerry")
  elif(count_zero==count_one):
      print("Another round")
N=int(input())
array=list(map(int,input().split()))
Tom(N,array)
//5
def distribute_integers_evenly(n, m):
    quotient = n // m  # Integer division
    remainder = n % m

    result = [quotient] * m
    for i in range(remainder):
        result[i] += 1

    return result

# Input format
n, m = map(int, input().split())

# Find the area of m integers satisfying the condition
result = distribute_integers_evenly(n, m)

# Output format
print(*sorted(result))
