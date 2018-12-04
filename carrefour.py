from gpiozero import LED, Button
from time import sleep
import RPi.GPIO as GPIO
import sys
import os
#from carrefour_helper import *

signal_vert_voiture = LED(17)
signal_orange_voiture = LED(27)
signal_rouge_voiture = LED(22)
signal_vert_pieton = LED(23)
signal_rouge_pieton = LED(24)
bouton_pieton = Button(25)
bouton = "bouton"


def attendre(s):
    if (s == bouton):
        bouton_pieton.wait_for_press()
    else:
        sleep(s)

def vert_voiture():
    signal_vert_voiture.on()
    signal_orange_voiture.off()
    signal_rouge_voiture.off()
    
def orange_voiture():
    signal_vert_voiture.off()
    signal_orange_voiture.on()
    signal_rouge_voiture.off()

def rouge_voiture():
    signal_vert_voiture.off()
    signal_orange_voiture.off()
    signal_rouge_voiture.on()
    
def vert_pieton():
    signal_vert_pieton.on()
    signal_rouge_pieton.off()
    
def rouge_pieton():
    signal_vert_pieton.off()
    signal_rouge_pieton.on()

def vert_pieton_clignotement():
    signal_vert_pieton.blink(on_time=0.5, off_time=0.5, n=3, background=False)
    
def shutdown():
    print ("shutting down now")
    GPIO.cleanup()
    os.system("sudo halt")
    sys.exit()

def bouton_callback():
    for i in range(60):
        #print ("je suis la, i = ", i)
        if GPIO.input(25):
            #print("ici aussi i = ", i)
            break
        sleep(0.05)
        
    if 25 <= i < 59: # if released between 1.25 & 3s close program
        print ("Closing program")
        GPIO.cleanup()
        sys.exit()
        
    if not GPIO.input(25):
        if i >= 59:
            print("shutdown")
            shutdown()

print ("Debut du programme")
bouton_pieton.when_pressed = bouton_callback

try:
    while True:
        vert_voiture()
        rouge_pieton()
        attendre(bouton)
        attendre(1)
        orange_voiture()
        rouge_pieton()
        attendre(2)
        rouge_voiture()
        rouge_pieton()
        attendre(2)
        rouge_voiture()
        vert_pieton()
        attendre(5)
        vert_pieton_clignotement()
        rouge_voiture()
        rouge_pieton()
        attendre(2)
        vert_voiture()
        rouge_pieton()
        
        

except KeyboardInterrupt:
    print("fin du programme")
finally:
    GPIO.cleanup()
    sys.exit()
