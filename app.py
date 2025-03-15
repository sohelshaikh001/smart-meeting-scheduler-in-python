
# Smart Meeting Scheduler

from datetime import datetime
import calendar

class Scheduler:
    def __init__(self):
        self.hours = range(9, 18)
        self.holidays = {"2025-03-23", "2025-04-10"}
        self.meetings = {}

    def is_working_day(self, date):
        return date.weekday() < 5 and date.strftime("%Y-%m-%d") not in self.holidays

    def book(self, user, date_str, start, end):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if not self.is_working_day(date) or start not in self.hours or end not in self.hours:
            return "Invalid time or non-working day."
        self.meetings.setdefault(user, {}).setdefault(date_str, [])
        if any(s < end and start < e for s, e in self.meetings[user][date_str]):
            return "Slot unavailable."
        self.meetings[user][date_str].append((start, end))
        return "Meeting scheduled."

    def available_slots(self, user, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if not self.is_working_day(date): return "Non-working day."
        booked = sorted(self.meetings.get(user, {}).get(date_str, []))
        slots, start = [], 9
        for s, e in booked:
            if start < s: slots.append(f"{start}:00 - {s}:00")
            start = e
        if start < 17: slots.append(f"{start}:00 - 17:00")
        return slots or "No available slots."

    def view_meetings(self, user, date_str):
        return self.meetings.get(user, {}).get(date_str, "No meetings.")


s = Scheduler()
print(s.book("Sohel", "2025-03-18", 10, 11))
print(s.available_slots("Mr.shaikh", "2025-04-20"))
print(s.view_meetings("Sohel", "2025-03-18"))
