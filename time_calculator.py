"""Time Calculator"""

from typing import Optional, Tuple, Union

def day_of_week_convert(
    day_name: Optional[str] = None,
    day_number: Optional[int] = None) -> Optional[Union[str | int]]:
    """
    Convert between day of week string and number.

    Args:
        day_name (str, optional): Day of week name (e.g. 'monday').
        day_number (int, optional): Day of week number (1=Sunday .. 7=Saturday).

    Returns:
        int or str:
            - If given a day string, returns corresponding number.
            - If given a number, returns corresponding day string.
            - None if not found.
    """
    days = {
        "sunday": 1,
        "monday": 2,
        "tuesday": 3,
        "wednesday": 4,
        "thursday": 5,
        "friday": 6,
        "saturday": 7,
    }

    if day_name:
        return days.get(day_name.strip().lower())
    return next((k for k, v in days.items() if v == day_number), None)

def parse_time_12h(start: str) -> Tuple[int, int, str]:
    """Split a 12h formatted time string into hour, minute, and AM/PM."""
    time, am_pm = start.split()
    hour, minute = map(int, time.split(":"))
    return hour, minute, am_pm.upper()

def convert_to_minutes(hour: int, minute: int, am_pm: str) -> int:
    """Convert 12h formatted time into total minutes since midnight."""
    if am_pm == "PM":
        hour = (hour % 12) + 12
    else:
        hour = hour % 12
    return hour * 60 + minute

def minutes_to_12h(total_minutes: int) -> Tuple[int, int, str]:
    """Convert total minutes since midnight to 12h time format."""
    new_hour_24 = (total_minutes // 60) % 24
    new_minute = total_minutes % 60

    if new_hour_24 == 0:
        return 12, new_minute, "AM"
    if 1 <= new_hour_24 < 12:
        return new_hour_24, new_minute, "AM"
    if new_hour_24 == 12:
        return 12, new_minute, "PM"
    return new_hour_24 - 12, new_minute, "PM"

def format_days_passed(days_passed: int) -> str:
    """Return a string describing how many days have passed."""
    if days_passed == 0:
        return ""
    if days_passed == 1:
        return "(next day)"
    return f"({days_passed} days later)"

def calculate_new_day(start_day: str, days_passed: int) -> str:
    """Return the new day of week after adding days_passed."""
    start_day_number = day_of_week_convert(day_name=start_day)
    new_day_number = ((start_day_number - 1) + days_passed) % 7 + 1
    new_day_name = day_of_week_convert(day_number=new_day_number)
    return new_day_name.title()

def add_time(start: str, duration: str, day_of_week: Optional[str] = None) -> str:
    """
    Add a duration to a 12h formatted start time.

    Args:
        start (str): Start time, e.g. "3:30 PM".
        duration (str): Duration in hours:minutes, e.g. "2:12".
        day_of_week (str, optional): Starting day of the week.

    Returns:
        str: New time string with day and days passed if applicable.
    """
    start_hour, start_minute, am_pm = parse_time_12h(start)
    start_total_minutes = convert_to_minutes(start_hour, start_minute, am_pm)

    duration_hour, duration_minute = map(int, duration.split(":"))
    duration_total_minutes = duration_hour * 60 + duration_minute

    total_minutes = start_total_minutes + duration_total_minutes
    days_passed = total_minutes // (24 * 60)

    new_hour, new_minute, new_am_pm = minutes_to_12h(total_minutes)
    new_time_string = f"{new_hour}:{new_minute:02d} {new_am_pm}"

    days_passed_string = format_days_passed(days_passed)
    new_day_string = (
        calculate_new_day(day_of_week, days_passed) if day_of_week else ""
    )

    # Build final output
    parts = [new_time_string]
    if new_day_string:
        parts.append(new_day_string)
    if days_passed_string:
        parts.append(days_passed_string)

    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return f"{parts[0]}, {parts[1]}"
    return f"{parts[0]}, {parts[1]} {parts[2]}"
    

if __name__ == "__main__":
    # Demo runs
    examples = [
        ("3:00 PM", "3:10", None),
        ("11:30 AM", "2:32", "Monday"),
        ("11:43 AM", "00:20", "tuesday"),
        ("10:10 PM", "3:30", None),
        ("11:43 PM", "24:20", "friday"),
        ("6:30 PM", "205:12", "saturDAY"),
    ]

    for start, duration, day in examples:
        result = add_time(start, duration, day)
        print(f"{start} + {duration}" + (f" ({day})" if day else "") + f" → {result}")