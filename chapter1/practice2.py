#search in google text to speech python copy the (pip install pyttsx3) run this in terminal and copy the usage code in that website and run that code

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text")
engine.runAndWait()