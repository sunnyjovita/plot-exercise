# number 1
import csv
import datetime as dt
import statistics as st
import matplotlib.pyplot as plt
# filename = "activity.csv"
# dict = {}
# dictInterval = {}
# dictIntervalWeekdays = {}
# dictIntervalWeekends = {}
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     headerRow = next(reader)
#     for row in reader:
#         steps = row[0]
#         if(steps != "NA"):
#             date = row[1]
#             date2 = int(dt.datetime.strptime(date,"%Y-%m-%d").day)
#             interval = int(row[2])
# # kalau belum default, gabisa masukin key kedalam dict
#             dict.setdefault(str(date),[])
#             dict[str(date)].append(int(steps))
#
#             dictInterval.setdefault(interval,[])
#             dictInterval[interval].append(int(steps))
#
#             if(date2 % 7 == 0):
#                 dictIntervalWeekends.setdefault(interval,[])
#                 dictIntervalWeekends[interval].append(int(steps))
#             else:
#                 dictIntervalWeekdays.setdefault(interval,[])
#                 dictIntervalWeekdays[interval].append(int(steps))
# listDate = []
# listTotal = []
# listAve = []
# for i in dict.keys():
#     listDate.append(i)
#     listTotal.append(sum(dict.get(i)))
#     listAve.append(st.mean(dict.get(i)))
# plt.hist(listTotal)
# plt.title("Total steps per day")
# plt.xlabel("Steps per day")
# plt.ylabel("Frequency")
# plt.yticks(range(0,25,5))
# plt.show()
#
# print("Mean : ",st.mean(listTotal))
# print("Median :",st.median(sorted(listTotal)))

# number 2
# import csv
# import datetime as dt
# import statistics as st
# import matplotlib.pyplot as plt
#
# filename = "activity.csv"
# dict = {}
# dictInterval = {}
# dictIntervalWeekdays = {}
# dictIntervalWeekends = {}
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     headerRow = next(reader)
#     for row in reader:
#         steps = row[0]
#         if(steps != "NA"):
#             date = row[1]
#             date2 = int(dt.datetime.strptime(date,"%Y-%m-%d").day)
#             interval = int(row[2])
# # kalau belum default, gabisa masukin key kedalam dict
#             dict.setdefault(str(date),[])
#             dict[str(date)].append(int(steps))
#
#             dictInterval.setdefault(interval,[])
#             dictInterval[interval].append(int(steps))
#
#             if(date2 % 7 == 0):
#                 dictIntervalWeekends.setdefault(interval,[])
#                 dictIntervalWeekends[interval].append(int(steps))
#             else:
#                 dictIntervalWeekdays.setdefault(interval,[])
#                 dictIntervalWeekdays[interval].append(int(steps))
# listDate = []
# listTotal = []
# listAve = []
# for i in dictInterval.keys():
#     listDate.append(i)
#     listTotal.append(sum(dictInterval.get(i)))
#     listAve.append(st.mean(dictInterval.get(i)))
# plt.plot(listTotal)
# plt.title("Total steps per day")
# plt.xlabel("Steps per day")
# plt.ylabel("Frequency")
# plt.yticks(range(0,25,5))
# plt.show()
#
# print("Mean : ",st.mean(listTotal))
# print("Median :",st.median(sorted(listTotal)))

# number 3
import csv
import re
import matplotlib.pyplot as plt
import statistics
#
# filename = "activity.csv"
# def count_NA():
#     with open(filename) as f:
#         x = f.read()
#         return len(re.findall("NA",x))
# def replace():
#     with open(filename) as f:
#         x = f.read()
#     with open("New File", "w+") as f:
#         f.write(re.sub("NA","0",x))
# def Med_Mean_perDay():
#     with open(filename) as f:
#         reader = csv.reader(f)
#         next(reader)
#         total = 0
#         Median_perDay = []
#         Mean_perDay = []
#         stepToday = []
#         while True:
#             try:
#                 total += 1
#                 step = next(reader)[0]
#                 stepToday.append(int(step) if step != "NA" else 0)
#                 if(total % 288 == 0):
#                     stepToday.sort()
#                     Median_perDay.append(statistics.median(stepToday))
#                     Mean_perDay.append(statistics.mean(stepToday))
#                     stepToday = []
#             except StopIteration:
#                 break
#         return Median_perDay, Mean_perDay
# def make_plot():
#     median,mean = Med_Mean_perDay()
#     fig,axs = plt.subplots(2)
#     axs[0].set_title("Median Per Day")
#     axs[0].plot(median,c ="red")
#     axs[0].set_xlabel("Days")
#     axs[0].set_ylabel("Steps")
#     axs[1].set_title("Mean Per Day")
#     axs[1].plot(mean,c= "blue")
#     axs[1].set_xlabel("Days")
#     axs[1].set_ylabel("Steps")
#     plt.tight_layout()
#     plt.show()

# number 4
import matplotlib.pyplot as plt
import csv
file = open("activity.csv", "r")
csvReader = csv.reader(file)
def perInterval():
    with open(file) as f:
        x = f.read()
    next(x)
    perInterval = [0]*288
    totalDays = 61
    total = 0
    while True:
        try:
            step = next(x)[0]
            perInterval[total] += int(step) if step != "NA" else 0
            total += 1
            if total == 288:
                total = 0
        except StopIteration:
            break
    weekdayAverage = []
    weekendAverage = []
    dayCounter = 1
    for steps in perInterval:
        if dayCounter in [6, 7]:
            weekendAverage.append(steps/totalDays)
        else:
            weekdayAverage.append(steps/totalDays)
        dayCounter += 1
        if dayCounter == 8:
            dayCounter = 1
    return weekdayAverage, weekendAverage


def makePlot(weekday, weekend):
    xday = [x+1 for x in range(len(weekday))]
    xend = [x+1 for x in range(len(weekend))]
    fig, axs = plt.subplots(2)
    axs[0].set_title("Weekday")
    axs[0].plot(xday,weekday)
    axs[1].set_title("Weekend")
    axs[1].plot(xend,weekend)
    plt.tight_layout()
    plt.show()
