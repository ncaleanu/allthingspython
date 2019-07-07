# Practising some more advanced functions in Python: generators, fitlers, maps


class sys:
    def __init__(self, name):
        self.name = name
        self.state = 0

    def toggle(self):
        if self.state is 0:
            self.state = 1
        elif self.state is 1:
            self.state is 0
        return self


# Display the list of systems
def display_names(sys_list):
    for sys in sys_list:
        print("   ", sys.name, ":", sys.state)


# Create a generator filter
def my_filter(func, iterable):
    for i in iterable:
        if func(i) is 0:
            yield i

sys1 = sys('Lights')
sys2 = sys('Pressure')
sys3 = sys('Doors')

# iterable
systems = [sys1, sys2, sys3]

# using filter defined above, create new list from lambda func and iterable
sys_OFF = list(my_filter(lambda x: x.state, systems))
print("SYSTEMS OFF: ")
display_names(sys_OFF)

# Now use mapping function to turn all currently off systems back ON.
sys_ON = list(map(lambda sys: sys.toggle(), sys_OFF))
print("SYSTEMS ON: ")
display_names(sys_ON)

