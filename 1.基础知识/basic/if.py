
cars = ['audi', 'bmw', 'subaru']

for car in cars:
    if(car == 'audi'):
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'

print(car == 'bmw')


if 'bmw' in cars:
    print('wow')

if 'steve' not in cars:
    print('too pity')
    cars.append('steve')
print(cars)
