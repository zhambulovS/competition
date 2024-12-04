import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
# tizim = lambda: list(map(int, input().split()))
#--------------------------------------------------
# san = lambda: int(input())
# maap = lambda: map(int, input().split())
n=int(input())
res=04
for _ in range(n):
    a,b=map(int,input().split())
    res+=a+b
print(res)
        
    

    

