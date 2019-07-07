'''
counter,
defaultdict,
ordereddict (not in this file),
namedtuple,
deque
'''

#   counter - keeps track of how many times an element appears
from collections import Counter
'''
device_temp = [14.0, 14.5, 15.0, 14.0, 15.0, 15.0, 15.5]
temp_count = Counter(device_temp)
print(temp_count)
print(temp_count[14.0])
'''

# defaultdict - never raises key error, just returns the value
# returned by the func when the object was created
from collections import defaultdict
'''
coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'),('Rolf', 'Cambridge')]

# defaultdict takes in a function: list
alma_mater = defaultdict(list)

# if key doesnt exist in dict
# then function called empty list created ^^
for coworker in coworkers:
    alma_mater[coworker[0]].append(coworker[1])

# If you want to raise an error from invalid keys, 
# set default factory to None.  Note that empty lists still created above

alma_mater.default_factory = None

print(alma_mater['Rolf'])
print(alma_mater['Noah'])
'''

# named tuple.  A more explicit way of using tuples!
# Good for reading from databases and CSVs
from collections import namedtuple
'''
account = ('checking', 1850.90)
Account = namedtuple('Account', ['name', 'balance'])
accountNamedTuple = Account(*account)

print(accountNamedTuple)
print(accountNamedTuple._asdict()['balance'])
'''

# Double ended queue, can push/remove items from
# front or back of queue.  GOOD FOR THREADS (thread safe)
from collections import deque
'''
friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))

# Working at the back
friends.append('Jose')
friends.pop()

# Working at the start
friends.appendleft('Noah')
friends.popleft()
print(friends)
'''