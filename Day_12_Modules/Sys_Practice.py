import sys

# write to terminal, best practice to use flush() after write
# Without flush(), program may wait for further outputs before printing
# write strictly outputs given string (does not print new line character, etc.)
sys.stderr.write('test\n')
sys.stderr.flush()
sys.stderr.write('Hello')
sys.stderr.flush()

# Prints current directory and other info
print(sys.path)

# Prints input provided after program call
# Ex: Sys_Practice.py "Hello" -> prints('Sys_Practice.py', 'Hello') as a list
print(sys.argv)

# sys.argv creates a list allowing access at valid indexes
if len(sys.argv) > 1:
    print(sys.argv[1])
    print(float(sys.argv[1]) + 5)

# Create a function that adds all user input after directory
def main(arg):
    res = ""
    if len(arg) > 1:
        for i in arg:
            res += i
    return res

print(main(sys.argv))