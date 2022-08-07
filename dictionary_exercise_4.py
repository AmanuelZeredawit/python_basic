# Exercise : This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

# @ amanuel zeredawit August 06,2022

fname = input('enter file name: ')


try:
    fhand = open(fname)
except:
    print("can't open file, enter correct file name: ")

count = dict()
for line in fhand:
    if not line.startswith('From '): continue
    spos = line.find('@')
    epos = line.find(' ', spos)
    dname = line[spos + 1:epos]
    # print(dname)
    count[dname] = count.get(dname, 0) + 1
print(count)

