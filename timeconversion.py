def timeConversion(s):
    #if s[8] == "P":
    #   hours = int(s[0] + s[1]) + 12
    #else:
    #    hours = int(s[0] + s[1])
    #if hours < 10:
    #    time = "0" + str(hours) + s[2:8]
    #else:
    #    time = str(hours) + s[2:8]
    #return time
    if s[8] == "P" and (int(s[0] + s[1]) != 12):
            hours = str(int(s[0] + s[1]) + 12)
    elif int(s[0] + s[1]) < 10:
            hours = "0" + s[1]
    elif s[8] == "A" and (int(s[0] + s[1]) == 12):
            hours = "00"
    else:
            hours = s[0] + s[1]
    return hours + s[2:8]

s = raw_input().strip()
print timeConversion(s)



