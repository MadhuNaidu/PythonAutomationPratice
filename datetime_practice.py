import datetime

# print(datetime.date(2026, 1, 26))
# print(datetime.date.today())
# print(datetime.date.today().year)
# print(datetime.date.today().month)
# print(datetime.date.today().day)
# %m%d%Y

# 1-3-2026
print(datetime.date.today().strftime("%d-%m-%y"))
print(datetime.date.today().strftime("%d-%m-%y"))
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%a"))
print(datetime.datetime.now().strftime("%A"))
print(datetime.datetime.now().strftime("%w"))
print(datetime.datetime.now().strftime("%d"))
print(datetime.datetime.now().strftime("%b"))
print(datetime.datetime.now().strftime("%B"))
print(datetime.datetime.now().strftime("%p"))
print(datetime.datetime.now().strftime("%H"))
print(datetime.datetime.now().strftime("%I"))
