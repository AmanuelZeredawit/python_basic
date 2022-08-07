# Exercise : Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.
# @ amanuel zeredawit July 05,2022

str = 'X-DSPAM-Confidence:0.8475'

spos =str.find(':')
epos =str.find(' ', spos)
print(str[spos + 1:])