# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the number of messages from each
# person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.
# Sample Line:
# # From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Enter a file name: mbox_short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195


# @ amanuel zeredawit August 07,2022

# open file to read
fname = input("enter file name: ")
try:
    fhand = open(fname)
except:
    print(f'enter correct file name {fname}')
    exit()
count = dict()

# construct a dictionary of {email:values,}
for line in fhand:
    if not line.startswith('From '):continue
    email = line.split()[1]
    #print(email)
    count[email] = count.get(email, 0) + 1
#print(count)

# use tuple to arrange emails in descending order by values
lst = list()
for key, val in list(count.items()):
    lst.append((val, key))
lst.sort(reverse=True)

# show only the first three
for key, val in lst[:3]:
    print(key, val)



