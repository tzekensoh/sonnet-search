# Python program to read
# json file
 
import json
 
# Opening JSON file
f = open('sonnet_dict.json')
 
# returns JSON object as 
# a dictionary
sonnet_dict = json.load(f)
word_dict = {}
 
# Iterating the dictionary
for number in sonnet_dict.keys() :
    for word in sonnet_dict[number].split() :
        word = word.rstrip(',')
        word = word.rstrip('.')
        word = word.rstrip(';')
        word = word.rstrip("'s")
        word = word.lower()
        current_sonnets = word_dict.get(word)
        if current_sonnets == None :
            word_dict[word] = [number]
        else :
            if not (number in current_sonnets) :
                current_sonnets.append(number)

with open("word_dict.json", "w") as fp2 :
    json.dump(word_dict, fp2)
 
# Closing file
f.close()
