import pyautogui
from pynput.mouse import Button, Controller
import pydirectinput
import time


time.sleep(3)

#Controllo che si sia attivata l'abilità e controllo lo stato di cattura
def riconoscimentoCattura():
    #Inizializzo le variabii del tempo e della cattura  
    timeout_start = time.time()
    flagIndagine = False
    flagCattura = False
    risultato = False
    timout = 13
    #Controlla per 15 secondi la presenza dell'icona e che si sia attivatà l'abilità
    while time.time() < timeout_start + timout:
        #Boolean che diventa True se trova l'icona
        if pyautogui.locateOnScreen('PokeBot\images\Cattura.png', confidence=0.9) != None:
            flagCattura = True
        #Boolean che diventa True se si attiva l'abilità
        if pyautogui.locateOnScreen('PokeBot\images\Indagine.png', confidence=0.7) != None:
            flagIndagine = True
    if flagCattura == True and flagIndagine == True:
        risultato = True
    return(risultato)



#PPP
def primoFurto():
    time.sleep(0.4)
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')
#PPDP
def secondoFurto():
    time.sleep(0.4)
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')
    pydirectinput.keyDown('d')
    time.sleep(0.4)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')
#PPDDP
def terzoFurto():
    time.sleep(0.4)
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')
    pydirectinput.keyDown('d')
    time.sleep(0.4)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('d')
    time.sleep(0.4)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')



#Usa Fuga
def Fuga():
    time.sleep(0.4)
    pydirectinput.keyDown('d')
    time.sleep(0.4)
    pydirectinput.keyUp('d')
    time.sleep(0.4)
    pydirectinput.keyDown('s')
    time.sleep(0.4)
    pydirectinput.keyUp('s')
    time.sleep(0.4)
    pydirectinput.keyDown('p')
    time.sleep(0.4)
    pydirectinput.keyUp('p')

#Se sono Meowth e si è attivatà l'attività, uso furto. Altrimenti Scappo.
def Furto():
    if riconoscimentoCattura() == True:
        global encounter
        encounter += 1
        print("Oggetti trovati: ", +encounter)
        primoFurto()
        time.sleep(24)
        secondoFurto()
        time.sleep(24)
        terzoFurto()
        time.sleep(24)
        Fuga()
        time.sleep(1.5)
        rimozioneElemento()
        time.sleep(1)
    else:
        Fuga()

#Usa Profumino di Oddish, impostato sulla key I
def Profumino():
    time.sleep(1)
    pydirectinput.keyDown('i')
    time.sleep(1)
    pydirectinput.keyUp('i')

#Rimuove l'oggetto rubato dopo ogni volta che viene usato Furto
def rimozioneElemento():
    mouse = Controller()
    mouse.position = (1333, 277)
    time.sleep(1)
    mouse.click(Button.right)
    mouse.position = (895, 507)
    time.sleep(1)
    mouse.click(Button.left)
    mouse.position = (892, 464)
    time.sleep(1)
    mouse.click(Button.left)
    mouse.position = (917, 236)
    time.sleep(1)
    mouse.click(Button.left, 2)

#Uso teletrasporto per tornare al centro pokemon, impostato sulla key U
def Teletrasporto():
    time.sleep(1)
    pydirectinput.keyDown('u')
    time.sleep(1)
    pydirectinput.keyUp('u')
    #Leggera pausa
    time.sleep(4)

#Curo i pokemon
def centroPokemon():
    pydirectinput.keyDown('p')
    time.sleep(5)
    pydirectinput.keyUp('p')

#Parto dal Centro Pokemon di Celestopoli e raggiungo l'erba alta
def Ritorno():
    #ESCO DAL CENTRO POKEMON
    pydirectinput.keyDown('s')
    time.sleep(2)
    pydirectinput.keyUp('s')
    time.sleep(1)
    pydirectinput.keyDown('a')
    time.sleep(0.5)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(0.5)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(4)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(1)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(4)
    pydirectinput.keyUp('d')
    #ENTRO NELLA CASA
    pydirectinput.keyDown('w')
    time.sleep(1)
    pydirectinput.keyUp('w')
    time.sleep(1)
    pydirectinput.keyDown('a')
    time.sleep(0.1)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(0.8)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(0.3)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(2)
    pydirectinput.keyUp('w')
    #ESCO DALLA CASA
    time.sleep(1)
    pydirectinput.keyDown('d')
    time.sleep(0.8)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(2)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(0.6)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(3.3)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('a')
    time.sleep(2.8)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(2.5)
    pydirectinput.keyUp('s')


encounter = 0
#LOOP PER IL BOT
def Ciclo():
    Ciclo = 0
    while True:
        contatore = 0
        centroPokemon()
        Ritorno()
        while (contatore < 6):
            Profumino()
            Furto()
            contatore += 1
        Teletrasporto()
        time.sleep(3)
    Ciclo += 1

Ciclo()



    
