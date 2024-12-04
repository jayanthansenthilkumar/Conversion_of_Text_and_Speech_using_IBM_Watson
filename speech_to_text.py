import api
tts_authenticator = api.IAMAuthenticator(api.TTS_API_KEY)
text_to_speech = api.TextToSpeechV1(authenticator=tts_authenticator)
text_to_speech.set_service_url(api.TTS_SERVICE_URL)
text = "Hello Everyone! This is a text-to-speech service offered by IBM Watson. I hope you are enjoying this and learning a lot from it."
with open('output.mp3', 'wb') as audio_file:
    response = text_to_speech.synthesize(text,voice='en-US_AllisonV3Voice',accept='audio/mp3').get_result()
    audio_file.write(response.content)
print("Audio file created successfully with the name 'output.mp3'")