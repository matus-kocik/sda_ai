from best_selling_albums import best_selling_albums as bsa
from fav_books import favourite_books as fb
from fav_movies import favourite_movies as fm

from pprint import pprint
from datetime import datetime


def averageAge(array_of_objects, year=datetime.now().year):
    return round(
        year - sum(obj["year"] for obj in array_of_objects) / len(array_of_objects)
    )


""" pprint(averageAge(fb))
pprint(averageAge(fm, 2023))
pprint(averageAge(bsa)) """

pprint(50 * "-")


def average(array_of_objects, key):
    # only first check - predpokladame ze vsetky objekty maju rovnake kluce
    return (
        sum(obj[key] for obj in array_of_objects) / len(array_of_objects)
        if key in array_of_objects[0]
        else None
    )


""" pprint(average(fb, "year"))
pprint(average(fm, "rating"))
pprint(average(bsa, "sale")) """

pprint(50 * "-")


def latest_or_oldest(array_of_objects, latest=True):
    # True = latest, False = oldest
    year = [datetime.now().year - obj["year"] for obj in array_of_objects]
    return min(year) if latest else max(year)


""" pprint(latest_or_oldest(fb, True))
pprint(latest_or_oldest(fm, True))
pprint(latest_or_oldest(bsa, True))
pprint(latest_or_oldest(fb, False))
pprint(latest_or_oldest(fm, False))
pprint(latest_or_oldest(bsa, False)) """

pprint(50 * "-")
