class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date_object=datetime.date(year,month,day)
        return date_object.strftime('%A')
