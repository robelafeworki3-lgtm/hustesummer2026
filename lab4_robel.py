#ticket 1

ages = [25, 30, 35, 40, 45, 10]
for age in ages:
    if age >= 13:
        print("access granted")
    else:age < 13
        print("too young")
#25,30,35,40,45 will print access granted and 10 will print too young   
#the variable age holds the value of each element in the ages list as the loop iterates through it. 
# The if statement checks if the age is greater than or equal to 13, and if so, it prints "access granted". 
# If the age is less than 13, it prints "too young".

#ticket 2

keep_checking = "yes"
while keep_checking == "yes":
    age = int(input("Enter your age: "))
    if age >= 13:
        print("access granted")
    else:
        print("too young")
    keep_checking = input("Do you want to check another age? (yes/no): ")
#no
#we dont know how many times can the user will want to check an age.

#ticket 3

while True:
    user_input = input("Enter an age or type 'stop': ")
    if user_input.lower() == 'stop':
        break
    age = int(user_input)
    print(f"the age you entered is: {age}")
#the loop woould never end.
# ticket 2 can be used to check multiple ages.

#ticket 4

def can_access(age):
    if age >= 13:
        return "access granted"
    else:
        return "too young"
    
#THIS ONE IS BETTER THAN TICKET 1 BECAUSE IT IS MORE FLEXIBLE AND REUSABLE.
#it makes it resuable,easier to read.

#ticket 5

def signup_report(ages):
    approved = 0
    for i , age in enumerate(ages,1):
        if age >= 13:
            status = "access granted"
            approved += 1
        else:
            status = "too young"
        print(f"Signup {i}: Age {age} - {status}")
    print(f"Total approved signups: {approved}")
#5
#functions ,parameters, variable, loops,conditional statements,enumerate function, string formatting, and print statements are used in this code snippet.
