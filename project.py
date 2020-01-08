import speech_recognition  
from gtts import gTTS            
from pygame import mixer       


while True:                      

    sr = speech_recognition.Recognizer()          
    with speech_recognition.Microphone()as source: 
        sr.adjust_for_ambient_noise(source)     
        print('Talk now: ')       
        audio = sr.listen(source)  

    try:
        message = (sr.recognize_google(audio)) 
                                           
        print(message)                        
    

        if 'hello' in message:              
            speech = ('Hello, whats up..?')  
            tts = gTTS(text=speech, lang='en')        
            tts.save('H:\\aaa\\hello.mp3')
            mixer.init()                              
            mixer.music.load('H:\\aaa\\hello.mp3') 
            mixer.music.play() 

        if 'good morning' in message:
            speech = ('Good Morning, how are you')
            tts = gTTS(text=speech, lang='en',slow = False)
            tts.save('H:\\aaa\\morning_greeting.mp3')
            mixer.init()
            mixer.music.load('H:\\aaa\\morning_greeting.mp3')
            mixer.music.play()


        if 'what is your name' in message:
            speech = ('my name is mafia')
            tts = gTTS(text=speech, lang='en')
            tts.save('H:\\aaa\\name.mp3')
            mixer.init()
            mixer.music.load('H:\\aaa\\name.mp3')
            mixer.music.play()

        if 'what are you doing' in message:
            speech = ('i am thinking how to increase my intelligence')
            tts = gTTS(text=speech, lang='en')
            tts.save('H:\\aaa\\doing.mp3')
            mixer.init()
            mixer.music.load('H:\\aaa\\doing.mp3')
            mixer.music.play()


    except Exception:                            
        print("Could not understand")                  