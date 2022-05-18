import re, keyboard, datetime, pyttsx3, pywhatkit, wikipedia, os
import speech_recognition as sr
import subprocess as sub
from pygame import mixer
from pywhatkit.remotekit import start_server
from flask import Flask, request

bot = "Arturito"
listener = sr.Recognizer()


sites = {
    'google':'google.com',
    'youtebe':'youtube.com',
    'facebook':'facebook.com',
    }
files = {

}


def indentify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)","^([A-Za-z]+)$"]
    for pattern in patterns:
       try:
           name = re.findall(pattern, text)[0]
       except IndexError:
           talk("Porfavor dime tu nombre uwu")
    return name


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listener():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec


def write(f):
    talk("que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, ya puedes ver tu anotacion")
    sub.Popen("nota.txt", shell=True)


def run_Arturito():
    rec = listener(text)
    name = indentify_name(rec)
    engine.say("Hola como te llamas")
    engine.runAndWait()

    if name:
        engine.say("Encantada de concerte, {}".format(name))
    else:
        engine.say("No te he entendido, puedes repetirlo?")
    engine.runAndWait()

    while True:
        if 'reproduce' in rec:
            video = rec.replace('reproduce', '')
            print("Reproducioendo" + video)
            talk("Reproduciendo" + video)
            pywhatkit.playonyt(video)
        elif 'busca' in rec:
            search = rec.place('busca', '')
            wiki = wikipedia.summary(search, 1)
            print( search + ": " + wiki)
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip()
            talk("Alarma activada a las " + num + "horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == num :
                    print("ya es hora!!")
                    mixer.init()
                    mixer.music.load("auronplay-alarma.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe {sites[sites]}', shell=True)
                    talk(f'Abriendo {site}')
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True)
                    talk(f'Abriendo {file}')
        elif 'escribe' in rec:
            try:
                with open('documento.txt', 'a') as f:
                    write(f)
            except FileNotFoundError as e:
                file = open("documento.txt", 'w')
                write(file)
        elif 'adios' in rec:
            talk('Hasta pronto!')
            break


if __name__ == '__main__':
    run_Arturito()
