# String Module
# Pour rechercher/remplacer, nous avons à notre disposition les
# méthodes count, find et replace

STRING_CASESENSITIVE = 0
STRING_NOCASE = 1


def mid(string, start, length=None):
    # If length omitted, extract until the end of the string
    if length is None:
        length = len(string)
    return string[start - 1:start - 1 + length]


def left(string, length):
    return string[:length]


def right(string, length):
    return string[-length:]


def reverse(string):
    return string[::-1]


def replace(string, to_find, replaced_by, mode=STRING_CASESENSITIVE):
    import re
    # String$ = ReplaceString(String$, StringToFind$, ReplacementString$ [, Mode [, StartPosition [, NbOccurrences]]])
    output_string = str()

    # Save in a list each positions founded in the string
    list_positions = []

    if mode is STRING_NOCASE:
        # Ignoring case sensitive
        list_positions = [m.start() for m in re.finditer(to_find, string, re.IGNORECASE)]
        output_string = re.compile(re.escape(to_find), re.IGNORECASE)
    else:
        # Case sensitive
        list_positions = [m.start() for m in re.finditer(to_find, string)]
        output_string = re.compile(re.escape(to_find))

    # Check
    # If list is still empty, we didn't find
    if not list_positions:
        return -1
    else:
        return output_string.sub(replaced_by, string)


print(left("This is Art", 4))  # Will display "This"

print(right("This is Art", 3))  # Will display "Art"

print(mid("Hello", 2))  # Will display "ello"
print(mid("Hello", 2, 1))  # Will display "e"

print(reverse("Hello"))  # Will display "elleH"

# E:\Projects\cobol\EDITOR\purebasic\Canvas_Input_14.pb, line 408
# Using backspace at the 5th index
DATA_INPUT_INDEX = 5
INPUT_DATA = "Welcome to my pleasure dome"
LEFT_DATA = left(INPUT_DATA, DATA_INPUT_INDEX)
RIGHT_DATA = right(INPUT_DATA, len(INPUT_DATA) - DATA_INPUT_INDEX - 1)
# Generate our new text
INPUT_DATA = LEFT_DATA + RIGHT_DATA

print(INPUT_DATA)

# Will display -1
print(replace("Hello again, hello again", "HELLO", "oh no..."))

# Will display "Hello again, oh no... again"
print(replace("Hello again, hello again", "hello", "oh no..."))

# Will display "oh no..., oh no... again"
print(replace("Hello again, hello again", "hello", "oh no...", STRING_NOCASE))

# ll = "Hello again, hello again"
# for down_to in ll[::-1]:
#     print(down_to)
