# Exercise : Find all unique words in a file
# Shakespeare used over 20,000 words in his works. But how would you
# determine that? How would you produce the list of all the words that
# Shakespeare used? Would you download all his work, read it and track
# all unique words by hand?
# Let’s use Python to achieve that instead. List all unique words, sorted
# in alphabetical order, that are stored in a file romeo.txt containing a
# subset of Shakespeare’s work.
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
# Create a list of unique words, which will contain the final result. Write
# a program to open the file romeo.txt and read it line by line. For each

# @ amanuel zeredawit August 05, 2022

def userInput():
    fname = input('enter name of the file: ')
    try:
        fhand = open(fname)
    except:
        print('error, enter correct file name')
        exit()
    words_list(fhand)


def words_list(fhand):
    new_list = []
    for line in fhand:
        lst = line.rstrip().split()
        #print(lst)
        for word in lst:
            if word in new_list: continue
            new_list.append(word)
    print(sorted(new_list))

userInput()
