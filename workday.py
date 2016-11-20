import pandas as pd
import datetime
from pandas.tseries.offsets import CustomBusinessDay
import calendars

def workday(start_date, days, calendars):
    holidays, working_weekends = calendars.holidays_and_working_weekends(calendars.start_year)
    # Get all custom business days in the year taking holidays into account
    offset = CustomBusinessDay(holidays=holidays)
    end_date = datetime.date(calendars.end_year, 12, 31)
    index = pd.date_range(start_date, end_date, freq=offset)

    # Add working weekends
    index_working_weekends = pd.DatetimeIndex(working_weekends)
    custom_business_day = index.union(index_working_weekends)

    # Find start date in the array
    df = pd.DataFrame(custom_business_day.date, columns=['Date'], index=range(len(custom_business_day)))
    date = df['Date']
    found_index = date[date > start_date].head(1).index
    # Return the n-th date after start date

    end_index = found_index + days - 1
    if end_index >= len(date):
        end_index = date.index[-1:]

    end_date = df.iloc[end_index]
    return end_date["Date"][end_date.index[0]]

def workday_helper(start_date_string, days):
    year, month, day = map(int, start_date_string.split('-'))
    cal = calendars.Calendars(year)
    start_date = datetime.date(year, month, day)
    end_date =  workday(start_date, days, cal)
    return end_date
