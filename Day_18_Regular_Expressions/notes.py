import re

# Regular Expression (RegEx) is a special text string that helps find patterns in data
# Ex: re.match() searches the first line
txt = "I love waffles for breakfast"
match = re.match("I love waffles", txt, re.I)
print(f"The result of using match for the string of \'{txt}\' and substring \'I love waffles\' returns:\n{match}\n")

span = match.span()
print(f"The span of the match is: {span}")
start, end = span

# Ex: re.search() searches all line
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search("programming", txt, re.I)
print(f"The result of using search for the string of \'{txt}\' and substring \breakfast\' returns:\n{match}\n")

span = match.span()
print(f"The span of the match is: {span}")
start, end = span

# Ex: re.findall() returns all matches as a list
matches = re.findall("language", txt, re.I)
print(f"The result of using findall for the string of \'{txt}\' and substring \language\' returns:\n{matches}\n")

# Note re.I includes both upper and lower case whening finding a pattern
# If you do not want to include re.I, you can do r"substring" or r"[Ss]ubstring" or structure your search as follows:
matches = re.findall("Python|python", txt)
matches = re.findall("[Pp]ython", txt)

# You can replace a substring within a string by using re.sub()
match_replaced = re.sub("Python", "Java", txt, re.I)
print(f"Using re.sub() allows the user to change a substring within a string:\n->{txt}\n->{match_replaced}")


# You can split text using re.split()
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
txt_updated = re.split("\n", txt)
print(f"Using re.split allows the user to split text:\n->{txt}\n->{txt}")
