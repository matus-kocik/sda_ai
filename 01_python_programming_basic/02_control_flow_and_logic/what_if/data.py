# WRITE YOUR CODE HERE

from favourite_movies import favourite_movies as fm

for movie in fm:
    print(f"{movie['title']}")


print(50 * "-")

i = 0
while i < len(fm):
    print(f"{fm[i]['title']}")
    i += 1

print(50 * "-")

total_rate = 0
i = 0
while i < len(fm):
    total_rate += fm[i]["rating"]
    i += 1

average_rate = total_rate / len(fm)
print(average_rate)

print(50 * "-")


newest_movie = fm[0]
for movie in fm:
    if movie["year"] > newest_movie["year"]:
        newest_movie = movie

print(newest_movie["title"])

print(50 * "-")


# for movie in fm:
#     print(f"{movie['title']} stars: {', '.join(movie['stars'])}")


for movie in fm:
    print(f"{movie['title']}, stars: {movie["stars"][0]}, {movie["stars"][1]}, {movie["stars"][2]}")