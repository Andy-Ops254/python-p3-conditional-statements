dog = "cuddly"

if dog == "thirsty":
    owner = "refill the water bowl."
elif dog == "hungry":
    owner = "Refill food bowl."
elif dog == "playfull":
    owner = "playng tug-of-war."
elif dog == "cuddly":
    owner = "snuggle"
else :
    owner = "reading newspaper"

age = 1
is_baby = 'baby' if age < 2 else 'not a baby'

#Dictionary mapping

dog = "cuddly"

dict_map = {
    "hungry" : "Refilling food bowl",
    "thirsty": "Refill water bowl",
    "playfull" : "Playing tug-of-war",
    "cuddly" : "snuggle",
}
owner = dict_map.get(dog, "Reading news paper.") # .get() sets the default value