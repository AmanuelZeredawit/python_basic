# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
# @ amanuel zeredawit 04/08/2022

def userInput():
    inpStr = input('please enter a string: ')
    get_characters(inpStr)


def get_characters(inpStr):
    iterVar = len(inpStr)

    # using while
    print(f'the character of string {inpStr} using while loop')
    while iterVar > 0:
        print(inpStr[iterVar - 1])
        iterVar -= 1

    # for loop
    print(f'the characters of string {inpStr} using for loop')
    # range(start,stop,step)
    for i in range(len(inpStr)-1, -1, -1):
        print(inpStr[i])




userInput()
