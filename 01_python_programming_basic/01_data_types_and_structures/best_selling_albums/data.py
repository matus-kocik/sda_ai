from bestSellingAlbums import bestSellingAlbums as bsa
from pprint import pprint

# WRITE YOUR CODE HERE

# print(bsa)

average_sale = sum([album["sale"] for album in bsa]) / len(bsa)

print(f"Average sale of the best selling albums is: {average_sale}")


print(50 * "*")

current_year = 2024
average_age = round(sum([current_year - album["year"] for album in bsa]) / len(bsa))
# print(average_age)

print(f"Average age of the best selling albums is: {average_age} years")


print(50 * "*")

album_year = [current_year - album["year"] for album in bsa]
# print(album_year)
min_album_year = min(album_year)
max_album_year = max(album_year)
print(f"Min album year: {min_album_year}")
print(f"Max album year: {max_album_year}")
# vyuzijem index() na zistenie indexu najnovsieho a najstarsieho albumu

newest_album = bsa[album_year.index(min_album_year)]
oldest_album = bsa[album_year.index(max_album_year)]

print(f"Newest album: {newest_album['title']} by {newest_album['artist']}")
print(f"Oldest album: {oldest_album['title']} by {oldest_album['artist']}")

print(50 * "*")

album_eagles = {}
is_both_soft_rock = True
album_eagles_list = [album for album in bsa if album["artist"] == "Eagles"]
album_eagles["sales"] = sum([album["sale"] for album in album_eagles_list])

for album in album_eagles_list:
    if "soft rock" not in album["genres"]:
        is_both_soft_rock = False

album_eagles["is_both_soft_rock"] = is_both_soft_rock

print(album_eagles)

print(50 * "*")

bsa1 = bsa.copy()
for album in bsa1:
    album["i_like_it"] = (
        True
        if album["artist"] == "Eagles" and album["title"] == "Hotel California"
        else False
    )

pprint(bsa1)
