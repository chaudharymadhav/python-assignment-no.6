# Question number 1

n=int(input("Enter a positive integer-:"))
list1=[]
for item in range(1,n):
    if n%item==0:
        list1.append(item)
print("proper positive divisors of",n,"are",list1)
if sum(list1) == n :
    print("Yes it is a perfect number")
else :
    print("No it is not a perfect number")

# Question number 2

string1=input("Enter a string of your choice and check whether a passed string is palindrome or not-:")
string3=string1.replace(" ","")
string2=string3[::-1]

if string3==string2:
    print("yes it is a palindrome")
else :
    print("No it is not a palindrome")


# Question number 3
import math as M
n = int(input("Enter the number of rows-:"))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(M.factorial(i)//(M.factorial(j)*M.factorial(i-j)),end=" ")
    print()


# Question number 4

import string
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for i in alphabet:
      if i not in str.lower():
         return False
   return True

string = input("Enter a string: ")
if True:
   print("Yes, the given string is a pangram.")
else:
   print("No, the given string is not a pangram")


# Question number 5

word=input("Enter hyphen-separated sequence of words : ")
items=[n for n in word.split('-')]
items.sort()
print('-'.join(items))


# Question number 6

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class: {kwargs['student_class']}")


student_data(student_id='21107038', student_name='Madhav chaudhary')

student_data(student_id='21107038', student_name='Madhav chaudhary', student_class ='2nd Semester')


# Question number 7

class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))


# Question number 8

list=[]
def findTriplets(arr, n):

    found = False
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    list.append([arr[i],arr[j],arr[k]])
                    print(list)
                    found = True

    if (found == False):
        print(" not exist ")

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)


# Question number 9

class validity:

    def f(str):

        a= ['()', '{}', '[]']

        while any(i in str for i in a):

            for j in a:

                str = str.replace(j, '')

        return not str

s = input("enter : ")

print(s, "-", "is balanced"

      if validity.f(s) else "is Unbalanced")
