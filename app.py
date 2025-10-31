import streamlit as st
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
from voice_utils.speech_to_text import transcribe_audio
from voice_utils.text_to_speech import speak_text
from voice_utils.ai_reply import generate_ai_reply

st.set_page_config(page_title="AI Voice Assistant", page_icon="🎙️", layout="wide")

st.title("🎤 AI Voice Assistant — Whisper (Groq) + LLaMA + TTS")
st.markdown("""
Record your voice → Transcribe via **Whisper (Groq)** →  
Get a **Groq LLaMA** AI reply → Hear it with **Text-to-Speech** 🔊
""")

# Recording section
duration = st.slider("🎙️ Recording Duration (seconds):", 3, 15, 5)
record_btn = st.button("🎧 Record Now")

if record_btn:
    st.info("Recording... please speak clearly.")
    fs = 44100
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    st.success("✅ Recording complete!")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        wav.write(tmpfile.name, fs, audio)
        st.audio(tmpfile.name, format="audio/wav")

        # Transcription
        st.write("🧠 Transcribing via Groq Whisper...")
        text = transcribe_audio(tmpfile.name)
        st.success(f"**You said:** {text}")

        # AI response
        st.write("🤖 Thinking...")
        ai_reply = generate_ai_reply(text)
        st.subheader(f"**AI Reply:** {ai_reply}")

        # TTS playback
        st.write("🔊 Speaking response...")
        speak_text(ai_reply)
