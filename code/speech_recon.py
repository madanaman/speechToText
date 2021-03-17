import speech_recognition as sr
import pyttsx3

#initialize the recognizer
r = sr.Recognizer()

#Speak Text
def speak_text(command):

    #initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

speak_text("Hi There")

# Loop infinitely for user to
# speak
while 1:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("speak up now")
            audio2 = r.listen(source2)

            myText = r.recognize_google(audio2)
            myText = myText.lower()

            print("did you say :"+myText)
            speak_text(myText)

    except sr.RequestError as e:
        print("Could not request results: {e}".format(e))

    except sr.UnknownValueError as e:
        print("unknown error encountered")

