# WRITE YOUR CODE HERE

from favourite_movies import favourite_movies as fm
from pprint import pprint

# pprint(fm)
print(50 * "-")

print(fm[0]["title"])
print(fm[1]["year"])
print(fm[2]["rating"])
print(fm[3]["description"])

print(50*"-")

print(f"The title of the first movie is: {fm[0]["title"]}")
print(f"The year of the second movie is: {fm[1]["year"]}")
print(f"The rating of the third movie is: {fm[2]["rating"]}")
print(f"The description of the fourth movie is: {fm[3]["description"]}")

print(50*"-")

fm[0]["directors"] = []
fm[1]["directors"] = []
fm[2]["directors"] = []
fm[3]["directors"] = []

fm[0]["directors"].append("Frank Darabont")
fm[1]["directors"].append("Francis Ford Coppola")
fm[2]["directors"].append("Christopher Nolan")  
fm[3]["directors"].append("Quentin Tarantino")

fm[0]["writers"] = []
fm[1]["writers"] = []
fm[2]["writers"] = []
fm[3]["writers"] = []

fm[0]["writers"].append("Stephen King")
fm[1]["writers"].append("Mario Puzo")
fm[2]["writers"].append("Christopher Nolan")
fm[3]["writers"].append("Quentin Tarantino")

fm[0]["actors"] = []
fm[1]["actors"] = []
fm[2]["actors"] = []
fm[3]["actors"] = []

fm[0]["actors"].extend(["Tim Robbins", "Morgan Freeman"])
fm[1]["actors"].extend(["Marlon Brando", "Al Pacino"])
fm[2]["actors"].extend(["Christian Bale", "Heath Ledger"])
fm[3]["actors"].extend(["John Travolta", "Uma Thurman"])

fm[0]["genres"] = []
fm[1]["genres"] = []
fm[2]["genres"] = []
fm[3]["genres"] = []

fm[0]["genres"].append("Drama")
fm[1]["genres"].append("Crime")
fm[2]["genres"].append("Action")
fm[3]["genres"].append("Crime")


print(f"The lead director of the first movie is: {fm[0]["directors"][0]}")
print(f"The lead writer of the second movie is: {fm[1]["writers"][0]}")
print(f"The lead star of the third movie is: {fm[2]["actors"][0]}")
print(f"The main genre of the fourth movie is: {fm[3]["genres"][0]}")

print(50 * "-")

averageRating = (fm[0]["rating"] + fm[1]["rating"] + fm[2]["rating"] + fm[3]["rating"]) / len(fm)
print(averageRating)

print(50 * "-")

current_year = 2024
average_age = current_year - (fm[0]["year"] + fm[1]["year"] + fm[2]["year"] + fm[3]["year"]) / len(fm)

print(average_age)


pprint(fm)