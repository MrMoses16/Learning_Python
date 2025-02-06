from random import randint

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    new_list = lst.copy()
    res = []

    for i in range(len(lst)):
        index = randint(0, len(new_list) - 1)
        res.append(new_list[index])
        new_list.pop(index)
    
    return res

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_unique_numbers():
    valid_nums = []
    res = []

    for i in range(10):
        valid_nums.append(i)

    for i in range(7):
        index = randint(0, len(valid_nums) - 1)
        res.append(valid_nums[index])
        valid_nums.pop(index)
    
    return res
