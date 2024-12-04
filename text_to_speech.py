import api
stt_authenticator = api.IAMAuthenticator(api.STT_API_KEY)
speech_to_text = api.SpeechToTextV1(authenticator=stt_authenticator)
speech_to_text.set_service_url(api.STT_SERVICE_URL)
audio='output.mp3'
with open(audio, 'rb') as audio_file:
    response = speech_to_text.recognize(audio=audio_file,content_type='audio/mp3',model='en-US_BroadbandModel').get_result()
transcription = response['results'][0]['alternatives'][0]['transcript']
print("Transcription:", transcription)