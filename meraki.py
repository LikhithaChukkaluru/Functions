# print("NavGurukul")
# def say_hello():
#     print("Hello!")
#     print("How are you?")
# say_hello()
# print("Python is awesome")
# say_hello()
# print("Hello…")
# say_hello()

# names_list = ["Fiza", "Shivam", "Imtiyaz", "Deepanshu", "Rahman"]
# print(len(names_list))

# def definition_say_hello():
#     print("NavGurukul")
#     print("In Navgurukul, we have to take responsibility for our learning.")
# definition_say_hello()
# print("In Navgurukul we treat all the people in the same way.")
# definition_say_hello()

# def function_say_bye():
#     print("It was fun meeting with you. ")
#     print("Bye bye")
# function_say_bye()
# function_say_bye()
# print("Python is used a lot.")
# function_say_bye()
# function_say_bye()

# def definition_hello_again():
#     print("Again Hello :)")
#     print("How are you?")
# definition_hello_again()

# numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# def max(list):
#     max=list[0]
#     for  i in list :
#         if i>max:
#             max=i
#     return max
# print(max([3, 5, 7, 34, 2, 89, 2, 5]))

# def sum(list):
#     sum=0
#     for i in list :
#         sum+=i
#     return sum
# print(sum([1, 2, 3, 4, 5]))

# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 1]
# unorder_list.sort()
# print(unorder_list)

# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# reverse_list.reverse()
# print(reverse_list)

# def sort (list):
#     min=list[0]
#     for i in list :
#         if i<min:
#             min=i
#     return min
# print(min([8, 6, 4, 8, 4, 50, 2, 7]))

# def sum():
#     print(12+13)
# sum()

# def welcome():
#     print("Welcome to function")
# welcome()

# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven()

# def say_hello(name):
#     print("Hello ", name)
#     print("How are you?")
# say_hello("Aatif")

# def add_numbers(number1, number2):
#     print("I will add two numbers.")
#     print(number1 + number2)
# add_numbers(120, 50)
# num_x = "134"
# name = "Rinki"
# add_numbers(num_x, name)

# def say_hello_language(name, language):
#     if language == "hindi":
#         print("Namaste ", name)
#         print("Aap kaise ho?")
#     elif language == "punjabi":
#         print("Sat sri akaal ", name)
#         print("Tuhada ki haal hai?")
#     else:
#         print("Hello ", name)
#         print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")

# def say_hello_people(name_x, name_y, name_z, name_a):
#     print("Namaste ", name_x) # In hindi
#     print("Alah hafiz ", name_y) # In urdu 
#     print("Bonjour ", name_z) # In french 
#     print("Hello ", name_a) # In english 
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")

# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)
# icecream("chocolate", "butterscotch","vanilla","strawberry")

# def attendance(name,status="absent"):
#     print(name,"is",status," today")
# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")

# def info(name, age = "4"):
#    print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")

# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello",name,"your",currentMilestone,"concept","is clear with the help of",mentorName)
# studentDetails("Nilam","loop","likhitha")

# def funtprint_lines(name,institute):
#     print("myname is",name,"and i'm founder of",institute)
# funtprint_lines("likhitha","agriculture science"

# def add(num1,num2):
#     num3=num1+num2
#     print(num3)
# add(56,12)

# def sum(l,l1) :
#     b=[]
#     for i in range (len(l)):
#         b.append(l[i]+l1[i])
#     return b
# l=[10, 20, 13] 
# l1=[50, 60, 10]
# print(sum(l,l1))

# def check(num1,num2):
#     if num1 %2==0 and num2 %2 ==0 :
#         print("both are even")
#     else :
#         print("both are not even")
# check(16,25)

# def check (l,l1):
#     for i in range (len(l)):
#         for i in range (len(l1)):
#             if l[i] %2==0 and l1[i]%2==0 :
#                 print("both are even")
#             else :
#                 print("both are not even")
# l= [2, 6, 18, 10, 3, 75]
# l1= [6, 19, 24, 12, 3, 87]
# check(l,l1)

# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)

# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print("Hello from NavGurukul ;)")
#     return number_sum
# sum6 = add_numbers_more(100, 20)
# print(sum6)

# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"
# print("Will I be able to print? :-(")
# mon_menu = menu("monday")
# print(mon_menu)
# tues_menu = menu("tuesday")
# print(tues_menu)
# fri_menu = menu("friday")
# print(fri_menu)

# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#         print("Will I be able to print? :-(")
#         return food
#     print("But I'm not sure will print? :'(")
# print(menu("monday"))

# def f1():
#    s = "I Love Navgurukul"
#    def f2():
#        print(s)
#    f2()
# f1()

# def first_function():
#     s = 'I love India'
#     def second_function():
#         print(s)
#     second_function()
# first_function()

# def first_function():
#     s = 'I love India'
#     def second_function():
#         s = "MY NAME IS JACK"
#         print(s)
#     second_function()
#     print(s)
# first_function()

# def check():
#     a=int(input("enter a:"))
#     if a>= 18:
#         print("eligiable")
#     else :
#         print("not eligible")
# check()

# a = int(input("Enter any Minimum Value: "))
# b = int(input("Enter any Maximum Value: "))
# for i in range(a, b ):
#     Sum = 0
#     for n in range(1, i ):
#         if(i % n == 0):
#             Sum = Sum + n
#     if(Sum == i):
#         print(i)

# def sum(num1,num2,num3):
#     sum=num1+num2+num3
#     avg=sum//3
#     print( sum)
#     print(avg)
# sum(12,3,4)

# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)
# employee("kartik",30000)
# employee("deepak")

# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# def meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner":
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))

# def checkKey():
#     car ={"brand":  "ford","model":  "mustang","year":  1964}
#     if "model" in car:
#         print("Yes, 'model' is one of the keys in the thisdict dictionary.")
#     else:
#         print("No, 'model' key dictionary mai nahi hai.")
# checkKey()

# def multi(a,b):
#     multiply=a*b
#     return multiply
# print(multi(3,4))

# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)

# def Avg(number1,number2,number3):
#     Avg=number1+number2+number3/3
#     print(Avg)
# Avg(1,3,2)

# def voter(age):
#     if age < 18:
#         print("eligible")
#     else:
#         print("not eligible")
# voter(20)

# def distance(kms):
#     if kms < 20:
#         print("close")
#     elif kms < 50:
#         print("median")
#     else:
#         print("far")
# distance(56)

# def fun(name,age=25):
#     print(name,age)
# fun("emma",20) 

# def fun(name,age=25):
#     print(name,age)
# fun("emma",20)

# def sumofdigits(number):
#     sum = 0
#     while number > 0 :
#         modulus = number%10
#         sum+=modulus
#         number//=10
#     return sum
# print(sumofdigits(123))

# def primeorNot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeorNot(406)

# d=dict ()
# for i in range (1,16):
#     d[i]=i**2
# print(d)


# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# while True:
#     choice = input("Enter choice(1/2/3/4): ")
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
    