
ingall = {}
ingredient_lines = []
allergen_lines = []
all_ingredients = set()
all_allergens = set()
done_ingredients = set()
with open("day21.txt", "r") as f:
    for line in f:
        ing, all = line.strip().split(" (contains ")
        ing = set(ing.split())
        ingredient_lines.append(ing)
        all = set([x.strip() for x in all.strip(")").split(',')])
        allergen_lines.append(all)
        # print(ing, all)

        for a in all:
            if a not in ingall:
                ingall[a] = ing
            else:
                ingall[a] = ingall[a].intersection(ing)

            if len(ingall[a]) == 1:
                done_ingredients = done_ingredients.union(ingall[a])

        all_allergens = all_allergens.union(all)
        all_ingredients = all_ingredients.union(ing)
        # print(ingall, "\n", done_ingredients, "\n")

for k, v in ingall.items():
    if len(v) > 1:
        ingall[k] = v - done_ingredients
        if len(ingall[k]) == 1:
            done_ingredients = done_ingredients.union(ingall[k])

# print("ingall: ", ingall, "\ndone_i: ", done_ingredients, "\n")

possibilities = set()
for k, v in ingall.items():
    possibilities = possibilities.union(v)

notpossible = all_ingredients - possibilities
counter = 0
for il in ingredient_lines:
    counter += len(il.intersection(notpossible))

print(counter)