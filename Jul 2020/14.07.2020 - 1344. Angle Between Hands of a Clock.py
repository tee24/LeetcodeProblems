def clock_angle(mins, hour):
    min_percentage = mins/60
    hour_percentage = (hour+min_percentage)/12

    angle = abs(min_percentage-hour_percentage)

    return min(360*angle, 360-360*angle)

#Space, Time = O(1)