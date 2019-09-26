import sys
import binascii

MORSE_ALPHABET = {"a": "·−", "b": "−···", "c": "−·−·", "d": "−··",
                  "e": "·", "f": "··−·", "g": "−−·", "h": "····",
                  "i": "··", "j": "·−−−", "k": "−·−", "l": "·−··",
                  "m": "−−", "n": "−·", "o": "−−−", "p": "·−−·",
                  "q": "−−·−", "r": "·−·", "s": "···", "t": "−",
                  "u": "··−", "v": "···−", "w": "·−−", "x": "−··−",
                  "y": "−·−−", "z": "−−··", "1": "·−−−−", "2": "··−−−",
                  "3": "···−−", "4": "····−", "5": "·····", "6": "−····",
                  "7": "−−···", "8": "−−−··", "9": "−−−−·", "0": "−−−−−",
                  ".": "·−·−·−"}

def string2morse(string):
    output = ""
    while " " * 2 in string:
        string = string.replace((" " * 2), " ")
    for char in string.lower().strip():
        if char == " ":
            output += (" ")
            continue
        else:
            if("·−·−·−" == MORSE_ALPHABET.get(char,"")):
              output += MORSE_ALPHABET.get(char, "") + " "
              output += (" ")
            else:
              output += MORSE_ALPHABET.get(char, "") + " "
    return output.strip()


def morse2string(morse_code):
    output = ""
    morse_code = \
    morse_code.replace(".", "·").replace("-", "−").replace("_", "−")

    morse = {v: k for k, v in MORSE_ALPHABET.items()}
    for word in morse_code.split(" "):
      for letter in word.split(" "):
        output += morse.get(letter, "")
      output += " "
    new = output.split(" " *2)
    for each in range(len(new)):
      new[each] = new[each].replace(" ", "")
    space = " "
    space = space.join(new)  
    return space


#f = open('testing.txt')
if __name__ == '__main__':
  print("FYI: Input for type has to be following:\n 1. UTF-8\n 2. UTF-32\n 3. Baudot code\n 4. Morse code\n")
  namefile = input("Enter file name with .txt: ") 
  
  typein = input("Converting from type? ")
  typeout = input("Converting to type? ")
  inputstring = ""
  fo = open(namefile, 'r')

  if(typein == "Morse code"):
    for line in fo:
      inputstring += morse2string(line)

  if(typein == "UTF-32"):
    fo = open(namefile, 'rb')
    for line in fo:
      inputstring += line.decode(encoding='UTF-8', errors = 'ignore')

  #if(typein == "Baudot code"):

  else: 
    for line in fo: 
      inputstring += line

  myfile = open('output.txt', 'w')
  if(typeout == "Morse code"):
    myfile.write(string2morse(inputstring))

  if(typeout == "UTF-32"):
    myfile = open('output.txt','wb')
    myfile.write(inputstring.encode(encoding='UTF-32', errors = 'ignore'))    

  if(typeout == "Baudot code"):
    myfile = open('output.txt', 'w')
    myfile.write(binascii.a2b_uu(inputstring))
  else: 
    myfile.write(inputstring)
  # if ((typein == "UTF-8") and (typeout == "Morse code")):
  #   fo = open(namefile, 'r')
  #   myfile = open('utf8_to_morse_output.txt', 'w')
  #   for line in fo:
  #     myfile.write(string2morse(line))

  # if ((typein == "Morse code") and (typeout == "UTF-8")):
  #   fo = open(namefile, 'r')
  #   myfile = open('morse_to_utf8_output.txt', 'w')
  #   for line in fo:
  #     myfile.write(morse2string(line))

  # if ((typein == "UTF-8") and (typeout == "UTF-32")):
  #   fo = open(namefile, 'r')
  #   myfile = open('utf8_to_utf32_output.txt', 'wb')
  #   for line in fo: 
  #     myfile.write(line.encode(encoding='UTF-32', errors = 'ignore'))

  # if ((typein == "UTF-32") and (typeout == "UTF-8")):
  #   fo = open(namefile, 'rb')
  #   myfile = open('utf32_to_utf8_output.txt', 'w')
  #   for line in fo:
  #     myfile.write(line.decode(encoding='UTF-8', errors = 'ignore'))    
      
  # if ((typein == "Morse code") and (typeout == "UTF-32")):
  #   fo = open(namefile, 'r')
  #   myfile = open('morse_to_utf32_output.txt', 'wb')

  fo.close()