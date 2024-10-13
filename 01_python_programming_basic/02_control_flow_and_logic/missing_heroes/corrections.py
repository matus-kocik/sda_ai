from data import movies as m
from pprint import pprint

# You can use the `movies` array here
# Please write every correction and modification of the data to this file by updating the `movies` array

# WRITE YOUR CODE HERE

# pprint(m)

for movie in m:
    # print(movie["title"] + " - " + movie["director"])
    if movie["director"] == "" or movie["director"] == "N/A":
        # print(f"{movie["id"]}: {movie["title"]} - {movie["director"]}")
        movie["director"] = "Martin Scorsese"
        # print(f"{movie["id"]}: {movie["title"]} - {movie["director"]}")

# for i in movie:
#     if movie["director"] == "" or movie["director"] == "N/A":
#         print(f"{movie["id"]}: {movie["title"]} - {movie["director"]}")


for movie in m:
    if movie["year"] < 1500:
        # print(f"{movie["id"]}: {movie["title"]} - {movie["year"]}")
        movie["year"] = 1900
        # print(f"{movie["id"]}: {movie["title"]} - {movie["year"]}")

for movie in m:
    if "Leonardo da Vinci" in movie["actors"]:
        #print(f"{movie["id"]}: {movie["title"]} - {movie["actors"]}")
        movie["actors"].remove("Leonardo da Vinci")
        movie["actors"].append("Leonardo DiCaprio")

for movie in m:
    # print(f"{movie["id"]}: {movie["title"]} - {movie["genres"]}")
    if "" in movie["genres"]:
        # print(f"{movie["id"]}: {movie["title"]} - {movie["genres"]}")
        movie["genres"].remove("")
        movie["genres"].append("Drama")
        # print(f"{movie["id"]}: {movie["title"]} - {movie["genres"]}")

#pprint(m)

allTheActors = []
for movie in m:
    for actor in movie["actors"]:
        allTheActors.append(actor)
        #print(actor)
        #print(allTheActors)

setAllTheActors = set(allTheActors)

print(len(allTheActors))
print(len(setAllTheActors))
