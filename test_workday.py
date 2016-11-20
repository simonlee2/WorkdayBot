import workday as Workday
import datetime
from unittest import TestCase

class WorkdayTest(TestCase):

    def end_date(self, start_date, days):
        return Workday.workday_helper(start_date, days)

    def test_one_day(self):
        self.assertEqual(
            datetime.date(2017, 1, 4), 
            self.end_date('2017-01-03', 1)
        )

    def test_over_weekend(self):
        self.assertEqual(
            datetime.date(2017, 1, 10), 
            self.end_date('2017-1-3', 5)
        )

    def test_start_on_off(self):
        self.assertEqual(
            datetime.date(2017, 1, 9), 
            self.end_date('2017-1-2', 5)
        )

    def test_start_on_weekend(self):
        self.assertEqual(
            datetime.date(2017, 1, 13), 
            self.end_date('2017-1-8', 5)
        )

    def test_over_working_weekend(self):
        self.assertEqual(
            datetime.date(2017, 2, 20), 
            self.end_date('2017-2-16', 3)
        )

    def test_start_1day_before_working_weekend(self):
        self.assertEqual(
            datetime.date(2017, 2, 21), 
            self.end_date('2017-2-17', 3)
        )

    def test_start_on_working_weekend(self):
        self.assertEqual(
            datetime.date(2017, 2, 20),
            self.end_date('2017-2-18', 1)
        )

    def test_start_on_working_weekend_5days(self):
        self.assertEqual(
            datetime.date(2017, 2, 24),
            self.end_date('2017-2-18', 5)
        )

    def test_end_on_working_weekend(self):
        self.assertEqual(
            datetime.date(2017, 2, 18),
            self.end_date('2017-2-13', 5)
        )

    def test_long_workdays(self):
        self.assertEqual(
            datetime.date(2017, 6, 6),
            self.end_date('2017-4-28', 26)
        )

    def test_fall_season(self):
        self.assertEqual(
            datetime.date(2017, 10, 11),
            self.end_date('2017-9-28', 7)
        )

    def test_last_day(self):
        self.assertEqual(
            datetime.date(2017, 12, 29),
            self.end_date('2017-12-25', 20)
        )
