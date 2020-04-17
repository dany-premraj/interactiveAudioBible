import mysql.connector


import sys

modulename = 'mysql.connector'
if modulename not in sys.modules:
    print( 'You have not imported the {} module'.format(modulename))


mydb = mysql.connector.connect(
  host="localhost",
  user="jeni",
  passwd="passpass",
  database="tamil_bible"
)




import speech_recognition as sr
r=sr.Recognizer()
mic=sr.Microphone()
#sr.Microphone.list_microphone_names()
with mic as source:
    r.adjust_for_ambient_noise(source)
    print('speak...')
    audio=r.listen(source)
    try:
        tex=r.recognize_google(audio, language="ta-IN")
        print(tex)
        
    except:
        print('sorry... try again')
        exit()

#tex='சங்கீதம் 1 1'
q=tex.split()
a=q[0]
b=q[1]

d={0: 'ஆதியாகமம்', 1: 'யாத்திராகமம்', 2: 'லேவியராகமம்', 3: 'எண்ணாகமம்', 4: 'உபாகமம்', 5: 'யோசுவா', 6: 'நியாயாதிபதிகள்', 7: 'ரூத்', 8: '1 சாமுவேல்', 9: '2 சாமுவேல்', 10: '1 இராஜாக்கள்', 11: '2 இராஜாக்கள்', 12: '1 நாளாகமம்', 13: '2 நாளாகமம்', 14: 'எஸ்றா', 15: 'நெகேமியா', 16: 'எஸ்தர்', 17: 'யோபு', 18: 'சங்கீதம்', 19: 'நீதிமொழிகள்', 20: 'பிரசங்கி', 21: 'உன்னதப்பாட்டு', 22: 'ஏசாயா', 23: 'எரேமியா', 24: 'புலம்பல்', 25: 'எசேக்கியேல்', 26: ' தானியேல் ', 27: 'ஓசியா', 28: 'யோவேல்', 29: 'ஆமோஸ்', 30: 'ஒபதியா', 31: 'யோனா', 32: 'மீகா', 33: 'நாகூம்', 34: 'ஆபகூக்', 35: 'செப்பனியா', 36: 'ஆகாய்', 37: 'சகரியா', 38: 'மல்கியா', 39: 'மத்தேயு', 40: 'மாற்கு', 41: 'லூக்கா', 42: 'யோவான்', 43: 'அப்போஸ்தலருடைய நடபடிகள்', 44: 'ரோமர்', 45: '1 கொரிந்தியர்', 46: '2 கொரிந்தியர்', 47: 'கலாத்தியர்', 48: 'எபேசியர்', 49: 'பிலிப்பியர்', 50: 'கொலோசெயர்', 51: '1 தெசலோனிக்கேயர்', 52: '2 தெசலோனிக்கேயர்', 53: '1 தீமோத்தேயு', 54: '2 தீமோத்தேயு', 55: 'தீத்து', 56: 'பிலேமோன்', 57: 'எபிரெயர்', 58: 'யாக்கோபு', 59: '1 பேதுரு', 60: '2 பேதுரு', 61: '1 யோவான்', 62: '2 யோவான்', 63: '3 யோவான்', 64: 'யூதா', 65: 'வெளிப்படுத்தின  விசேஷம்'}
#a='உபாகமம்'
l = [key  for (key, value) in d.items() if value == a]
#print(l[0])
aa=l[0]


if len(q)==3:
    c=q[2]
    sql = """select verse from bible where book={} and Chapter={} and Versecount={};""".format(aa,b,c)
    
elif len(q)==2:
    sql = """select verse from bible where book={} and Chapter={};""".format(aa,b)
else:
    c=q[2]
    d=q[4]
    sql = """select verse from bible where book={} and Chapter={} and Versecount between {} and {} """.format(aa,b,c,d)

    


mycursor = mydb.cursor()

#sql = """select verse from bible where book={} and Chapter={} and Versecount={};""".format(aa,b,c)

mycursor.execute(sql)

myresult = mycursor.fetchall()

w=[x[0] for x in myresult]
tex=" ".join(w)
print(tex)

import gtts as gt 
import os
text='கர்த்தர் என் மேய்ப்பராயிருக்கிறார், நான் தாழ்ச்சியட'
tts = gt.gTTS(tex, lang='ta')

#TO SAVE
tts.save("Tamil-Audio.mp3")
#TO PLAY
#os.system("Tamil-Audio.mp3")
import pyglet
song = pyglet.media.load('Tamil-Audio.mp3')
song.play()
pyglet.app.run()
  
  

