import datetime

def time():
    now = datetime.now()
    t = "bây giờ là %d giờ %d phút" %(now.hour,now.minute)
    return t
def date():
    now = datetime.now()
    d = "hôm nay là ngày %d tháng %d năm %d" %(now.day,now.month,now.year)
    return d