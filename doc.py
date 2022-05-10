# 1.
# def word(num):
    # count=0
    # for i in num:
    #     if len(i) > 2 and i[0]==i[-1]:
    #         count+=1
            
    # return count
#     print(count)    
# word(['abc', 'xyz', 'aba', '1221'])
# print(word(['abc', 'xyz', 'aba', '1221']))

 # 2.

# def max(a,b,c):
#     if a > b and a>c :
#         print(a)
#     elif b>a and b>c :
#         print(b)
#     elif c>a and c>b :
#         print(c)
# max(12,78,90)

# def max ():
#     a=int(input("enter a:"))
#     b=int(input("enter a:"))
#     c=int(input("enter a:"))
#     if a > b and a>c :
#         print(a)
#     elif b>a and b>c :
#         print(b)
#     elif c>a and c>b :
#         print(c)
# max()

# def max(a,b,c):
#     if a > b and a>c :
#        return a
#     elif b>a and b>c :
#         return b
#     elif c>a and c>b :
#        return c
# print(max(12,78,90))

# def largest (a,b,c):
#      if a > b and a>c :
#        largest= a
#      elif b>a and b>c :
#         largest= b
#      else :
#         largest=c
#         return largest
# print(max(12,89,67))

# 3.
# def sum(list):
#     sum=0
#     for i in list :
#         sum+=i
#     return sum
# print(sum((8, 2, 3, 0, 7)))
# list=[8,2,3,0,7]
# print(sum(list))

# 4.

# def reverse (string):
#     reverse =string[::-1]
#     print(reverse)
# (reverse(["1","2","3","4","a","b","c","d"]))

# def reverse (string):
#     rev=""
#     for i in range (len(string),0,-1):
#         rev+=string[i-1]
#     print(rev)
# reverse(["1","2","3","4","a","b","c","d"])

# 5.
# def unique (list):
#     b=[]
#     for i in  list:
#         if (i) not in b :
#             b.append(i)
#     print(b)
# list=[1,2,3,3,3,3,4,5]
# unique(list)

# def unique (list):
#     b=[]
#     i=0
#     while i<len(list):
#         if list[i] not in b :
#             b.append(list[i])
#         i+=1
#     return b
# list=[1,2,3,3,3,3,4,5]
# print(unique(list))

# 6.

# def even(l):
#     i=0
#     b=[]
#     while i<len(l):
#         if l[i]%2==0 :
#             b.append(l[i])
#         i+=1
#     return b
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(even(l))

# 7.

# def bmi(weight,height):
#     bmi=weight/(height*height)
#     if bmi<18.5 :
#         return "underweight"
#     if bmi<=25  :
#         return "Normal"
#     if bmi <=30.0  :
#         return "over weight"
#     if bmi > 30:
#         return "obeese"
# print(bmi(90,150))

# 8.

# def string(l):
#     count=0
#     count1=0
#     for i in l :
#         if i.islower():
#             count+=1
#         elif i.isupper() :
#             count1+=1
#     print(count)
#     print(count1)
# string('ThequickBrowFox')

#9.

# def values():
#     l=[]
#     for i in range (1,31):
#         l.append(i**2)
#     print(l[:5])
#     print(l[-5:])
# values()

# 10.

# def out(l):
#     i=0
#     sum=0
#     while i<len(l) :
#         sum+=int(l[i])
#         i+=1
#     print(str(sum))
# l="4","5"
# out(l)  

# 11.

# def sum (min,max,step):
#     b=[]
#     for i in range (min,max+1,step):
#         b.append(i)
#     return b
# print(sum(2,10,2))

# 12.

# def num(l):
#     b=[]
#     c=""
#     if "0" not in l :
#         c+=l
#     b.append(l)
#     print(b)
# num(14500)

# 13.

# def even(num):
#     if num%2==0:
#         return "even"
#     else :
#         return "odd"
# print(even(12378))

# 14.

# def prime (num):
#     if num > 1 :
#         for i in range (2,num):
#             if num%i==0 :
#                 print(num,"is not a prime number")
#                 print(i,num//i)
#                 break
#             else :
#                 print(num, "is not a prime number")
#     else :
#         print("not  a prime number")
# prime(234)

# 16.

# def table (num):
#     i=1
#     while i<=10:
#         print(num,"*",i,"=",num*i)
#         i+=1
# table(12)

# 17.

# def vote(age):
#     if age >=18 :
#         return "eligible"
#     else :
#         return "not eligiable"
# print(vote(45))

# 19.

# def func(x = 1, y = 2):
#     x = x + y
#     y += 1
#     print(x, y)
# func(y = 2, x = 1)
# func()

# 20.

# num = 1
# def func():
#     num = 3
#     print(num)
# func()
# print(num)

# 21.

# num = 1
# def func():
#     num=3
#     num = num + 3
#     print(num)
# func()
# print(num)

# 22.

# num = 1
# def func():
#     global num
#     num = num + 3
#     print(num)
# func()
# print(num)

# 24.

# def test(x =1, y=2 ):
#     x = x + y
#     y += 1
#     print(x, y)
# test(2, 1)
# test()

