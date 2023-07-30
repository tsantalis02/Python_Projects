def  fibonacci(n):
   if n == 1  or n == 0:
       return n;
   else:
       return fibonacci(n-2) + fibonacci(n - 1)

#Test function
num = int(input("Give a positive integer number: "))
while num < 0:
    print("Number not valid!")
    num = int(input("Give a positive integer number: "))
print("Fibonacci sequence: ")
for i in range(0, num):
	print(fibonacci(i),end=" ")