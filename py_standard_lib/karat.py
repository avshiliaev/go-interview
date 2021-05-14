"""
We have a bin of doll parts in a factory. Each part goes to a doll with a specific, unique name. Each part will be
described by a string, with the name of the doll and the part name separated by an underscore, like "Mary_arm".

All dolls are made of the same types of parts, and we have a list of all of the parts that form a complete doll. Given
a list of available parts, return a list of doll names for which we will be able to create at least one complete doll.

all_parts_1 = "eyes,nose,mouth,ears"
all_parts_2 = "eyes,nose,mouth,ears,feet"

parts = [
    "Bette_feet",
    "Bette_eyes",
    "Colleen_nose",
    "Astrid_eyes",
    "Doug_eyes",
    "Bette_nose",
    "Astrid_nose",
    "Doug_mouth",
    "Bette_ears",
    "Bette_mouth",
    "Colleen_nose",
    "Colleen_arms",
    "Astrid_feet",
    "Colleen_nose",
    "Colleen_mouth",
    "Doug_nose",
    "Doug_ears",
    "Astrid_hands",
    "Doug_eyes" ]

# Expected output for parts list 1 (in any order):  ["Doug", "Bette"]
# Expected output for parts list 2 (in any order):  ["Bette"]

N: Number of items in parts
P: Number of parts in all_parts

"""

all_parts_1 = "eyes,nose,mouth,ears"
all_parts_2 = "eyes,nose,mouth,ears,feet"
parts = [
    "Bette_feet",
    "Bette_eyes",
    "Colleen_nose",
    "Astrid_eyes",
    "Doug_eyes",
    "Bette_nose",
    "Astrid_nose",
    "Doug_mouth",
    "Bette_ears",
    "Bette_mouth",
    "Colleen_nose",
    "Colleen_arms",
    "Astrid_feet",
    "Colleen_nose",
    "Colleen_mouth",
    "Doug_nose",
    "Doug_ears",
    "Astrid_hands",
    "Doug_eyes"]


def run():
    parts_dict = {}
    for doll_part in parts:
        doll_part_split = doll_part.split("_")
        parts_dict[doll_part_split[0]] = parts_dict.get(doll_part_split[0], set())
        parts_dict[doll_part_split[0]].add(doll_part_split[1])

    parts_required_one = set(all_parts_1.split(","))
    parts_required_two = set(all_parts_2.split(","))

    result_one = []
    result_two = []
    for k, v in parts_dict.items():
        if parts_required_one.issubset(v):
            result_one.append(k)
        if parts_required_two.issubset(v):
            result_two.append(k)

    print(result_one)
    print(result_two)


if __name__ == '__main__':
    run()
