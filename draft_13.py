# https://my.smeuh.org/al/blog/lost-in-scope
# Does not work properly
callbacks = []
days = "monday tuesday wednesday thursday friday saturday sunday".split()
for day in days:
    callbacks.append(lambda: "Today is %s." % day)

print(callbacks[0]())

# And this try neither
callbacks = []
days = "monday tuesday wednesday thursday friday saturday sunday".split()
for day in days:
    def callback():
        return "Today is %s." % day


    callbacks.append(callback)

print(callbacks[0]())

# Why ?, checke the following to explain why:
#
# http://alicebob.cryptoland.net/closure-gotcha-with-python/
"""
The function make_number_printer receives a number and returns a function which,
when called, prints that same number. It’s not the most useful function in the world,
but it does show how closures work. In this case, the number_printer function is a closure,
because it references the variable n which is in an outer scope (of the make_number_printer function).
"""


def make_number_printer(n):
    def number_printer():
        print(n)

    return number_printer


printer = make_number_printer(5)
printer()

"""
My intention here, though, it’s not to explain what closures are but to show a property of them which
may cause some confusion (and made me spent quite some time hunting for a bug caused by it).
What does this code prints when run?
"""

printer_lst = []
for i in range(10):
    def number_printer():
        print(i)


    printer_lst.append(number_printer)

for printer in printer_lst:
    printer()

"""
It loops between 0 and 10 creating a number_printer function and appending it to a list. 
Then it loops through the functions of the list, calling them. You would expect it to print the numbers 0 to 9, right?

Wrong! It prints the number 9 ten times.

The problem is that most people (including me, before learning this) think that closures work by evaluating 
the variables in the outer scope and storing their values to use when necessary. But actually they keep an 
reference to those variables, and if their contents change, the closure will use the new value. 
Since our variable i stores the value 9 after the closures are created, that is the value they will print. 
This happens even if the variable i goes out of scope after the closures are created 
(e.g., if the first for were inside a function).

So how to solve this? You can move the creation of the closure to another function, like this:
"""


def make_number_printer(n):
    def number_printer():
        print(n)

    return number_printer


printer_lst = []
for i in range(10):
    printer_lst.append(make_number_printer(i))

for printer in printer_lst:
    printer()

"""
Here the closure will reference the variable n, which has different instances for each different closure created. 
Another alternative is to use a somewhat contrived Python “feature” which is the fact that default parameter values 
are evaluated when the function is defined and not when they are called:
"""

printer_lst = []
for i in range(10):
    def number_printer(x=i):
        print(x)


    printer_lst.append(number_printer)

for printer in printer_lst:
    printer()

"""
When def number_printer(x=i): is run, the variable i is evaluated and its value is saved in the function definition; 
so, each time the function is defined (i.e., the closure is created), the current value of i is “frozen”.
"""

"""
If somebody is thinking, “but I’ll never run into this situation”, here is a little more real example 
(which actually happened to me when I was coding a Flash game, which uses ActionScript). 
Basically it’s the same code above and has the same issue:
"""


class Button:
    # This is a dummy Button class; suppose
    # it's part of a GUI library and for some reason
    # you can't subclass it

    def __init__(self):
        self.listener = None

    def set_click_listener(self, fn):
        self.listener = fn

    def on_click(self):
        self.listener()


# Create 10 buttons...
buttons = [Button() for i in range(10)]
# And suppose the buttons are added to the GUI after

# Set the listeners to the click event.
# The number of buttons may change in the future
# and all of them have the same code, the
# only difference is the button index. So it's better
# to do this within a loop.
for i in range(10):
    def on_click():
        # Suppose there is something more useful here
        print(i)


    buttons[i].set_click_listener(on_click)

# Simulate a click in each button
for j in range(10):
    buttons[j].on_click()

# Back to the beginning:
"""
In Python, Ruby and JavaScript, if we create callbacks within a for loop, the variable available to those 
callbacks will be the one and unique variable which belongs to the function where we've written the 
for loop and which has been overwritten at each iteration, not the value the variable had when the 
callback was created. But in Ruby and JavaScript, if we iterate in a functional way, the function (or block) 
in which we create our callbacks gets passed a different value at each iteration and doesn't overwrite 
that value while it's executing so each callback will refer to a different value. Using this idea, 
in Python we can do:
"""


def make_callback(day):
    def callback():
        return "Today is %s." % day

    return callback


days = "monday tuesday wednesday thursday friday saturday sunday".split()
callbacks = []
for day in days:
    callbacks.append(make_callback(day))

print(callbacks[0]())
print(callbacks[3]())

"""
Or more succinctly, because in Python default values get evaluated when the function is created 
(which is another source of confusion), we can do this:
"""

days = "monday tuesday wednesday thursday friday saturday sunday".split()
callbacks = [lambda day=day: "Today is %s." % day for day in days]
print(callbacks[1]())
print(callbacks[5]())
