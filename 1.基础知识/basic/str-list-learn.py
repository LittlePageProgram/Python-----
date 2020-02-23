msg = "Hello Eric, would you like to learn some Python today."
print(msg)
msg = "Steve yu"
print(msg.upper())
print(msg.lower())
print(msg.lower().title())
msg2 = 'Albert Einstein once said, "A person who never made a mistake never tried anything new"'
print(msg2)
msg3 = "    hi strip    "
print(msg3.lstrip())
print(msg3.rstrip())
print(msg3.strip())


# list
bicycles = ['trek', 'cannondale', 'redline']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
bicycles[0] = 'hello'
print(bicycles)

bicycles.append('hello')

bicycles.insert(1, 'steveyu')

del bicycles[0]

print(bicycles)

val = bicycles.pop()

print(bicycles, val)

bicycles.sort()

print(bicycles)

bicycles.reverse()

print(bicycles)



print(len(bicycles))