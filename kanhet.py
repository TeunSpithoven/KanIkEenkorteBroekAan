# kan ik een korte broek aan?
import requests

response = requests.get('https://www.kanikeenkortebroekaan.nl')

ja = 'meta property="og:title" content="Kan ik een korte broek aan? - ja! "'
koertebroek = ja in response.text

print(koertebroek)
