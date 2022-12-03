#Inspired by @achrafcodes on Instagram
#Made by Amaryne B. (a.k.a. TasDeNeige), 12/11/2022, updated on 03/12/2022

from time import sleep
Restart = True

while Restart == True:
    def print_but_cool(sentence):
        sentence = sentence.lower() #Prevent the program from not finding an uppercase character

        #---------- DEFINE ALPHABET ----------#
        alphabet = []
        numASCIIlettre = 97
        alphabet.append(" ") #Adds the 'space' character to the list
        alphabet.append(".")

        for i in range(26):
            alphabet.append(chr(numASCIIlettre + i))

        #---------- CREATE SENTENCE ----------#
        letter = ""
        newSentence = ""
        numLetter = -1 #Used to go through the alphabet list, -1 to not get out of range

        for i in range(len(sentence)):
            while letter != sentence[i]:

                if numLetter == 26:
                    letter = "*" #Replace an unknown character
                    break

                else:
                    numLetter += 1
                    letter = alphabet[numLetter]
                    print(newSentence + letter)
                    sleep(0.05) #Gives this cool effect of printing

            newSentence += letter
            numLetter = -1 #Goes back to the beginning of the list


    print_but_cool(str(input("What do you want to print? -> ")))
    print("\n")
    Again = str(input("Print something else? (Y/N) -> ")).lower()

    if Again == "n" or Again == "no":
        Restart = False

print("Goodbye! Hope you had fun!")
sleep(2)
