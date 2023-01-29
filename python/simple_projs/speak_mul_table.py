import pyttsx3
print("=====> speak multiplication table <=======")

n = 0


try:
    n = int(input("Enter a number between(1-10): "))
    if n > 10:
        raise Exception("Value must be between(1-10).")

except Exception as error:
    print(error)


names = {
    "1": "ones",
    "2": "twos",
    "3": "threes",
    "4": "fours",
    "5": "fives",
    "6": "sixes",
    "7": "sevens",
    "8": "eights",
    "9": "nines",
    "10": "tens"
}


text = "{} {} are {}"
wholeText = ""

for i in range(1, 11):
    output = text.format(i, names[str(n)], n*i)
    wholeText += output+"\n\n"
    print(output)
engine = pyttsx3.init()
engine.say(wholeText)
engine.runAndWait()
