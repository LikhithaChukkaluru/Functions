# r=lambda a:a+15
# print(r(10))

# r=lambda x,y:x*y
# print(r(10,12))

# s = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# s.sort(key = lambda x: x[1])
# print(s)

# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even=list(filter(lambda x:x%2==0,s))
# # print(even)
# odd=list(filter(lambda x :x%2!=0,s))
# print(odd)

# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s=list(map(lambda x :x**2,s))
# s=list(map(lambda x :x**3,s))
# print(s)

# s = [-1, 2, -3, 5, 7, 8, 9, -10]
# r=sorted(s,key=lambda i:0 if i==0 else -1/i)
# print(r)

# s = [1, 2, 3, 5, 7, 8, 9, 10]
# odd=len(list(filter(lambda x: (x%2 !=0),s)))
# even=len(list(filter(lambda x: (x%2==0),s)))
# print(odd)
# print(even)

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# days = filter(lambda day: day if len(day)==6 else '', weekdays)
# for d in days:
#   print(d)

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# s=(map(lambda x,y :x+y,nums1,nums2))
# print(list(s))

# s = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# r=list(filter(lambda x:(x%19==0 or x%13==0),s))
# print(r)

# s = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
# r=list(filter(lambda x:(x=="".join(reversed(x))),s))
# print(r)

# s = [2, 4, 6, 9 , 11]
# n = 2
# r=list(map(lambda x:x*n,s))
# print(r)

# s = [2, 4, -6, -9, 11, -12, 14, -5, 17]
# esum=list(filter(lambda x:x>0,s))
# print(sum(esum))
# osum=list(filter(lambda x:x<0,s))
# print(sum(osum))


# RECURSION

# def fib(n): 
#         if n==0 :
#             return 0
#         if n==1:
#             return 1
#         else :
#             return (fib(n-1) + fib(n-2))
# n=10
# for i in range (0,n):
#     print(fib(i),end=" ")

# def fact(n):
#     # for i in range (0,n):
#         if n==0 or n==1  :
#             return 1
#         else :
#             return n*fact(n-1)
# n=6
# print(fact(n))

# def palindrome(string):
#     if string=="":
#         return True
#     elif len(string)==1:
#         return True
#     elif len(string)==2:
#         return True
#     elif string[0]==string[-1]:
#         return palindrome(string[1:-1])
#     else :
#         return False
# print(palindrome("nayan"))

# def pa(n):
#     if len(n) < 2: 
#         return True
#     if n[0] != n[-1]: 
#         return False
#     return pa(n[1:-1])
# n="mom"
# print(pa(n))
              
# def pro(a,b):
#     if a<b :
#         return pro(b,a)
#     elif b!=0:
#         return(a+pro(a,b-1))
#     else :
#         return 0
# a=5
# b=6
# print(pro(a,b))

# def sum(n):
#     if n==1 :
#         return n 
#     return n +sum(n-1)
# n=10
# print(sum(n))

# def len(str):
#     if str=="":
#         return 0
#     else :
#         return 1+len(str[1:])
# str="likhitha"
# print(len(str))

# def sum(n):
#     sum=0
#     i=0
#     while (n!=0):
#         sum=sum+int(n%10)
#         n=int(n/10)
#     return sum
# n=687
# print(sum(n))

# def find(decimal):
#     if decimal==0:
#         return 0
#     else :
#         return decimal%2+10*find(decimal//2)
# decimal=15
# print(find(decimal))

