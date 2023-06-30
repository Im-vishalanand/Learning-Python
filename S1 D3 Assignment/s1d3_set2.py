#1


for i in range(1, 6):

    for j in range(1, i+1):

        print(j, end=" ")
    
    print()




#-----------------------------------------------------------------

#2

numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 500:
        break 
    if number > 150:
        continue 
    if number % 5 == 0:
        print(number)


#-----------------------------------------------------------------


#3

s1 = "Ault"
s2 = "Kelly"

mid= len(s1) // 2
s3 = s1[:mid] + s2 + s1[mid:]

print(s3)



#-----------------------------------------------------------------


#4

str1 = "PyNaTive"

lowercase = []
uppercase = []

for char in str1:
    if char.islower():
        lowercase.append(char)
    else:
        uppercase.append(char)

str = ''.join(lowercase + uppercase)

print(str)


#-----------------------------------------------------------------


#5

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]

# Add any leftover items from the longer list
if len(list1) > len(list2):
    new_list += list1[len(list2):]
else:
    new_list += list2[len(list1):]

print(new_list)


#-----------------------------------------------------------------


#6

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concatenated_list = [item1 + item2 for item1 in list1 for item2 in list2]

print(concatenated_list)