# 25.

# def count(l):
#     count=0
#     count1=0
#     for i in  (l):
#         if i >= 0 :
#             count+=1
#         elif i < 0 :
#             count1+=1
#     print(count)
#     print(count1)
# l=[2, -7, 5, -64, -14]
# count(l)

# 26.

# def func(num):
#     for i in range (num) :
#         if num%5==0 and num%3 ==0:
#             return"FizzBuzz"
#         elif num%3 ==0:
#             return"Fizz"
#         elif num%5==0 :
#             return"Buzz"
#         else :
#             return (num)
# print(func(45))

# 27.

# def KM(speed):
#     if speed <=70 :
#         return "ok"
#     else :
#         r= (speed-70)//5
#         if r<=12 :
#             return r
#         else :
#             return "license suspended"
# print(KM(90))

# 28.

# def shownumbers(limit):
#     for i in range (limit):
#         if i%2!=0 :
#             print(i,"odd")
#         else :
#             print (i,"even")
# (shownumbers(101))

# 29.

# def  fun(limit):
#     sum=0
#     for i in range (1,limit+1):
#         if i%3==0 or i%5==0 :
#             sum+=i
#     return sum
# print(fun(20))

# 30.

# def prime (limit):
#     for limit  in range (1,limit):
#         if limit > 1:
#             for i in range (2,limit) :
#                 if limit%i ==0:
#                     break
#             else :
#                     print(limit)
# prime(100)
    
# def prime (limit):
#     for i in range (2,limit):
#         for j in range (2,i):
#             if i%j==0:
#                 break
#         else :
#             print(i)
# prime(1000)

# 31.

# def table(number):
#     for num in range(1,11):
#         print (str(num),"*",str(number),"="+str(num * number))
# (table(5))

# 32.

# def num():
#     l=[]
#     n=int(input("enetr n :"))
#     i=0
#     while i<=n:
#         b=2**i
#         l.append(b)
#         i+=1
#     print(l)
# num()

# 34.

# def  larger(l):
#     sum=0
#     l.sort()
#     sum+=l[-1]+l[-2]
#     return sum
# # l=[10, 14, 2, 23, 19]
# l=[99, 2, 2, 23, 19]
# print(larger(l))

# 35.

# def num(age):
#     if age <=14 :
#         return ("kids drink toddy")
#     elif age>14 and age <=18 :
#         return ("teens drink coke")
#     elif age >18 and age <=21:
#         return ("young drink beer")
#     else :
#         return ("adults drink whisky")
# a=int(input("enetr a:"))
# print(num(a))

# 37.

# def sum(l):
#     count=0
#     i=0
#     while i<len(l):
#         if l[i] =="True":
#             count+=1
#         i+=1
#     return count    
# l=["True","True","True","False","True","True","True","True","True","False","True","False","True","False","False","True","True","True","True","True","False","False","True","True"]
# print(sum(l))

# 40.

# def square (l):
#     for i in  (l):
#         b=str(i**2)
#     return b
# l=[9,1,1,9]
# print(square(l))

# 41.
# def max(l):
#     max=0
#     for i in l:
#         if len(i)>max:
#             max=len(i)
#             res=i   
#     return res,max
# l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# print(max(l))
 
# def min(l):
#     min=l[0]
#     for i in l:
#         if len(min)>len(i):
#             min=i
#         return min,len(min)
# print(min([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# 42.

# def sum(l):
#     b=[]
#     for i in l :
#         sum=0
#         for digit in str(i):
#             sum+=int(digit)
#         b.append(sum)
#     return b 
# l=l=[2345,876,648,87513,758]
# print(sum(l))

# def sum(l):
#     b=[]
#     for i in range (len(l)): 
#         c=l[i]//10
#         d=l[i]%10
#         e=c+d
#         b.append (e)
#         i+=1
#     return b
# l=[12, 67, 98, 34]
# print(sum(l))

# 43.

# def ele(l):
#     n=int(input("enetr :"))
#     b=l[:n]
#     c=l[n:]
#     print(b)
#     print(c)
# l=['a', 1, 2, 5, 'b', 'q']
# ele(l)

# 44.

# def ele(l):
#     b=l[::-1]
#     print(b)
#     n=int(input("enetr :"))
#     c=b[:n]
#     print(c)
# l=['a', 1, 2, 5, 'b', 'q']
# ele(l)

# 45.

# def list():
#     l=[]
#     i=1
#     while i<=10:
#         a=int(input("enetr a:"))
#         l.append(a)
#         i+=1
#     print(l)
#     for i in l :
#         if (i)%2!=0 :
#             print(i*-1)
#         if (i)%2==0:
#             print(i*100)
# (list())

# list()

# 48.

# def pow():
#     a=int(input("enter a :"))
#     b=int(input("enter b:"))
#     pow=a**b
#     return pow
# print(pow())

# 49.

# def n(num):
#     for i in range (num):
#         if num%2!=0 :
#             return "odd"
#         else :
#             return "even"
# print(n(1020))

# 50.

# s="i am good girl"
# print(s.split())

