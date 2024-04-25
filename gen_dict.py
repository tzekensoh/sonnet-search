import json

# Generate Sonnet Number to Text Dictionary
sonnet_dict = {}
current_number = "I."
current_text = ""
isBeginningOfSonnet = True
 
with open("sonnets.txt") as fp:
    while True:
        line = fp.readline()

        if isBeginningOfSonnet :
            current_number = line.strip()[:-1]
            if current_number.startswith("EOF") :
                break
            line = fp.readline() # skip the next blank line
            line = fp.readline() # read first line of sonnet
            current_text = line
            isBeginningOfSonnet = False
        else :
            current_text = current_text + line
        if not (line.strip()) : # this is the last blank line of the sonnet
            # add current_number -> current text
            sonnet_dict[current_number] = current_text
            isBeginningOfSonnet = True    

with open("sonnet_dict.json", "w") as fp2 :
    json.dump(sonnet_dict, fp2)
