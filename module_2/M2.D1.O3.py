import time

def stoplicht():
    while True:
        print("Rood")
        time.sleep(20)

        print("Groen")
        time.sleep(30)

        print("Oranje")
        time.sleep(10)

stoplicht()