import sys

os_to_check = sys.platform.lower()

if os_to_check.startswith('win32'):
    from msvcrt import getch
elif os_to_check.startswith('linux'):
    import sys, tty, termios
elif os_to_check.startswith('darwin'):
    import carbon


