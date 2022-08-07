# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

# Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

# @ amanuel zeredawit August 06, 2022

fname = input('enter file name: ')
try:
    fhand = open(fname)
except:
    print('file name does not exist')
    exit()
count = dict()

# to get the person who sent highest number of emails
def max_email(count):
    highest = None
    for key in count:
        if highest is None or count[key] > highest:
            highest = count[key]
            max_key = key
    print(f'the email {max_key} has most messages which is {highest}')



for line in fhand:
    if not line.startswith('From '):continue
    email = line.split()[1]
    #print(email)
    count[email] = count.get(email, 0) + 1
    # if email in count:
    #     count[email] = count[email] + 1
    # else:
    #     count[email] = 1
print(count)
max_email(count)



