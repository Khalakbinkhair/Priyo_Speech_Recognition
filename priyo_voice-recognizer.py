#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install SpeechRecognition')


# In[2]:


get_ipython().system('pip install PyAudio')


# In[3]:


get_ipython().system('pip install pyttsx3')


# In[4]:


get_ipython().system('pip install pipwin')


# In[166]:


import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes


# In[167]:


get_ipython().system('pip install pyjokes')


# In[168]:


lis = sr.Recognizer()
priyo= pyttsx3.init()
voices= priyo.getProperty('voices')
priyo.setProperty('voice',voices[2].id)

def talk(text):
    priyo.say(text)
    priyo.runAndWait()
    


# In[169]:


def take_command():
    try:
        with sr.Microphone() as micro:
#         print('Listening....')
           voice= lis.listen(micro)
        command=lis.recognize_google(voice)
        command=command.lower()
        if 'priyo' in command:
            command=command.replace('priyo','')
        
    
    
    except:
        pass
    return command
    


# In[173]:


def run_priyo():
    command =take_command()
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Thank You For asking..... ... Current Time is'+time)
    elif 'play' in command:
            song=command.replace('play','')
            print('Thanks for Command...i\'m playing'+ song)
            pywhatkit.playonyt(song)
    elif 'tell me' in command:
            search=command.replace('tell me','')
            info= wikipedia.summary(search,1)
            talk(info)
    elif ' say a joke' in command:
            search=command.replace(' say a joke','')
            info= pyjokes.get_joke()
            talk(info)
           
            
            
            
run_priyo()


# In[ ]:




