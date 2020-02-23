alien = {'color': 'green', 'points': 5}


print(alien['color'])
print(alien['points'])

print(alien)

alien['x_position'] = 5

print(alien)

for k, v in alien.items():
    print("key " + k)
    print("value " + str(v))

print()

for k in alien.keys():
    print(k)
    print(alien[k])

