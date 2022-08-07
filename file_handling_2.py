# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence90 CHAPTER 7. FILES
# values from these lines. When you reach the end of the file, print out
# the average spam confidence

# @ amanuel zeredawit August 05,2022

def countSpam(fhand):
    count = 0
    total = 0
    for line in fhand:
        if not line.startswith('X-DSPAM-Confidence:'):
            continue
        # print(line)
        spos = line.find(':')
        # print(line[spos + 2: ])
        count += 1
        total = total + float(line[spos + 2: ])
    print('The average spam confidence is ', total/count)






def inputFile():
    fname = input('enter file name: ')
    try:
        fhand = open(fname)
    except:
        print('please enter right file name:', fname)
        exit()
    countSpam(fhand)
inputFile()
