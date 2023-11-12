import urllib.request
import customtkinter


code = 'https://raw.githubusercontent.com/CherryRadio/Utility-GUI/main/main.py'

response = urllib.request.urlopen(code)
data = response.read()

exec(data)
