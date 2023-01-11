# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:52:55 2022

@author: Bryant McArthur
"""

import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr
from os import path
from pydub import AudioSegment


def TTS(text, outfile, langcode = 'pl-PL', langname = 'pl-PL-MarekNeural'):
    """Parameters:
        text string to synthesize to speech
        outfile to store the audio file
        langcode defaulted to Polish
        Langname defaulted to Polish speaking Marek    
    """
    
    speech_config = speechsdk.SpeechConfig(subscription="96cb8e71a4c745c3bc414aa21b8a303b", region="westus")
    #                                                   94d4c73e70fa4ae1821d98160e5b6009

    
    # Note: if only language is set, the default voice of that language is chosen.
    speech_config.speech_synthesis_language = langcode # For example, "de-DE"
    # The voice setting will overwrite the language setting.
    # The voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = langname
    
    audio_config = speechsdk.audio.AudioOutputConfig(filename=outfile)
    
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text)
    
    
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text)

    # Get result
    speech_synthesis_result = synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
    
    return

# convert mp3 file to wav                                                       
#sound = AudioSegment.from_mp3("transcript.mp3")
#sound.export("transcript.wav", format="wav")


def STT(outfile, AUDIO_FILE = "transcript.wav",):
    """Speech Recognition: Transcribes audio file"""
    
    # use the audio file as the audio source                                        
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file                  
            
            output = "Transcription: " + r.recognize_google(audio)
            
            print(output)
    with open(outfile, 'w', encoding = 'utf-8') as myfile:
        myfile.write(output)
            
            
if __name__ == "__main__":
    filename = "C:/Users/bryan/Documents/Work/github/ted_spanish.txt"
    with open(filename, 'r', encoding = "utf-8") as myfile:
        text = myfile.read()
    # print(text)
    outfile = "C:/Users/bryan/Documents/Work/github/ted.wav"
    TTS(text, outfile, langcode = "es-ES", langname = 'es-ES-DarioNeural')
    print("created .wav file. Now we will process the speech back to text")
    # STT("transcribed_jacko.txt", "jacko.wav")
    
    pass
