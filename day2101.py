
ingall = {}
notingall = {}
ingredient_lines = []
all_ingredients = set()
with open("day21test.txt", "r") as f:
    for line in f:
        ing, all = line.strip().split(" (contains ")
        ing = ing.split()
        ingredient_lines.append(ing)
        all = set([x.strip() for x in all.strip(")").split(',')])
        print(ing, all)
        for i in ing:
            all_ingredients.add(i)
            if i not in ingall:
                ingall[i] = all
                notingall[i] = set()
            else:
                notingall[i] = notingall[i].union(ingall[i] ^ all)
                ingall[i] = ingall[i].intersection(all)
        for a in all:
            for i in all_ingredients:
                if i not in ing:
                    notingall[i].add(a)
                    ingall[i].discard(a)


        print(ingall)
        print(notingall)
        print()

nonallergens = []
for k, v in ingall.items():
    if len(v) == 0:
        nonallergens.append(k)

print(nonallergens)