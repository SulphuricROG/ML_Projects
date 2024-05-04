import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# List available microphones
microphone_list = sr.Microphone.list_microphone_names()
print("Available microphones:")
for i, microphone_name in enumerate(microphone_list):
    print(f"{i+1}. {microphone_name}")

# Select a microphone by its index
mic_index = 1  # Change this index based on the desired microphone
selected_microphone_name = microphone_list[mic_index]

# Use the selected microphone as the audio source
with sr.Microphone(device_index=mic_index) as source:
    print(f"Using microphone: {selected_microphone_name}")

    print("Say something:")
    audio = recognizer.listen(source)

# Recognize speech using Google Speech Recognition
try:
    print("You said:", recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
