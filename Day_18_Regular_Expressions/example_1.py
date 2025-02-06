import re

# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

para_updated = re.sub(r"[^\w\s]", "", paragraph, re.I)
para_split = re.split(" ", para_updated)
unique_words = set(para_split)
print(unique_words)

result = []
for word in unique_words:
    matches = re.findall(rf"\b{word}\b", paragraph)
    result.append((len(matches), word))
    
result.sort()
result.reverse()
print(f"{result}\n")

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
# Extract these numbers from this whole text and find the distance between the two furthest particles.
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

regex_pattern = r'-?\d+'
nums = re.findall(regex_pattern, txt, re.I)
nums = [int(x) for x in nums]
nums.sort()
print("The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.\nExtract these numbers from this whole text and find the distance between the two furthest particles.")
print(nums)
max_diff = int(nums[-1]) - int(nums[0])
print(max_diff)
