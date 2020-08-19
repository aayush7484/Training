n=int(input())
lst=[]
for i in range(1,n+1):
    lst.append(i)
print(lst)
a=list(map(lambda x:x**2,lst))
print(a)
print(sum(a))