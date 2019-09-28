import sys

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

BAUDOT_LETTER = {"": "00000000", "T": "00000001", "\r": "00000010", "O": "00000011", " ": "00000100",
         "H": "00000101", "N": "00000110", "M": "00000111", "\n": "00001000", "L": "00001001",
         "R": "00001010", "G": "00001011", "I": "00001100", "P": "00001101", "C": "00001110",
         "V": "00001111", "E": "00010000", "Z": "00010001", "D": "00010010", "B": "00010011",
         "S": "00010100", "Y": "00010101", "F": "00010110", "X": "00010111", "A": "00011000",
         "W": "00011001", "J": "00011010", "U": "00011100", "Q": "00011101", "K": "00011110" }

BAUDOT_FIGURE = {"": "00000000", "5": "00000001", "\r": "00000010", "9": "00000011", " ": "00000100",
         "": "00000101", ",": "00000110", ".": "00000111", "\n": "00001000", ")": "00001001",
         "4": "00001010", "&": "00001011", "8": "00001100", "0": "00001101", ":": "00001110",
         ";": "00001111", "3": "00010000", "\"": "00010001", "$": "00010010", "?": "00010011",
         "\a": "00010100", "6": "00010101", "!": "00010110", "/": "00010111", "-": "00011000",
         "2": "00011001", "\'": "00011010", "7": "00011100", "1": "00011101", "(": "00011110" }
SPECIAL_CASE = ["", "\r"," ","\n"]

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
    #morse_code = \
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

def string2baudot (string):
  output = ""
  previous = ""
  for char in string.upper():
    if not previous:
      temp = BAUDOT_LETTER.get(char, "")
      if char in SPECIAL_CASE:
        output += temp
      if not temp:
        output += "00011011" + BAUDOT_FIGURE.get(char, "")
      else:
        output += "00011111" + temp
    else:
      temp = BAUDOT_LETTER.get(char, "")
      check = BAUDOT_LETTER.get(previous, "")
      if char in SPECIAL_CASE:
        output += temp
      elif not check:
        if not temp:
          output += BAUDOT_FIGURE.get(char, "")
        else:
          output += "00011111" + temp
      else:
        if not temp:
          output += "00011011" + BAUDOT_FIGURE.get(char, "")
        else:
          output += temp
    if char not in SPECIAL_CASE:
      previous = char 
  return output

def baudot2string(baudot_code):
  output = ""
  convert = [baudot_code[i:i+8] for i in range(0, len(baudot_code), 8)]
  letter = {v: k for k, v in BAUDOT_LETTER.items()}
  figure = {x: y for y, x in BAUDOT_FIGURE.items()}
  check = "default"
  for i in range(len(convert)):
    if(convert[i] == "00011011"):
      check = "figure"
    elif (convert[i] == "00011111"):
      check = "letter"
    else:
      if(check == "figure"):
        output += figure.get(convert[i], "")
      else:
        output += letter.get(convert[i], "")
  return output


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

  elif(typein == "UTF-32"):
    fo = open(namefile, 'rb')
    for line in fo:
      inputstring += line.decode(encoding='UTF-8', errors = 'strict')

  elif(typein == "Baudot code"):
    for line in fo:
      inputstring += baudot2string(line)

  else: 
    for line in fo: 
      inputstring += line

  myfile = open('output1.txt', 'w')

  if(typeout == "Morse code"):
    myfile.write(string2morse(inputstring))

  elif(typeout == "UTF-32"):
    myfile = open('output.txt','wb')
    myfile.write(inputstring.encode(encoding='UTF-32', errors = 'ignore'))    

  elif(typeout == "Baudot code"):
    myfile = open('output.txt', 'w')
    myfile.write(string2baudot(inputstring))
  else: 
    myfile.write(inputstring)
  
  fo.close()