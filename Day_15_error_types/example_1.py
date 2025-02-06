# Examples and types of errors

def Syntax():
    return "A SyntaxError occurs when the code has improper syntax.\nExample: print \'syntax error'\\nResults in: SyntaxError: Missing parentheses in call to \'print\'. Did you mean print(\'sytax error\')\n"

def Name():
    return "A NameError occurs when the code uses a variable not defined.\nFor example: print(age).\nNameError: name \'age\' is not defined\n"

def Index():
    return "An IndexError occurs when the code tries to access an array outside of its range.\nFor example, if an array has a length of 5, trying to access indexes greater than 4 would result in an IndexError.\nAdditionally, trying to access negative indexes will result in an IndexError.\nError looks like: IndexError: list index out of range\n"

def ModuleNotFound():
    return "A ModuleNotFoundError occurs when the code tries to import a module spelt incorrently.\nFor example: import maths.\nModuleNotFoundError: No module named \'maths\'\n"

def Attribute():
    return "An AttributeError occurs when the code tries to access a function that does not exist in the module imported.\nFor example: import math --- math.pi.\nAttributeError: module \'math\' has no attribute \'PI\'.\n"

def Key():
    return "An KeyError occurs when the code tries to access a dictionary value but the key is misspelt.\nFor example: users = {\'name\':\'Kris\', \'age\':250, \'country\':'USA'}, users[\'county\'].\nKeyError: \'county\'\n"

def Type():
    return "A TypeError occurs when two different data types are operated on each other (add, subtract, etc.)\nFor example: 4 + \'3\'.\nTypeError: unsupported operand type(s) for +: \'int\' and \'str\'\n"

def Import():
    return "A ImportError occurs when the code tries to access a non-existing function from a module. For example: from math import power.\nImportError: cannot import name 'power' from \'math\'\n"

def Value():
    return "A ValueError occurs when the code tries to convert one data type to another but fails as the data does not fit the requirements of the convertion.\nFor example: int(\'12a\').\nValueError: invalid literal for int() with base 10: \'12a\'\n"

def ZeroDivision():
    return "A ZeroDivisionError occurs when the code tries divide a number by zero.\nFor example: 15 / 0.\nZeroDivisionError: division by zero\n"

def default():
    return "Type of error does not exist. Type in a valid error\n"

# switch statement
switch = {
    "Syntax" : Syntax,
    "Name" : Name,
    "Index" : Index,
    "ModuleNotFound" : ModuleNotFound,
    "Attribute" : Attribute,
    "Key" : Key,
    "Type" : Type,
    "Import" : Import,
    "Value" : Value,
    "ZeroDivision" : ZeroDivision
}

flag = True

while flag:
    print("\nWhich type of error would you like to know more about:\nSyntax, Name, Index, ModuleNotFound, Attribute, Key, Type, Import, Value, ZeroDivision\nTo exist type \'stop\'\n")

    key = input()
    if key == "stop":
        flag = False
        break

    result = switch.get(key, default)()
    print(result)