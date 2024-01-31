import speech_recognition as sr
from textblob import TextBlob

def process_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        # Use Google's Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

        # Perform sentiment analysis using TextBlob
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        # Output sentiment analysis result
        if sentiment > 0:
            print("Positive sentiment!")
        elif sentiment < 0:
            print("Negative sentiment!")
        else:
            print("Neutral sentiment.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"Error connecting to the Google API: {e}")

if __name__ == "__main__":
    process_speech()

