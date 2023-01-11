#needed pip installs
#pip install azure-cognitiveservices-speech
#pip install requests
#these are the only two project specific installs I made it is possible you might need uuid or json. I already ahd those as well as
#several other python packages.
#calling main should run everything. I am in pycharm. Google colab might struggle with this code due to microphone access.

import azure.cognitiveservices.speech as speechsdk
import requests, uuid, json
import PySimpleGUI as sg

def from_mic(source):
    text = "This is where your text will appear to verify it is good"
    layout = [[sg.Text('Speak into the Mic', size=(20, 1), font='Lucida', justification='left')],
              [sg.Text('If you do not like the output you can edit it, or restart the application', size=(12, 1), font='Lucida', justification='left')],
              [sg.Multiline(size=(90,20),
                           background_color='white',
                           text_color='black',
                           reroute_stdout=True,
                           reroute_stderr=True)],
              [sg.Button('SAVE', font=('Times New Roman', 12))]]
    speech_config = speechsdk.SpeechConfig(subscription="94d4c73e70fa4ae1821d98160e5b6009", region="westus")
    speech_config.speech_recognition_language = source
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    while True:
        window = sg.Window("Speech to Text", layout, finalize = True)
        result = speech_recognizer.recognize_once_async().get()
        print(result.text)
        event, values = window.read()
        if event == "SAVE" or event == sg.WIN_CLOSED:
            break

    return values[0]

def getCodes(languageName, gender):
    if (languageName == 'English'):
        if(gender == "Male"):
            return "en", "en-US", "en-US-BrandonNeural"
        elif(gender == "Female"):
            return "en", "en-US", "en-US-MonicaNeural"
    if (languageName == 'Spanish'):
        if (gender == "Male"):
            return "es", "es-ES", "es-ES-DarioNeural"
        elif (gender == "Female"):
            return "es", "es-VE", "es-VE-PaolaNeural"
    if (languageName == 'Polish'):
        if (gender == "Male"):
            return "pl", "pl-PL", "pl-PL-MarekNeural"
        elif (gender == "Female"):
            return "pl", "pl-PL", "pl-PL-ZofiaNeural"
    if (languageName == 'Dutch'):
        if (gender == "Male"):
            return "nl", "nl-NL", "nl-NL-MaartenNeural"
        if (gender == "Female"):
            return "nl", "nl-NL", "nl-NL-FennaNeural"
    if (languageName == 'Portuguese'):
        if (gender == "Male"):
            return "pt", "pt-BR", "pt-BR-AntonioNeural"
        if (gender == "Female"):
            return "pt", "pt-BR", "pt-BR-FranciscaNeural"
    if (languageName == 'Icelandic'):
        if (gender == "Male"):
            return "is", "is-IS", "is-IS-GunnarNeural"
        if (gender == "Female"):
            return "is", "is-IS", "is-IS-GudrunNeural"
    if (languageName == 'Japanese'):
        if (gender == "Male"):
            return "ja", "ja-JP", "ja-JP-KeitaNeural"
        if (gender == "Female"):
            return "ja", "ja-JP", "ja-JP-NanamiNeural"
    if (languageName == 'Russian'):
        if (gender == "Male"):
            return "ru", "ru-RU", "ru-RU-DmitryNeural"
        if (gender == "Female"):
            return "ru", "ru-RU", "ru-RU-SvetlanaNeural"


def mt(text, source, target):
    # Add your subscription key and endpoint
    subscription_key = "a5d1179eb1c14961b6ba8fdff1c25470"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "westus2"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': source,
        'to': [target]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    response =  response[0]
    response = response["translations"]
    response = response[0]
    response = response["text"]
    return response

def speak(response, target4, targetAccent):
    speech_config = speechsdk.SpeechConfig(subscription="fa090106709c4548a07cfcab8fcd8ee1",
                                           region="westus")
    # Note: if only language is set, the default voice of that language is chosen.
    speech_config.speech_synthesis_language = target4  # For example, "de-DE"
    # The voice setting will overwrite the language setting.
    # The voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = targetAccent
    #audio_config = speechsdk.audio.AudioOutputConfig(filename="sentence22.wav")
    #synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    #synthesizer.speak_text_async(response)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(response)
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    languageOptions = ['English', 'Spanish', 'Polish', 'Dutch', 'Portuguese', 'Icelandic', 'Japanese', 'Russian']

    layout = [[sg.Text('Choose Source Language', size=(20, 1), font='Lucida', justification='left')],
              [sg.Combo(
                  languageOptions,
                  default_value='English', key='source')],
              [sg.Text('Choose Target Language ', size=(20, 1), font='Lucida', justification='left')],
              [sg.Combo(
                  languageOptions,
                  default_value=  "Spanish", key='target')],
              [sg.Text('Choose Output Voice', size=(20, 1), font='Lucida', justification='left')],
              [sg.Radio('Male', "OutputVoice", default=False)],
              [sg.Radio('Female', "OutputVoice", default=True)],
              [sg.Button('SAVE', font=('Times New Roman', 12)), sg.Button('CANCEL', font=('Times New Roman', 12))]]

    # Create the window
    window = sg.Window("Demo", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        if event == "SAVE" or event == sg.WIN_CLOSED:
            break
    gender = ""
    if (values[0] == True):
        gender = "Male"
    if (values[1] == True):
        gender = "Female"
    window.close()
    source2, source4, sourceAccent = getCodes(values['source'], gender)
    target2, target4, targetAccent = getCodes(values['target'], gender)

    text = from_mic(source4)
    response = mt(text, source2, target2)
    print(response)
    speak(response, target4, targetAccent)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
