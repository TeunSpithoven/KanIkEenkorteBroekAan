# kan ik een korte broek aan?
import requests

x = requests.get('https://www.kanikeenkortebroekaan.nl')

y = 'meta property="og:title" content="Kan ik een korte broek aan? - nee! "' not in x.text

print(y)
