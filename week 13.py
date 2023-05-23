#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibonacci(n, second_last, last):

if n-1 == 0:

return second_last

else:

new_last = second_last + last

second_last = last

return fibonacci(n-1, second_last, new_last)

if __name__ == "__main__":

print(fibonacci(10, 0, 1))

def gcd(a, b):
if a == 0 :
return b

return gcd(b%a, a)

a=int(input())
b=int(input())
print("gcd(", a , "," , b, ") = ", gcd(a, b))

def comp(a,b):
if a<b:
return -1
elif a>b:
return -1
else:
return 0

a=input()
b=input()
print("string equality= ", comp(a, b))

