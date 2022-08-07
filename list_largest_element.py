# write another program that prompts for a list of numbers
#  and at the end prints out  the maximum, minimum ,count and
# average of the numbers

# @ amanuel zeredawit August 03,2022


def getSmallest(numberList):
    smallestNum = None
    for number in numberList:
        if smallestNum is None or number < smallestNum:
            smallestNum = number
    return smallestNum

def getaverage(numberList):
    count = 0
    sum = 0
    for number in numberList:
        count += 1
        sum = sum + number
    average = sum/count
    return count, average




def getLargest(numberList):
    largestNum = None
    for number in numberList:
        if largestNum is None or number > largestNum:
            largestNum = number
    return largestNum


def userInput():
    numberList = []
    while True:
        inp = input('please enter set of numbers one by one: ')
        try:
            if inp == 'done':
                break
            else:
                inpFloat = float(inp)
                numberList.append(inpFloat)
        except:
            print('please enter a number')
    print('Here is the list of numbers: ', numberList)
    print('The largest number in the list is :', getLargest(numberList))
    print('The smallest number in the list is :', getSmallest(numberList))
    count, average = getaverage(numberList)
    print(f'The count is {count} and average is {average}')
    #print('The count is {0} and average is {1}'.format(count, average))
    
userInput()
