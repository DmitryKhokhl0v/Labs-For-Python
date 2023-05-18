import speech_recognition
import pyttsx3
import requests
import json
import webbrowser


class VoiceAssistant:
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""


def setup_voice():
    voices = ttsEngine.getProperty("voices")

    if assistant.speech_language == "en":
        assistant.recognition_language = "en-US"
        if assistant.sex == "female":
            ttsEngine.setProperty("voice", voices[1].id)
        else:
            ttsEngine.setProperty("voice", voices[2].id)
    else:
        assistant.recognition_language = "ru-RU"
        ttsEngine.setProperty("voice", voices[0].id)


def listen_to_user(*args: tuple):
    with mic:

        recognized_data = ""
        rec.adjust_for_ambient_noise(mic, duration=2)

        try:
            print("Listening...")
            audio = rec.listen(mic, 5, 10)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        try:
            print("Started recognition...")
            recognized_data = rec.recognize_google(audio, language="en").lower()

        except speech_recognition.UnknownValueError:
            pass

        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data


def speak(text_to_speech):
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


if __name__ == "__main__":
    rec = speech_recognition.Recognizer()
    mic = speech_recognition.Microphone()

    ttsEngine = pyttsx3.init()

    assistant = VoiceAssistant()
    assistant.name = "Anny"
    assistant.sex = "female"
    assistant.speech_language = "en"

    setup_voice()
    # prep
    print("To give a request use [find, searching word and command].")
    speak("To give a request, use. find. searching word. and command.")
    while True:

        user_input = listen_to_user()
        print(user_input)
        user_input = user_input.split(" ")
        command = user_input[0]

        match command:
            case "find":
                print("I heard you. let me find.")
                speak("I heard you. let me find.")
                try:
                    comm = user_input[1]
                    res = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + comm)
                    data = res.json()[0]

                    while True:
                        type_command = user_input[-1]
                        print(type_command)
                        match type_command:
                            case "example":
                                for i in data["meanings"][0]["definitions"]:
                                    try:
                                        response = i["example"]
                                        break
                                    except:
                                        pass
                                speak(response)

                            case "definition":
                                for i in data["meanings"][0]["definitions"]:
                                    try:
                                        response = i["definition"]
                                        break
                                    except:
                                        pass
                                speak(response)
                                break

                            case "antonyms":
                                response = data["meanings"][0]["antonyms"]
                                response = ", ".join(response)
                                speak(response)
                                break

                            case "synonyms":
                                response = data["meanings"][0]["synonyms"]
                                response = ", ".join(response)
                                speak(response)
                                break

                            case "link":
                                url = res.json()[0]["phonetics"][0]["sourceUrl"]
                                print(url)
                                speak("Here you are")
                                webbrowser.get().open(url)
                                break

                            case "phonetic":
                                phonetic = res.json()[0]["phonetics"][0]["phonetic"]
                                print(phonetic)
                                speak("Here you are")
                            case other:
                                print("Can't understand the command. Please make sure you said the command word last.")
                                break
                except Exception as exc:
                    print("Exception :", exc)
                    pass
            case "hey" | "hello" | "hi":
                speak("Hey! How can i help you?")

            case "help":
                speak("To give a request, use. find. searching word. and command.")

            case "thanks" | "thank":
                speak("You welcome")
                ttsEngine.stop()
                quit()

            case "bye" | "goodbye":
                speak("See you later, goodbye!")
                ttsEngine.stop()
                quit()
            case "stop":
                speak("Stopping")
                ttsEngine.stop()
                quit()
            case other:
                speak("Sorry, as very young voice helper, i still don't understand much.")
                ttsEngine.stop()
