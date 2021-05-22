
# Python program to
# demonstrate merging
# of two files
  
data = data2 = ""
  
# Reading data from file1
with open('test.txt') as fp:
    data = fp.read()
  
# Reading data from file2
with open('train.txt') as fp:
    data2 = fp.read()
  
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2
  
with open ('trainv1.txt', 'w') as fp:
    fp.write(data)