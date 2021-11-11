with open('test.txt') as new_file:


#    for line in new_file:
#        print(line.rstrip())
#  print(new_file.read)   
#  print(new_file.seek(0))
# new_file.seek(0)

    new_file.seek(0)
    lines=new_file.readlines()
    line= new_file.read(300)
print(lines)