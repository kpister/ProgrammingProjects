import urllib2
import urllib

def strip(string):
    meat = False
    newString = ""
    for letter in string:
        if letter.isalnum():
            meat = True
        if meat:
            newString = letter + newString

    string = newString
    newString = ""
    meat = False
    for letter in string:
        if letter.isalnum() or letter == "\"":
            meat = True
        if meat:
            newString = letter + newString

    return newString

def learn(word):
    word = urllib.quote_plus(word)
    response = urllib2.urlopen("http://etymonline.com/index.php?allowed_in_frame=0&search=" + word)
    text = response.read()

    start = text.find("<dl")
    end = text.find("</dd>")

    text = text[start:end]

    newText = ""

    deleting = 0
    ending = False
    for index in range(0, len(text)):
        letter = text[index]

        if ending and letter.isupper():
            break
        
        if letter == "<" or letter == "(":
            deleting += 1

        if deleting == 0:
            if letter == ".":
                ending = True
            elif ord(letter) > 95:
                ending = False
            try:
                if letter == " " and text[index+1] == "(":
                    nothing = 0
                elif letter == "," and text[index+1] == "\"":
                    nothing = 0
                else:
                    if letter == "*":
                        newText += " "
                    newText += letter
            except:
                break

        if letter == ">" or letter == ")":
            deleting -= 1

    text = newText
    quotes = 0
    origins = []

    index = text.find("from")
    if index != -1:
        origins.append(text[0:index])
        text = text[index:]
    index = text.find("from")
    while index != -1:
        for letter in range(0, len(text)):
            if text[letter] == "\"":
                if quotes == 1:
                    if text[letter-1] == ",":
                        origins.append(text[index:letter-1]+"\"")
                    else:
                        origins.append(text[index:letter+1])
                    text = text[letter+1:]
                    quotes = -1
                    break
                else:
                    quotes = 1

        if index != -1:
            index2 = text.find("from", index+3)
            if index2 != -1:
                origins.append(text[index:index2])
                text = text[index2:]
                index = index2
            else:
                origins.append(text)
                break
        quotes = 0
        index = text.find("from")
        
    for item in range(0, len(origins)):
        origins[item] = strip(origins[item])
        if origins[item] == "":
            origins.pop(item)
            item -= 1
        else:
            print origins[item]
            

user = ""
while user != "Exit":
    user = raw_input("Enter a word to learn more! (Exit to quit): ")
    learn(user)
