#output sys

MORSE_ALPHABET = {"a": "·−", "b": "−···", "c": "−·−·", "d": "−··",
                  "e": "·", "f": "··−·", "g": "−−·", "h": "····",
                  "i": "··", "j": "·−−−", "k": "−·−", "l": "·−··",
                  "m": "−−", "n": "−·", "o": "−−−", "p": "·−−·",
                  "q": "−−·−", "r": "·−·", "s": "···", "t": "−",
                  "u": "··−", "v": "···−", "w": "·−−", "x": "−··−",
                  "y": "−·−−", "z": "−−··", "1": "·−−−−", "2": "··−−−",
                  "3": "···−−", "4": "····−", "5": "·····", "6": "−····",
                  "7": "−−···", "8": "−−−··", "9": "−−−−·", "0": "−−−−−",
                  "-": "-....-"}

def string2morse(string):
    output = ""

    while " " * 2 in string:
        string = string.replace((" " * 2), " ")
    for char in string.lower().strip():
        if char == " ":
            output += (" ")
            continue
        if char == ".":
        	output += (" ")
        	continue
        else:
            output += MORSE_ALPHABET.get(char, "") + " "
    return output.strip()


def morse2string(morse_code):
    output = ""
    morse_code = \
    morse_code.replace(".", "·").replace("-", "−").replace("_", "−")

    morse = {v: k for k, v in MORSE_ALPHABET.items()}
    for word in morse_code.split(" " * 2):
        for letter in word.split(" "):
            output += morse.get(letter, "")
        output += " "

    return output.strip()


#f = open('testing.txt')

print("FYI: Input for type has to be following:\n 1. UTF-8\n 2. UTF-32\n 3. Baudot code\n 4. Morse code\n")
namefile = input("Enter file name with .txt:")
fo = open(namefile, 'r') 
line = fo.readline()
myfile = open('output1.txt', 'w')

typein = input("Converting from type? ")
typeout = input("Converting to type? ")
if ((typein == "UTF-8") and (typeout == "Morse code")):
	while line:
		#print(line)
		myfile.write(string2morse)
		#print(string2morse(line))
elif ((typein == "UTF-8") and (typeout == "UTF-32")):
	while line: 
		newline = line.encode(encoding='UTF-32', errors = 'strict')
		myfile.write(newline)
elif ((typein == "Morse code") and (typeout == "UTF-8")):
	while line:
		#print(line)
		myfile.write(morse2string)
		#print(morse2string(line))
fo.close()