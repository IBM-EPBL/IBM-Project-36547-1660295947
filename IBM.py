

 

1) write a program, to test a given number is prime or not 
num = 11 
if num > 1: 
for i in range(2, int(num/2)+1): 
if (num % i) == 0: 
print(num, "is not a prime number") 
break 
else: 
print(num, "is a prime number") 
else: 
print(num, "is not a prime number") 

2) write a program, to generate a odd numbers from m to n using while loop 
m=int(input('Enter the number')) 
n=int(input('Enter the number')) 
while(n<=m): 
if n%2!=0: 
print(n) 
n+=1 

3) write a Python program, to display prime numbers series upto given number
upper = int(input()) 
for num in range(1, upper + 1): 
if num > 1: 
for i in range(2, num): 
if (num % i) == 0: 
break 
else: 
print(num) 

4) write a python program to generate fibonacci series 
nterms = int(input("How many terms? ")) 
n1, n2 = 0, 1 
count = 0 
if nterms <= 0: 
print("Please enter a positive integer") 
elif nterms == 1: 
print("Fibonacci sequence upto",nterms,":") 
print(n1) 
else: 
print("Fibonacci sequence:") 
while count < nterms: 
print(n1) 
nth = n1 + n2 
n1 = n2 
n2 = nth 
count += 1
 
4) write a python program to generate fibonacci series 
nterms = int(input("How many terms? ")) 
n1, n2 = 0, 1 
count = 0 
if nterms <= 0: 
print("Please enter a positive integer") 
elif nterms == 1: 
print("Fibonacci sequence upto",nterms,":") 
print(n1) 
else: 
print("Fibonacci sequence:") 
while count < nterms: 
print(n1) 
nth = n1 + n2 
n1 = n2 
n2 = nth 
count += 1

