from datetime import datetime, timedelta, time
from random import randint
import re

def get_alt_time(num):
    ct = datetime.now()
    d, s, micros = int(ct.strftime("%w")), int(ct.strftime("%H")) * 3600 + int(ct.strftime("%M")) * 60 + int(ct.strftime("%S")), int(ct.strftime("%f"))
    ct = timedelta(d, s, micros)

    if 5 < num <= 30:
        rand_min = randint(-30, 30) + num * 60

        if randint(0, 1) == 0:
            return ct + timedelta(0, rand_min, 0), 2
        else:
            return ct - timedelta(0, rand_min, 0), 2

    elif 30 < num <= 80:
        rand_h = randint(1, 4) * 3600

        if randint(0, 1) == 0:
            return ct + timedelta(0, rand_h, 0), 3
        else:
            return ct - timedelta(0, rand_h, 0), 3
    
    elif 80 < num <= 100:
        rand_d, rand_h = randint(1, 3), randint(0, 12) * 3600

        if randint(0, 1) == 0:
            return ct + timedelta(rand_d, rand_h, 0), 4
        else:
            return ct - timedelta(rand_d, rand_h, 0), 4

    return ct, 1

print("\nIt's Shrimp Time!\n")
while True:
    rand_num = randint(0, 100)
    t, rand = get_alt_time(rand_num)
    t = re.split("[days, : .]", str(t))
    t_list = list(filter(None, t))

    if len(t_list) == 4:
        t_list.insert(0, 0)

    d, h, m, s, micros = list(map(int, t_list))
    alt_t = datetime(2018, 1, d + 7, h, m, s, micros)

    if rand == 1:
        print("It's exactly " + alt_t.strftime("%H:%M:%S.%f") + " on " + alt_t.strftime("%A"))
    elif rand == 2:
        print("It's around " + alt_t.strftime("%H:%M") + " on " + alt_t.strftime("%A"))
    elif rand == 3:
        print("It's like " + alt_t.strftime("%I %p") + " on " + alt_t.strftime("%A") + ", I think")
    else:
        print("It's uhhh... " + alt_t.strftime("%A"))

    user = input("")
    if user == "n":
        break