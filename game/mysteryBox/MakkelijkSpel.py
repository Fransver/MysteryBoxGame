


#=============
codeSpel = [3,2,4,1]

ingevoerdeCode = []


#=============


def makkelijk_spel():
    game = True
    while game:
        inputNumber = int(input("Raad de 4 cijferige code"))

        if (inputNumber == codeSpel[0] or
            inputNumber == codeSpel[1] or
            inputNumber == codeSpel[2] or
                inputNumber == codeSpel[3]):
            ingevoerdeCode.append(inputNumber)

            for i in range(len(ingevoerdeCode)):
                print("Goed geraden, je hebt code nummer " + str(ingevoerdeCode) + " Geraden, die zit in de code !!")
                game = True

        elif(inputNumber != codeSpel):
            print("Probeer het nog een keer")
            game = True

        elif (inputNumber[0:3] == codeSpel):
            print("PROFICIAT")


if __name__ == "__main__":
    makkelijk_spel()