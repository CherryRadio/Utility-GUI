import urllib.request
import tkinter as tk
import subprocess
import platform

code = 'https://raw.githubusercontent.com/CherryRadio/Utility-GUI/main/main.py'

response = urllib.request.urlopen(code)
data = response.read()

exec(data)