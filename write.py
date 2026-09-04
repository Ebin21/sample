exmp2 = 'example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
print( f"Done writing to file and the file opened is {writefile.name} and the mode is {writefile.mode} and the file is closed: {writefile.closed}")
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())