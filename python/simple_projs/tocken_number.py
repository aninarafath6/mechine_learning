from gtts import gTTS
from playsound import playsound
while True:
    token = int(input("Enter you token number: "))
    text = "ടോക്കൺ നമ്പർ {}".format(token)

    if (token == 404):
        ob2 = gTTS(
            "നന്ദി, ഇന്നത്തേ പരിശോദന അവസാനിചിരിക്കുന്നു... ബുക്കിങ്ങിനായി 62 8 20 62 52 7 എന്ന നമ്പറിൽ ബന്ദപെഡുക", lang="ml")
        ob2.save("close.mp3")
        playsound("close.mp3")
        quit()
    else:
        ob = gTTS(text, lang="ml")
        ob.save("token.mp3")
        playsound("token.mp3")
