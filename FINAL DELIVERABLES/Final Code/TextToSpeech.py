from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('1qKT8ieAGOm3nFmtF7w86OrE1GaOSQzRGlsWfKdVMokq')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/e53089eb-3654-4d71-a64e-08fe95adf5b0')

with open('medicine.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello John its time to take your medicine',
            voice='en-US_LisaV3Voice',
            accept='audio/mp3'        
        ).get_result().content)
