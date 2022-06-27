import pyautogui as spam
import time

limite = int(input("Quantidades de mensagens: "))
msg = input("Qual a mensagem que quer spammar? ")

time.sleep(5)

i = 0
while i < limite:
    spam.typewrite(msg)
    spam.press("Enter")
    i += 1