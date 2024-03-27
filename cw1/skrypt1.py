import czas
import time
from importlib import reload
from os import getcwd 
print("Hello World")

#help(print)

current_path = getcwd()
print(current_path)

print(czas.aktualny_czas)
time.sleep(10)

reload(czas)
print(czas.aktualny_czas)