from multiprocessing import Process
import threading
import time

import requests
import datetime


def loop_thread0():
    while True:
        print("=== Thread 0 ===\n" + get_btc_price() + "\n================")
        time.sleep(1.0)


def loop_thread1():
    while True:
        t = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        print("=== Thread 1 ===\n" + "Current date and time: " + t + "\n================")
        time.sleep(10.0)


def get_btc_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if response.status_code == 200:
        data = response.json()
        return "Current Bitcoin price in USD: $ " + "{:.4f}".format(data["bpi"]["USD"]["rate_float"])
    else:
        return "Error while getting current Bitcoin price. Error status: " + str(response.status_code)


if __name__ == '__main__':
    p1 = Process(target=loop_thread0, args=())
    p1.start()

    p2 = Process(target=loop_thread1, args=())
    p2.start()