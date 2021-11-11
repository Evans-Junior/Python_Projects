with open('test.txt','w') as write_file:
  
    write_file.write('Hey there ninjas,  python is awesome')
    
with open('test.txt','a') as write_file:
    write_file.write('\n Hey there ninjas,  python is awesome')