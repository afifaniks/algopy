def timeConversion(s):
    code = s[-2:]
    time = s[:-2]

    split = time.split(":")

    hour = int(split[0])
    if code.upper() == "AM":
        if hour == 12:
            res = "00"
        elif hour < 12:
            res = "0" + str(hour)
        else:
            res = str(hour)

        return res + ":" + str(split[1]) + ":" + str(split[2])

    elif code.upper() == "PM":
        if hour < 12:
            hour = hour + 12

    return str(hour) + ":" + str(split[1]) + ":" + str(split[2])


print(timeConversion('04:59:59AM'))