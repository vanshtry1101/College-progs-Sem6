import requests

html = requests.get("https://www.google.com")
print(html.text)