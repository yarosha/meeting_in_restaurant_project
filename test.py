import schedule
import time


def test():
    print(1)


schedule.every().day.at("22:54").do(test)

while True:
    schedule.run_pending()
    time.sleep(1)