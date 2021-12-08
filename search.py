import requests
import time
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    "User-Agent": ua.random,
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}

goroda = {"Минск": "1",
          "Светлогорск": "33",
          "Речица": "34"}


def get_data(city_from, id_city_to, travel_date):
    response = requests.get(url=f'https://618.by/api/v2/route/schedule-detail?id_city_from={goroda.get(city_from)}&id_city_to={goroda.get(id_city_to)}&date={travel_date}',
                            headers=headers).json()

    stops_start = response.get('stops_start')
    stops_finish = response.get('stops_finish')


    otprav_time = response.get('stops_start')[0]['stop_time']['4']
    kuda = response.get('schedule')
    ret = []
    for i in kuda:
        if i.get('count')>0:
            tim = time.strptime(i.get("time"), "%H:%M:%S")
            prib = int(tim.tm_hour)*60+int(tim.tm_min)+int(otprav_time)
            #print(f'mest {i.get("count")}\ncena {i.get("cost_adult")}\nposadka {prib//60}:{prib%60}:00')

            ret.append(f'mest {i.get("count")}\ncena {i.get("cost_adult")}\nposadka {prib//60}:{prib%60}:00\n\n')

    return ret


    #print(kuda)


if __name__ == '__main__':
    get_data("Речица", "Минск", '12.12.2021')

