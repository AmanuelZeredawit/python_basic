# Exercise: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.
# @ amanuel zeredawit August 05, 2022

fname = input('enter file name: ')
try:
    fhand = open(fname)
except:
    print('error, enter correct file name')
    exit()
word_dic = dict()
for line in fhand:
    li = line.split()
    for word in li:
        word_dic[word] = word

print(word_dic)
