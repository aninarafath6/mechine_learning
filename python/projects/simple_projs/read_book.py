import io
from gtts import gTTS
from playsound import playsound


fp = io.open("book.text", mode="r", encoding="utf-8")
book_content = fp.read()
data = gTTS(book_content, lang="ml")
data.save("book.mp3")
playsound("book.mp3")
