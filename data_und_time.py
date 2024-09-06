import datetime
dat = datetime.date
nin_day = dat.today()
delta_day = datetime.timedelta(1)
# print(nin_day + delta_day)
# swobod_day = dat(2024, 6, 26)
# print(swobod_day)
time = datetime.time
# Uhr = time(13, 59, 59)
# print(Uhr)
# data_und_time = datetime.datetime
# nin_moment = data_und_time.now()
# print(nin_moment)
# swobod_day = dat(2020, 5, 25)
# swobod_day_2 = dat(2023, 2, 23)
# # day_rasn = swobod_day - swobod_day_2
# # print(day_rasn.days)
# delta_day = datetime.timedelta(30)
# result_day = swobod_day + delta_day
# print(result_day)
# a = 9
# wremena = []
# while a <= 18:
#     Uhr = time(a, 0, 1)
#     a += 1
#     wremena.append(Uhr)
# print(wremena)
a = 1
swobod_dayi = []
while a <= 5:
    nin_day = dat.today()
    delta_day = datetime.timedelta(a)
    swobod_day = nin_day + delta_day
    text_data = swobod_day.strftime("%d/%m/%Y")
    print(text_data)
    swobod_dayi.append(swobod_day)
    a += 1
print(swobod_dayi)