import speech_recognition as sr
import webbrowser as Browser

recognizer = sr.Recognizer()

print("Search for your Favourite TV Shows, Movies, Songs & Much More from your Favourite Streaming Sites...")
x = 0
while x == 0:
    with sr.Microphone() as source:
        print("You may Select from any of these Streaming Platform...")
        print("-> YouTube")
        print("-> Spotify")
        print("-> Netflix")
        print("-> Amazon Prime")
        print("-> Hotstar\n")
        speech = recognizer.listen(source)
        try:
            speech_string = recognizer.recognize_google(speech)
            if speech_string[len(speech_string) - 7:] == "YouTube":
                url = 'https://www.youtube.com/results?search_query='
                media = speech_string[:len(speech_string) - 11]
                print("Showing Results for {} on YouTube...".format(media))
                x = 1
                Browser.open_new(url + media)

            elif speech_string[len(speech_string) - 7:] == "spotify":
                url = 'https://open.spotify.com/search/'
                media = speech_string[:len(speech_string) - 11]
                print("Showing Results for {} on Spotify...".format(media))
                x = 1
                Browser.open_new(url + media)

            elif speech_string[len(speech_string) - 7:] == "Netflix":
                url = 'https://www.netflix.com/search?q='
                media = speech_string[:len(speech_string) - 11]
                print("Showing Results for {} on Netflix...".format(media))
                x = 1
                Browser.open_new(url + media)

            elif speech_string[len(speech_string) - 12:] == "Amazon Prime":
                url = 'https://www.primevideo.com/search/ref=atv_nb_sr?phrase='
                media = speech_string[:len(speech_string) - 16]
                print("Showing Results for {} on Amazon Prime...".format(media))
                x = 1
                Browser.open_new(url + media)

            elif speech_string[len(speech_string) - 7:] == "hotstar":
                url = 'https://www.hotstar.com/in/search?q='
                media = speech_string[:len(speech_string) - 11]
                print("Showing Results for {} on Hotstar...".format(media))
                x = 1
                Browser.open_new(url + media)

            else:
                print("You didn't Select from Given Choices!\n")
        except sr.UnknownValueError:
            print("No Input was Detected!")
            print("Terminating the Program...")
            x = 1
        except sr.RequestError:
            print("Recognition Connection Failed!")
            x = 1
