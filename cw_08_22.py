# # python-basics1-review-cw
#
### Problem 1:
# Create a program that prints the user input until they enter 'q' to quit.

userInp= input("Enter the input: ")
while (userInp !='q'):
    userInp=input("Enter the input: ")

# ### Problem 3:
# Create a program that takes user input in a while loop. If they enter 1, print 1. If they enter 2,
# print 2. If they enter 3 print 3. If they enter ‘q’ or 0 (your choice), quit. Else, print “ERROR”.

userInp= input("Enter  1, print 1. enter 2,print 2. enter 3 print 3. enter ‘q’ to quit. Else, print “ERROR”.: ")
while (userInp !='q'):
    if(userInp=='1'):
        print('1')
    elif(userInp=='2'):
        print('2')
    elif(userInp=='3'):
        print('3')
    else:
        print("ERROR")
    userInp=input("Enter the input: ")


# ### Problem 4:
# Create a program that takes the user input until they enter 'q'.
# # You should store all of their input and separate the input with a comma. Once they enter 'q',
# print all of the comma separated words they entered.


userInp= input("Enter the input: ")
finalOutput = ""
while (userInp !='q'):
    finalOutput= finalOutput +  "," + userInp

    userInp=input("Enter the input: ")
print(finalOutput)