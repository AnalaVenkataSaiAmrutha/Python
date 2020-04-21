#Program for getting reverse of a string

#method1
n=input()
print(n[::-1])


#method2
def reverse(s):
    s1=[]
    for i in range(len(s)-1,-1,-1):
        s1.append(s[i])
    s="".join(s1)
    return s
s=input()
rev=reverse(s)
print(rev)
