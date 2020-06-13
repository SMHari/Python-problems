import datetime


def check_time(hr):
    if 6 <= hr < 18:
        print("Day time")
    else:
        print("Night")


if __name__ == '__main__':
    print("...Current time scenario...")
    nw = (datetime.datetime.now())
    check_time(nw.hour)
    n = input("Enter the time in the format as YYYY-MM-DD HH:MM:SS which u want to find ")
    time = datetime.datetime.strptime(n, "%Y-%m-%d %H:%M:%S")
    hr, mi = (time.hour, time.minute)
    check_time(hr)

