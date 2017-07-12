# String Class
# Pour rechercher/remplacer, nous avons à notre disposition les
# méthodes count, find et replace

# Added a docstring (between """)to have a help
# We can see the help of each method like this:
# help(cString.String.left)


class String:
    """Add a docstring here..."""
    created_object = 0

    def __init__(self, string):
        self.string = string
        self.length = len(string)

        String.created_object += 1

    def len(self):
        """Return the length of your String object instanciated
        
        String("This is Art").len() will display "11"
        """
        return self.length

    def left(self, length):
        """Return 'length' characters from the left

        String("This is Art").left(4) will display "This"
        """
        return self.string[:length]

    def right(self, length):
        """Return 'length' characters from the right
        
        String("This is Art").right(3) will display "Art"
        """
        return self.string[-length:]

    def mid(self, start, length=None):
        """Extract a string from the 'start' position with a length 
        If length is omitted, extract until the end of the string
        
        String("This is Art").mid(3,2) will display "is"
        """
        if length is None:
            length = self.length

        return self.string[start - 1:start - 1 + length]

    def reverse(self):
        """Reverse the string
        
        String("This is Art").reverse() will display "trA si sihT"
        """
        return self.string[::-1]


print(String("This is Art").left(4))

# print(right("This is Art", 3))  # Will display "Art"
print(String("This is Art").right(3))

# print(mid("Hello", 2))  # Will display "ello"
print(String("Hello").mid(2))

# print(mid("Hello", 2, 1))  # Will display "e"
print(String("Hello").mid(2, 1))
# or
test = String("This is Art")
print(test.left(4))
print(test.right(3))

test = String("Hello")
print(test.mid(2))
print(test.mid(2, 1))
print(test.len())
print(test.reverse())

# E:\Projects\cobol\EDITOR\purebasic\Canvas_Input_14.pb, line 408
# Using backspace at the 5th index
DATA_INPUT_INDEX = 5
INPUT_DATA = String("Welcome to my pleasure dome")

LEFT_DATA = INPUT_DATA.left(DATA_INPUT_INDEX)
RIGHT_DATA = INPUT_DATA.right(INPUT_DATA.len() - DATA_INPUT_INDEX - 1)

# Generate our new text
INPUT_DATA = LEFT_DATA + RIGHT_DATA

print(INPUT_DATA)

# How many object have been instanciated?
print('{} objects have been instanciated.'.format(String.created_object))
