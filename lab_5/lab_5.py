import requests
import json
import tkinter as tk
import urllib

while True:
    mod = input('1 - Погода, 2 - hh.ru, 3 - NASA фото дня, 0 - exit: ')
    match mod:
        case '1':
            appid = "37c5a59347e3daf2d4502b606a3ae0d5"

            def get_city_id(s_city_name):
                try:
                    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                                       params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru',
                                               'APPID': appid})
                    data = res.json()
                    cities = ["{} ({})".format(d['name'], d['sys']['country'])
                              for d in data['list']]
                    print("city:", cities)
                    city_id = data['list'][0]['id']
                    print('city_id=', city_id)
                except Exception as e:
                    print("Exception (find):", e)
                    pass
                assert isinstance(city_id, int)
                return city_id


            def request_forecast(city_id):
                try:
                    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                    data = res.json()
                    print('city:', data['city']['name'], data['city']['country'])
                    for i in data['list']:
                        print((i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
                              i['weather'][0]['description'])
                except Exception as e:
                    print("Exception (forecast):", e)
                    pass


            city_id = get_city_id(input("Введите наименование нас. пункта: "))
            request_forecast(city_id)

        case '2':
            def getPage():
                params = {
                    'employer_id': 1795976,  # ID ИTМО
                    'area': 2  # ID CПБ
                }
                req = requests.get('https://api.hh.ru/vacancies', params)
                data = req.content.decode()
                req.close()
                return data
            s=0
            dat = json.loads(getPage())["items"]
            print("Топ 20 вакансий в Университет ИТМО:")
            for i in dat:
                i = i["name"]
                s += 1
                print(str(s) + '. ' + i)

        case '3':
            response = requests.get("https://api.nasa.gov/planetary/apod?api_key=Pq4YxPVm2gldtyDhHLN93vfC3Q0zE3ESUbIAo8UB")
            todos = json.loads(response.text)
            print(str(todos["hdurl"]) + " Подождите, окно скоро откроется")

            destination = 'bg.png'
            url = todos["hdurl"]
            urllib.request.urlretrieve(url, destination)

            window = tk.Tk()
            window.title('Фото дня Nasa')
            window.geometry('1920x1080')
            bg = tk.PhotoImage(file='bg.png')

            lab_bg = tk.Label(window, image=bg, width=1920, height=1080)
            lab_bg.place(x=0, y=0)

            window.mainloop()
        case '0':
            break
        case _:
            print("Wrong type!")
