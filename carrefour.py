from gpiozero import LED, Button
from time import sleep
import RPi.GPIO as GPIO
import sys
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
	signal_vert_pieton.blink(on_time = 0.5, off_time = 0.5, n = 3, background = False)
	
try:
    while True:
        
        vert_voiture()
        rouge_pieton()
        attendre(bouton)
        attendre(1)
        orange_voiture()
        attendre(1)
        rouge_voiture()
        attendre(1)
        vert_pieton()
        attendre(5)
        rouge_pieton()
        attendre(1)

except KeyboardInterrupt:
    print("fin du programme")
finally:
    GPIO.cleanup()
    sys.exit()
