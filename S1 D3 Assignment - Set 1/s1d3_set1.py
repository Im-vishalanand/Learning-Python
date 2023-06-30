#1
print("Hello, World!")



#-----------------------------------------------------------------



#2
# Integer
myInt = 10

# Float
myFloat = 3.14

# String
myString = "Hello, World!"

# Boolean
myBoolean = True

# List
myList = [1, 2, 3, 4, 5]

# Tuple
myTuple = (6, 7, 8, 9, 10)

# Dictionary
myDict = {"name": "John", "age": 25, "city": "New York"}

# Set
mySet = {1, 2, 3, 4, 5}

print(f"Type of myInt: {type(myInt)}, value: {myInt}")
print(f"Type of myFloat: {type(myFloat)}, value: {myFloat}")
print(f"Type of myString: {type(myString)}, value: {myString}")
print(f"Type of myBoolean: {type(myBoolean)}, value: {myBoolean}")
print(f"Type of myList: {type(myList)}, value: {myList}")
print(f"Type of myTuple: {type(myTuple)}, value: {myTuple}")
print(f"Type of myDict: {type(myDict)}, value: {myDict}")
print(f"Type of mySet: {type(mySet)}, value: {mySet}")



#-----------------------------------------------------------------



#3
# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))  
print("Original list:", numbers)

# Adding the number 20 to the list
numbers.append(20)  
print("List after adding 20:", numbers)

# Remove the number 3 from the list
numbers.remove(3)  
print("List after removing 3:", numbers)

# Sort the list in ascending order
numbers.sort()  
print("Sorted list:", numbers)



#-----------------------------------------------------------------




#4
# List of numbers
numbers = [10, 20, 30, 40]  

# Calculate the sum of numbers
sum_of_numbers = sum(numbers)  

# Calculate the average of numbers
average_of_numbers = sum_of_numbers / len(numbers)  

print("Sum:", sum_of_numbers)
print("Average:", average_of_numbers)



#-----------------------------------------------------------------



#5
def reverseString(str):
    rev = ""
    for char in str:
        rev = char + rev
    return rev

# Example usage
string = "Python"
rev = reverseString(string)
print(rev)



#-----------------------------------------------------------------





#6
def countVowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0

    for char in str:
        if char in vowels:
            count += 1

    return count

# Example usage
string = "Hello"
count = countVowels(string)
print("Number of vowels:", count)

#-----------------------------------------------------------------


#7
def checkPrime(num):
    if number < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

number = 13
if checkPrime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")



#-----------------------------------------------------------------


#8
def fact(n):
    if n == 0:
        return 1
    
    fact=1

    for i in range(1, n+1):
        fact*=i

    return fact

# Example usage
number = 5
result = fact(number)
print("Factorial of", number, "is", result, ".")



#-----------------------------------------------------------------

#9

def fibonacci(n):
    sequence = [0, 1]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Example usage
n = 5
fib_sequence = fibonacci(n)
print(fib_sequence)


#-----------------------------------------------------------------


#10

squares = [num ** 2 for num in range(1, 11)]

print(squares)