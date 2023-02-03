from datetime import datetime

date = datetime.now()
time = date.strftime("%Y-%m-%d %H:%M:%S")
string = input() + '\n'

with open("statistic_type", "a") as fd:
    result = str(time) + ' ' + string
    fd.write(result)
