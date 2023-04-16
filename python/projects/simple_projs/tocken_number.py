from gtts import gTTS
from playsound import playsound
while True:
    token = int(input("Enter you token number: "))
    text = "ടോക്കൺ നമ്പർ {}".format(token)

    if (token == 404):
        ob2 = gTTS(
            "നന്ദി, ഇന്നത്തേ പരിശോദന അവസാനിചിരിക്കുന്നു... ബുക്കിങ്ങിനായി 79 94 54 13 13 എന്ന നമ്പറിൽ ബന്ദപെഡുക", lang="ml")
        ob2.save("close.mp3")
        playsound("close.mp3")
        quit()
    else:
        ob = gTTS(text, lang="ml")
        ob.save("token.mp3")
        playsound("token.mp3")
