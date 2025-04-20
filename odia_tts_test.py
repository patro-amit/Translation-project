import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/shyampatro/Translation projectt/models/facebook/nllb-200-distilled-600M/service_account.json"

from google.cloud import texttospeech
client = texttospeech.TextToSpeechClient()
synthesis_input = texttospeech.SynthesisInput(text="ନମସ୍କାର, ଏହା ଓଡ଼ିଆ ଭାଷାରେ ଏକ ପରୀକ୍ଷା ଅଟୋମେସନ୍")
voice = texttospeech.VoiceSelectionParams(language_code="or-IN", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
with open("odia_test.mp3", "wb") as out:
    out.write(response.audio_content)
print("Audio content written to file 'odia_test.mp3'")