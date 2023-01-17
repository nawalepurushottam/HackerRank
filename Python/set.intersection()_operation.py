N1=int(input())
RN1=set(map(int,input().split()))
N2=int(input())
RN2=set(map(int,input().split()))

print(len(RN1.intersection(RN2)))