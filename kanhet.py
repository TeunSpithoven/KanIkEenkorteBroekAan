# kan ik een korte broek aan?
import requests

daan = input('ben je Daan Telkamp? (ja/nee)')

if (daan == 'ja'):
    print('True')

else:
    response = requests.get('https://www.kanikeenkortebroekaan.nl')

    ja = 'meta property="og:title" content="Kan ik een korte broek aan? - ja! "'
    koertebroek = ja in response.text
    print(koertebroek)
