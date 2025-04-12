import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather



def Action(data):
    if data is None:
        return "Sorry, I didn't get any input."

    user_data = data.lower()



    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is AI Assistant.")
        return "My name is AI Assistant."

    elif "hello" in user_data:
        text_to_speech.text_to_speech("Hello, how can I assist you today?")
        return "Hello, how can I assist you today?"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning! How can I help you today?")    
        return "Good morning! How can I help you today?"
        

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = str(current_time.hour) + " Hour : " + str(current_time.minute) + " Minute"
        text_to_speech.text_to_speech("The current time is " + Time)
        return "The current time is " + Time


    elif "shut down" in user_data:
        text_to_speech.text_to_speech("Shutting down the system.")
        return "Shutting down the system."

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("Youtube is ready for you.")
        return "Youtube is ready for you."


    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("Playing music for you.")
        return "Playing music for you."

    elif "google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("Google is ready for you.")
        return "Google is ready for you."
    
    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech("The weather is " + ans)  
        return "The weather is " + ans




    else:
        text_to_speech.text_to_speech("Sorry, I did not understand that.")
        return "Sorry, I did not understand that."