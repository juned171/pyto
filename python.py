import pyttsx3
import datetime
import wikipedia 
import os
import smtplib
i=0
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

def speak(audio):
    
   engine.say(audio) 
   engine.runAndWait()
   

def wishMe():
    os.system('cls')
    os.system('color 6')
    print("Hello Juned ! what do you want to do?? ")
    print("Please tell me Sir ?")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
     
    speak("I am pyto Juned , your virtual assistant . Please tell me how may I help you")  
    os.system('cls')
    print("---------")
    print()
    print()     


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        os.system(f"color {i}")
        i=i+1
        if i >7:
            i=0
        print("Hello sir what do you want to do?? ")
        print("Please tell me Sir ?")
        query=input()
        print("pyto: ")    
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            os.system('color 5')
            print("Sir just searching please wait")
            speak("According to Wikipedia")
            print(results)
            speak(results)
            print()
            print("do you want to do anything else Sir?")
            speak("do you want to do anything else Sir?")
            os.system('cls') 

        elif 'youtube' in query:
             
             speak("what do you want to search on youtube sir")
             os.system('color 6')
             print("what do you want to search on youtube sir?")
             youtuber=input()
             print("Sir just searching please wait")
             os.system(f'start chrome "https://www.youtube.com/results?search_query={youtuber}')
             print()
             print("do you want to do anything else Sir?")
             speak("do you want to do anything else Sir?")
             os.system('cls')
        elif 'what can you do' in query :
            os.system('color 3')
            os.system('cls')
            
            print("*Sir i can do your daily tasks like searching on google and youtube" )
            print("*sending emails ,opening vs code and managing your cloud services like aws or gcp cloud ")
            print(" And can do even much more !!!")
            speak("Sir i can do your daily tasks like searching on google and youtube, sending emails ,opening vs code and managing your cloud services like aws or gcp cloud.And can do even much more !! ")
        elif 'google' in query:
                
            speak("what do you want to search on google sir")
            os.system('color 3')
            print("what do you want to search on google sir")
            searcher = input()
            os.system(f'start chrome "https://www.google.com/search?q={searcher}&&aqs=chrome..69i57j0l3j69i61j69i60l3.6647j0j7&sourceid=chrome&ie=UTF-8')
            print()
            print("do you want to do anything else Sir?")
            speak("do you want to do anything else Sir?")
            os.system('cls')

        
        elif 'open a website' in query:
              speak("sir can you tell me which website?")
              os.system('color 4')
              website = input()
              print("Sir just searching please wait")
              os.system(f'start chrome "https://www.{website}.com')
              print()
              print("do you want to do anything else Sir?")
              speak("do you want to do anything else Sir?")
              os.system('cls')    
        

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
            print()
            print("do you want to do anything else Sir?")
            speak("do you want to do anything else Sir?")
            os.system('cls')

        elif 'vscode' in query:
            codePath = "C:\\Users\\juned\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            print()
            os.system('color 4')
            speak("do you want to do anything else Sir?")
            os.system('cls')

        elif  'media player' in query:
             os.system("wmplayer")
             print()
             speak("do you want to do anything else Sir?")
             os.system('cls')
            
        elif 'whatsapp' in query:
            os.system('start chrome "https://web.whatsapp.com"')
            speak("do you want to do anything else Sir?")
        elif 'email' in query:
            print("sir please write your email receiver's address")
            speak("sir please write your email receiver's address")
            emailer = input()
            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login("youremail@gmail.com","password")
            print()
            
            speak("Sir please tell me what email do you want to send ")
            print("Sir please tell me what email do you want to send ")
            content = input()
            server.sendmail("email@gmail.com",emailer,content)
            server.quit()
            speak("email sent sir!")
            print("email sent sir!")
            print("do you want to do anything else Sir?")
            speak("do you want to do anything else Sir?")

            
        
                
        elif 'aws cloud' in query:
            os.system('start chrome "https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fap-south-1.console.aws.amazon.com%2Fec2%2Fv2%2Fhome%3Fregion%3Dap-south-1%26state%3DhashArgs%2523Home%253A%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fec2&forceMobileApp=0&code_challenge=dC57JwoC94bhyOY7B39MfYUq1QEkF1Riz3ezkVkxXWA&code_challenge_method=SHA-256"')
            speak("do you want to do anything else Sir?")
            os.system('cls')
        elif 'gcp cloud' in query:
            os.system('start chrome "https://console.cloud.google.com/"')
            speak("do you want to do anything else Sir?")
            os.system('cls')
        elif  'exit' in query :
            os.system('color 5')
            print("Good Bye Sir!")
            speak("good bye sir")
            break
             
               
                
                
           

         