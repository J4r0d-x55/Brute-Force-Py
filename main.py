import random
import pyautogui
import time

character = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\()*+,-./:;<=>?@[\]^_`{|}~"
character_list = list(character)
begin = time.time()

password = pyautogui.password("Entrez votre mot de passe ici: ")

guess_password = ''
while(guess_password != password):
    guess_password = random.choices(character_list, k=len(password))

    print(">>>" + str(guess_password))

    if(guess_password == list(password)):
        print("Votre mot de passe est: "  + "" .join(guess_password) + "\n" + "Trouvé en : " + str(time.time() - begin) + " secondes")
        break

