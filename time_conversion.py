def timeConversion(s):
    hours = int(s[0:2])
    minutes = s[3:5]
    seconds = s[6:8]
    period = s[8:10]
    if period == "AM":
        if hours == 12:
            hours = 0
    else:
        if hours != 12:
            hours = hours + 12
    hours = f"{hours:02d}"
    return f"{hours}:{minutes}:{seconds}"
