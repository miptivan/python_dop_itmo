from dataclasses import dataclass
from enum import Enum, auto
from typing import List


def pr_list_of_days(f):
    def wrapper(*args, **kwargs):
        for day in f(*args):
            print(day.day, day.comfort)
        return f(*args, **kwargs)

    return wrapper


class Cloudiness(Enum):
    rainy = auto()
    cloudy = auto()
    sunny = auto()


@dataclass
class DayForecast:
    day: int
    cloudiness: Cloudiness
    wind: float
    temperature: float


@dataclass
class PicnicDay:
    day: int
    comfort: int


@pr_list_of_days
def picnic_planner(weather_list: List[DayForecast]) -> List[PicnicDay]:
    good_days = []
    for day in weather_list:
        if day.cloudiness == Cloudiness.sunny:
            comfort = day.temperature - day.wind * 1.5 + 5
        else:
            comfort = day.temperature - day.wind * 1.5
        if comfort >= 15 and day.cloudiness != 'rainy':
            good_days.append(PicnicDay(day=day.day, comfort=int(round(comfort))))
    return list(sorted(good_days, key=lambda day: day.comfort, reverse=True))


if __name__ == "__main__":
    weather = [DayForecast(day=1, cloudiness=Cloudiness.rainy, wind=3, temperature=17),
               DayForecast(day=2, cloudiness=Cloudiness.sunny, wind=7, temperature=33),
               DayForecast(day=3, cloudiness=Cloudiness.sunny, wind=1, temperature=21),
               DayForecast(day=4, cloudiness=Cloudiness.cloudy, wind=8, temperature=22),
               DayForecast(day=5, cloudiness=Cloudiness.rainy, wind=2, temperature=12),
               DayForecast(day=6, cloudiness=Cloudiness.cloudy, wind=30, temperature=3),
               DayForecast(day=7, cloudiness=Cloudiness.sunny, wind=2, temperature=12),
               DayForecast(day=8, cloudiness=Cloudiness.sunny, wind=1, temperature=15)]

    print(picnic_planner(weather))
