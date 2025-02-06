# Opening file Syntax
# open('filename', mode) -> mode(r, a, w, x, t, b)
# r -> read; Opens the file for reading, it returns an error if the file does not exist
# a -> append; Opens the file for appending, creates the file if it does not exist; adds onto the end of the file
# w -> write; Opens the file for writing, creates the file if it does not exist; overwrites existing content
# x -> create; Creates the specified file, returns an error if the file exist
# t -> text; Text mode
# b -> binary; Binary mode (images)

# the default mode for open is reading

# read() -> reads the whole text as a string, can specify number of character read by read(number)
# readline() -> reads only the first line
# readlines() -> reads text line by line and returns a list of lines (includes \n, etc.)
# all must be closed after used: f.read() -> f.close()

# splitlines() -> another method to get each line into a list (does not include \n, etc.)
# f.read().splitlines()

# can also open a file with the following format (closes file for you)
# with open("file.txt") as f:
#     txt = f.read().splitlines()

# deleting files
# import os
# if os.path.exists("file.txt"):
#     os.remove("file.txt")
# else:
#     print("File does not exist")

# changing JSON to dictionary
# import json module and use 'loads' method
# import json
# person_json = '''{
#     "name": "Kris",
#     "country": "USA",
#     "city": "Orlando",
#     "skills": ["Java", "C", "Python"]
# }'''
# # change json to dictionary
# person_dct = json.loads(person_json)

# changing dictionary to JSON
# import json module and use 'dumps' method
# person_json = json.dumps(person_dct)

# Saving JSON file
# we use encoding and indentation to make the json file easy to read
# with open('file_name.json', 'w', encoding = 'utf-8') as f:
#     json.dumps(person_dct, f, ensure_ascii = False, indent = 4)

# File with CSV (Comma Seperated Values)
# import csv
# with open('file_name.cvs') as f:
#     cvs_reader = csv.reader(f, delimiter=',')

# File with Excel (need to install xlrd)
# import xlrd
# excel_book = xlrd.open_workbook('file_name.xls')


