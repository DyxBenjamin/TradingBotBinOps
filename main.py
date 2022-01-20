from iqoptionapi.stable_api import IQ_Option
import time

I_want_money = IQ_Option("bengarr.negocios@gmail.com", "Dayex23596_")
I_want_money.connect()  # connect to iqoption
ACTIVES = "AUDCAD"
duration = 5 # minute 1 or 5
amount = 1
media = 0.0
I_want_money.subscribe_strike_list(ACTIVES, duration)

while True:
    media = 0.0
    data = I_want_money.get_realtime_strike_list(ACTIVES, duration)
    for price in data:
        print(ACTIVES, "_price", price)
        media += float(price)

    media = media / len(data)
    print("_media", media)
    time.sleep(5)

I_want_money.unsubscribe_strike_list(ACTIVES, duration)
