import json

# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
def count_lines_and_words(file_name):
    with open(file_name) as f:
        lines = f.readlines()

        words = 0
        for line in lines:
            new_line = line.split()
            words += len(new_line)

        print(f'The file \"{file_name}\" contains {len(lines)} line(s) and {words} word(s).')

count_lines_and_words('obama_speech.txt')
count_lines_and_words('michelle_obama_speech.txt')

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_lang(file_name, num):
    with open(file_name, 'r', encoding='utf-8') as f:
        country_info = json.load(f)

        language_freq = {}
        for country in country_info:
            language = country['languages']
            
            for lang in language:
                if lang not in language_freq:
                    language_freq.update({lang: 1})
                else:
                    language_freq.update({lang: language_freq.get(lang) + 1})

        language_freq = {key: val for key, val in sorted(language_freq.items(), key = lambda ele: ele[1], reverse=True)}
        
        res = {}
        index = 0
        for key in language_freq:
            if index < num:
                res.update({key: language_freq.get(key)})
                index += 1
            else:
                break

        return res
    
print(most_spoken_lang('countries_data.json', 10))

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(file_name, num):
    with open(file_name, 'r', encoding='utf-8') as f:
        country_info = json.load(f)

        country_population = {}
        for country in country_info:
            population = country['population']
            
            
            country_population.update({country['name']: population})
                

        country_population = {key: val for key, val in sorted(country_population.items(), key = lambda ele: ele[1], reverse=True)}
        
        res = {}
        index = 0
        for key in country_population:
            if index < num:
                res.update({key: country_population.get(key)})
                index += 1
            else:
                break

        return res
    
print(most_populated_countries('countries_data.json', 10))