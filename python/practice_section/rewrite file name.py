# rewrite file name
filename1 = input("Enter the input file name: ")
filename2 = input("Enter the output file name: ")
file1 = open(filename1)
file2 = open(filename2, 'w')
file2.writelines(file1)
file2.close()
file1.close()
