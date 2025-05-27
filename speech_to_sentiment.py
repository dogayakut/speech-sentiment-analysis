from google.cloud import speech
from google.cloud import language_v1

def speech_to_text(speech_file):
    client = speech.SpeechClient()

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript

def analyze_sentiment(text):
    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={"document": document}).document_sentiment

    return sentiment.score, sentiment.magnitude

if __name__ == "__main__":
    audio_path = audio_path = input("Please enter the path of your audio file: ")

    text = speech_to_text(audio_path)
    print("Transcribed text:", text)

    score, magnitude = analyze_sentiment(text)
    print(f"Sentiment score: {score}, magnitude: {magnitude}")
    if score > 0.25:
    emotion = "Happy"
elif score < -0.25:
    emotion = "Sad"
else:
    emotion = "Neutral"

