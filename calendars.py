import requests
import pandas as pd
import datetime

class Calendar(object):
    def __init__(self, year):
        self.year = year
        self.base_url_format = "http://www.api.cloud.taipei.gov.tw/CSCP_API/ofc/{0}/info"
        json = self.get_calendar_json()
        pairs = [(entry["stateCalendar"], entry["category_code"]) for entry in json]
        self.holidays = [x[0] for x in pairs if (x[1] != '2' and x[1] != '5')]
        self.working_weekends = [x[0] for x in pairs if x[1] == '5']

    def get_calendar_json_url(self):
        return self.base_url_format.format(self.year)

    def get_calendar_json(self):
        url = self.get_calendar_json_url()
        response = requests.request("GET", url)
        return response.json()

class Calendars(object):
    def __init__(self, start_year):
        self.start_year = start_year
        self.end_year = start_year + 1
        self.holidays = []
        self.working_weekends = []

    def holidays_and_working_weekends(self, year):
        cal = Calendar(year)
        holidays = cal.holidays
        working_weekends = cal.working_weekends
        if len(holidays) == 0 and len(working_weekends) == 0:
            self.end_year = year - 1
            return (holidays, working_weekends)

        next_holidays, next_working_weekends = self.holidays_and_working_weekends(year + 1)
        self.holidays = holidays + next_holidays
        self.working_weekends = working_weekends + next_working_weekends
        return (self.holidays, self.working_weekends)
