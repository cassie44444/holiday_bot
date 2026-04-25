from datetime import date
import holidays

def get_holidays_for_date(day: date, country: str = "RU") -> list[str]:
    """
    Возвращает список праздников для заданной даты и страны.
    Если праздников нет, возвращает пустой список.
    """
    try:
        country_holidays = holidays.country_holidays(country)
        if day in country_holidays:
            return [country_holidays[day]]
    except Exception:
        return []
    return []