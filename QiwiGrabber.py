import requests
from colorama import Fore, Back, Style

banner = Fore.YELLOW + Style.BRIGHT + """
  \  __\    /\__  _\    /\ \  __/\ 
\ \ \/\ \   \/_/\ \/    \ \ \/\ \ \ \  \/_/\ 
\ \ \ \ \    \ \ \     \ \ \ \ \ \ \    \ \ \
\ \ \ \ \     \_\ \__   \ \ \_/ \_\ \    \_\ \

  by @li0ard [ovnl.in] |   t.me/termuxmam / PIRATIKA


""" + Style.RESET_ALL

print(banner)

token = input("[Eblan] Введите ваш токен: ")

if token == "":
 print("[❌] Введите токен!")
 quit()

session = requests.Session()
session.headers['Accept']= 'application/json'
session.headers['authorization'] = 'Bearer ' + token

try:
 req = session.get("https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true").json()
 print("[🔔] Информация получена")
 print("Номер телефона: +" + str(req['contractInfo']['contractId']) + " (" + req["userInfo"]["operator"] + ")")
 print("Никнейм: qiwi.com/n/" + req['contractInfo']["nickname"]["nickname"])
 print("Дата создания кошелька: " + req['contractInfo']['creationDate'])
 print("IP: " + req["authInfo"]["ip"])
 print("Привязаная почта: " + req["authInfo"]["boundEmail"])
 try:
  req2 = session.get("https://edge.qiwi.com/identification/v1/persons/" + str(req['contractInfo']['contractId']) + "/identification").json()
  print("[🔔] Паспортные данные")
  print("ФИО: " + req2["firstName"] + " " + req2["lastName"])
  print("Дата рождения: " + req2["birthDate"])
  print("Серия и номер: " + req2["passport"])
  print("ИНН: " + req2["inn"])
 except:
  print("[⚠️] Произошла ошибка при получении паспортных данных")
except:
 print("[⚠️] Произошла ошибка")
