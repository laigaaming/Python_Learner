guests = ['Ben', 'Jack', 'Tom']

print('I can only invite two of you.')

guests.insert(0, 'John')
guests.insert(2, 'David')
guests.append('Leon')

pop_guest1 = guests.pop()
print('Sorry ' + pop_guest1 + ', you are not invited.')
pop_guest2 = guests.pop()
print('Sorry ' + pop_guest2 + ', you are not invited.')
pop_guest3 = guests.pop()
print('Sorry ' + pop_guest3 + ', you are not invited.')
pop_guest4 = guests.pop()
print('Sorry ' + pop_guest4 + ', you are not invited.')

message0 = 'Hi ' + guests[0] + ', would you like to have dinner with me?'
message1 = 'Hi ' + guests[1] + ', would you like to have dinner with me?'


print(message0)
print(message1)
print(guests.__len__())
del guests[1]
del guests[0]
print(guests)
print(guests.__len__())
