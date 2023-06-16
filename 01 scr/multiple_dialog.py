#
# Mehrere Eingaben erfassen
# 
from easygui import *

# message to be displayed
text = "Bitte die folgende Eingaben machen:"

# window title
title = "Datenerfassung"

# list of multiple inputs
input_list = ["Name", "Vorname", "Abteilung", "Maiadresse"]

# list of default text
# default_list = ["Mustermann", "Max", "Marketing", "max.mustermann@firma.de"]
default_list = []

# creating a integer box
output = multenterbox(text, title, input_list, default_list)

# title for the message box
title = "Message Box"

# creating a message
message = "Eingaben: " + str(output)

# creating a message box
msg = msgbox(message, title)

# creating a integer box
passwd = passwordbox("Bitte Passwort eingeben", "Passwort", "")

# creating a message box
msg = msgbox(passwd, title)