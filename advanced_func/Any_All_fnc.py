# Practise using ANY and ALL 

friends = [
    {
        'name': 'Noah',
        'location': 'Vancouver'
    },
    {
        'name': 'John',
        'location': 'Sydney'
    },
    {
        'name': 'Polly',
        'location': 'Vancouver'
    }
]

your_location = input("Where are you right now? ")
friends_nearby = [friend for friend in friends if friend['location'] == your_location]
print(friends_nearby)

# Evaluates the bool value and if ANY are True
# it evaluates to True
if any(friends_nearby):
    print("You are not alone")

# Evaluates to TRUE if dict are non-empty
if all(friends_nearby):
    print("All friends are in your location")

