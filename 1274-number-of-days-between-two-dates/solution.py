class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeapYear(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        def dateToDays(date_str):
            year, month, day = map(int, date_str.split('-'))
            days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            total_days = 0

            # Add days for full years before the given year
            for y in range(1971, year):  # Assuming 1971 as reference
                total_days += 366 if isLeapYear(y) else 365

            # Add days for full months before the given month in the current year
            for m in range(1, month):
                total_days += days_in_month[m]
                if m == 2 and isLeapYear(year):
                    total_days += 1

            # Add the days of the current month
            total_days += day
            return total_days

        return abs(dateToDays(date1) - dateToDays(date2))

