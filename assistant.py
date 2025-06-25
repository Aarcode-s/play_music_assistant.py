import speech_recognition as st
import pyttsx3
import pywhatkit  # For playing the top YouTube result
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speaking speed

# Function to make the assistant speak
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen for a voice command
def listen(): 
    recognizer = st.Recognizer()
    with st.Microphone(device_index=9) as source:  # Change device_index if needed
        
        time.sleep(1)  # Brief pause before listening
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("Master, give your command.")

        try:
            # Listen for the command with a timeout
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except st.WaitTimeoutError:
            speak("Listening timed out. Please try again.")
            return ""

        # try:
        #     # Save audio for testing/debugging (optional)
        #     with open("test_audio.wav", "wb") as f:
        #         f.write(audio.get_wav_data())

            # Convert speech to text
        try:
            command = recognizer.recognize_google(audio)
            print(f"Master, your command is: {command}")
            return command.lower()
        except st.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except st.RequestError:
            speak("Speech service error.")
            return ""

# Function to activate and respond to the song command
def activate_assistant():
    speak("Hello Master, what do you want to listen to?")
    song = listen()
    if song:
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)  # Play top YouTube result automatically
    else:
        speak("No song detected. Please try again.")

# Main loop to wait for the wake word
def main():
    speak("Say 'activate' to start the assistant.")
    while True:
        audio_text = listen()
        if "activate" in audio_text:
            activate_assistant()
            break # Exit after one activation

# Run the assistant
if __name__ == "__main__":
    main()
