# practise using the Enumerate function

top_friends = ['Noah', 'Anna', 'Fred']

# iterating normally
#for i in range(3):
#    print(f'my top {i+1} friend is {top_friends[i]}')

# ****when you want to iterate over something 
# and want to access the index, enumerate func is useful****

for i, friend in enumerate(top_friends):
    print(f'My top {i+1} friend is {friend}')

# enumerate is a generator, returns a tuple
friend_g = enumerate(top_friends)
print(next(friend_g))