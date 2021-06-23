import pyttsx3

engine=pyttsx3.init()
engine.say("Hello world, welcome to my channel")
engine.save_to_file("Hello world,welcome to my channel", 'test.mp3')
engine.runAndWait()
