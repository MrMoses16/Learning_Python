import re

# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_txt(str):
    return re.sub(r"[^A-Z|a-z|\s]", "", sentence)

def most_freq_words(str):
    str_split = re.split(" ", str)
    unique_words = set(str_split)
    print(unique_words)
    freq = []
    for word in unique_words:
        matches = re.findall(rf'\b{word}\b', str, re.I)
        freq.append((len(matches), word))
    
    freq.sort()
    freq.reverse()

    print(freq[0:3])

print(most_freq_words(clean_txt(sentence)))
