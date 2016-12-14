colourList = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite2": "#ffefb", "AntiqueWhite3": "#cdc0b0",
              "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "azure2": "#e0eeee", "azure3": "#c1cdcd", "black": "#000000",
              "blue1": "#0000ff"}

userInput = input("Please enter a colour.")

if userInput in colourList:
    print("The colour code for {} is {:<8s}".format(userInput, colourList[userInput]))
else:
    print("Invalid code.")