from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def speak_text(text, lang="en"):
    """Convert AI text reply to speech and play it."""
    if not text.strip():
        return
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")
    audio = AudioSegment.from_mp3("response.mp3")
    play(audio)
    os.remove("response.mp3")
