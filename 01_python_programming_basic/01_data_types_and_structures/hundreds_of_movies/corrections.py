from data import movies as m
from pprint import pprint

# You can use the `movies` array here
# Please write every correction and modification of the data to this file by updating the `movies` array

# WRITE YOUR CODE HERE

# print(m[0])
m[1 - 1][
    "plot"
] = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
# print(m[0])

m[22 - 1][
    "plot"
] = "ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
m[52 - 1][
    "plot"
] = "dolor sit amet  consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
m[53 - 1][
    "plot"
] = "sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
m[105 - 1][
    "plot"
] = "magna aliqua sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

# print(m[104])

print(50 * "-")

m[18 - 1]["year"] = 2019
# print(m[18-1])

m[27 - 1]["year"] = 2000
m[54 - 1]["year"] = 2020
m[81 - 1]["year"] = 1989
m[102 - 1]["year"] = 1996

print(50 * "-")

# pprint(m[2])

m[3 - 1]["actors"][0] = "John Doe"
m[13 - 1]["actors"][len(m[13 - 1]["actors"]) - 1] = "John Doe I"
m[35 - 1]["actors"][0] = "John Doe II"
m[66 - 1]["actors"][1] = "John Doe III"
m[144 - 1]["actors"][2] = "John Doe IV"

# pprint(m[35])

print(50 * "-")

m[8 - 1]["director"] = "Alice Doe"
# pprint(m[8-1])
m[31 - 1]["director"] = "Alice Doe I"
m[38 - 1]["director"] = "Alice Doe II"
m[64 - 1]["director"] = "Alice Doe III"
m[82 - 1]["director"] = "Alice Doe IV"

print(50 * "-")

m[96 - 1]["genres"] = ["Action"]
m[146 - 1]["genres"] = ["Action", "Adventure"]

# pprint(m[145])

print(50 * "-")

pprint(m[90 - 1])

m[90 - 1]["actors"].clear()
m[90 - 1]["actors"].extend(["Keanu Reeves", "Natalie Portman", "Hugo Weaving"])
m[90 - 1]["director"] = "Michael Bay"
m[90 - 1]["genres"] = ["Action", "Drama", "Thriller"]
m[90 - 1]["id"] = 90
m[90 - 1][
    "plot"
] = "lore ipsut sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
m[90 - 1]["runtime"] = 128
m[90 - 1]["title"] = "V for Vendetta"
m[90 - 1]["year"] = 2016

pprint(m[90 - 1])
# pprint(m[91-1])
# pprint(m[31-1])
