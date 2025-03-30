import requests
import json

api_key = "d727d7e77dda36dfc6eb57e1"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan doviz turu: ") #USD
alinan_doviz = input("Alinan doviz turu: ") #TRY

miktar = input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ")
sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)
print(sonuc_json["conversion_rates"][alinan_doviz])
