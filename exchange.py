import requests
import json

api_key="<yyour api key>"
api_url= f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz=input("bozulan doviz turu : ")
alinan_doviz=input("alinan doviz turu : ")
miktar = int(input(f"N ekadar {bozulan_doviz} bozdurmak istiyorsunuz : "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))
