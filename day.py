"""
This piece of code belongs to K.Phani Pavan.
My e-mail ID: kphanipavan@gmail.com
For queries cantact me.
"""
import calendar as cal
from datetime import date
import datetime as dt
dm = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
dml = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
wd = {0: "Monday", 1: "Tuesday", 2:"Wednesday", 3: "Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
dw = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}

def __get_day(wkDay, wkDayType, dat=date.today()):
    #dat=i()
    # print(dtDate, wkDay, wkDayType)
    if wkDayType.lower()=='next':
        add_Dt = dat - dt.timedelta(days=dat.weekday())
        if dat.weekday() < dw[wkDay.lower()]:
            z = 0
        else:
            z = 7
        Dt1 = add_Dt + dt.timedelta(days=z)
        #print(Dt1)
        Dt1 = Dt1 + dt.timedelta(days=dw[wkDay.lower()])
        print(Dt1, "in_n")
    elif wkDayType.lower()=='previous':
        add_Dt = dat - dt.timedelta(days=dat.weekday())

        if dat.weekday() < dw[wkDay.lower()]+1:
            z = 7
        else:
            z = 0
        Dt1 = add_Dt - dt.timedelta(days=z)
        #print(Dt1)
        Dt1 = Dt1 + dt.timedelta(days=dw[wkDay.lower()])
        print(Dt1, "in_p")
    elif wkDayType.lower() == 'previous_week':
        add_Dt = dat - dt.timedelta(days=dat.weekday())
        if dat.weekday() < dw[wkDay.lower()]:
            z = 7
        else:
            z = 7
        Dt1 = add_Dt - dt.timedelta(days=z)
        #print(Dt1)
        Dt1 = Dt1 + dt.timedelta(days=dw[wkDay.lower()])
        print(Dt1,"in_pw")
    elif wkDayType.lower() == 'next_week':
        add_Dt = dat + dt.timedelta(days=7)
        add_Dt = add_Dt - dt.timedelta(days=dat.weekday())

        if dat.weekday() < dw[wkDay.lower()]:
            z = 0
        else:
            z = 0
        Dt1 = add_Dt + dt.timedelta(days=z)
        #print(Dt1)
        Dt1 = Dt1 + dt.timedelta(days=dw[wkDay.lower()])
        print(Dt1,"in_nw")

def get_weekdate(wkDay, wkDayType, Dtdt=0):
    if Dtdt == 0:
        __get_day(wkDay, wkDayType)
    else:
        dat = Dtdt.split('-')
        dat=date(int(dat[0]), int(dat[1]), int(dat[2]))
        __get_day(wkDay, wkDayType, dat)


#get_date('Tuesday', 'next_week', '2020-3-24')