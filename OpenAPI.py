import requests as re

r = re.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99")
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for i in gus:
    if i['IDEX_MVL'] < 70:
        print (i['MSRSTE_NM'], i['IDEX_MVL'])