# def greet():
#     print('hello world')
    
# greet()
# greet()
# greet()
# greet()


# def greet(name='ryu',time='morning'):
#     print(f'Good {time} {name}, hope you are well')
    
# # name = input('enter your name:')
# # time = input('enter the time of day:')

# greet('Evans','afternoon')

def area(radius):
    return 3.142*radius*radius
    
    
def vol(area,length):
    print(area*length)
    
radius = int(input('enter a radius:'))
length = int(input('enter a length:'))

area_calc = area(radius)
vol(area_calc,length)