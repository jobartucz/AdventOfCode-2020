from itertools import islice

class node:

    def __init__(self, num, lines):
        self.num = num
        self.lines = lines

        # sides
        self.sides = {}
        self.sides['left'] = set()
        self.sides['right'] = set()
        self.sides['top'] = set()
        self.sides['bottom'] = set()

        # neighbors
        self.neighbors = {}
        self.neighbors['left'] = None
        self.neighbors['right'] = None
        self.neighbors['top'] = None
        self.neighbors['bottom'] = None


        for h, i in enumerate(lines[0]):
            if i == '#':
                self.sides['top'].add(h)

        for h, i in enumerate(lines[9]):
            if i == '#':
                self.sides['bottom'].add(h)

        for i, l in enumerate(lines):
            if l[0] == '#':
                self.sides['left'].add(i)
            if l[9] == '#':
                self.sides['right'].add(i)

    def flip(self, line):
        newset = set()
        for i in line:
            newset.add(9-i)
        return newset

    def flip_ud(self):
        self.sides['left'] = self.flip(self.sides['left'])
        self.sides['right'] = self.flip(self.sides['right'])
        tmp = self.sides['top']
        self.sides['top'] = self.sides['bottom']
        self.sides['bottom'] = tmp

        tmp = self.neighbors['top']
        self.neighbors['top'] = self.neighbors['bottom']
        self.neighbors['bottom'] = tmp
        if self.neighbors['left'] and self.sides['left'] != self.neighbors['left'].sides['right']:
            self.neighbors['left'].flip_ud()
        if self.neighbors['right'] and self.sides['right'] != self.neighbors['right'].sides['left']:
            self.neighbors['right'].flip_ud()
        if self.neighbors['top'] and self.sides['top'] != self.neighbors['top'].sides['bottom']:
            self.neighbors['top'].flip_ud()
        if self.neighbors['bottom'] and self.sides['bottom'] != self.neighbors['bottom'].sides['top']:
            self.neighbors['bottom'].flip_ud()

    def flip_lr(self, frm = None):
        self.sides['top'] = self.flip(self.sides['top'])
        self.sides['bottom'] = self.flip(self.sides['bottom'])
        tmp = self.sides['left']
        self.sides['left'] = self.sides['right']
        self.sides['right'] = tmp

        tmp = self.neighbors['right']
        self.neighbors['right'] = self.neighbors['left']
        self.neighbors['left'] = tmp
        if self.neighbors['left'] and self.sides['left'] != self.neighbors['left'].sides['right']:
            self.neighbors['left'].flip_lr()
        if self.neighbors['right'] and self.sides['right'] != self.neighbors['right'].sides['left']:
            self.neighbors['right'].flip_lr()
        if self.neighbors['top'] and self.sides['top'] != self.neighbors['top'].sides['bottom']:
            self.neighbors['top'].flip_lr()
        if self.neighbors['bottom'] and self.sides['bottom'] != self.neighbors['bottom'].sides['top']:
            self.neighbors['bottom'].flip_lr()

    def rot_r(self):
        tmp = self.sides['top']
        self.sides['top'] = self.flip(self.sides['left'])
        self.sides['left'] = self.sides['bottom']
        self.sides['bottom'] = self.flip(self.sides['right'])
        self.sides['right'] = tmp


        tmp = self.neighbors['top']
        self.neighbors['top'] = self.neighbors['left']
        self.neighbors['left'] = self.neighbors['bottom']
        self.neighbors['bottom'] = self.neighbors['right']
        self.neighbors['right'] = tmp
        if self.neighbors['left'] and self.sides['left'] != self.neighbors['left'].sides['right']:
            self.neighbors['left'].rot_r()
        if self.neighbors['right'] and self.sides['right'] != self.neighbors['right'].sides['left']:
            self.neighbors['right'].rot_r()
        if self.neighbors['top'] and self.sides['top'] != self.neighbors['top'].sides['bottom']:
            self.neighbors['top'].rot_r()
        if self.neighbors['bottom'] and self.sides['bottom'] != self.neighbors['bottom'].sides['top']:
            self.neighbors['bottom'].rot_r()

    def rot_l(self):
        tmp = self.sides['top']
        self.sides['top'] = self.sides['right']
        self.sides['right'] = self.flip(self.sides['bottom'])
        self.sides['bottom'] = self.sides['left']
        self.sides['left'] = self.flip(tmp)


        tmp = self.neighbors['top']
        self.neighbors['top'] = self.neighbors['right']
        self.neighbors['right'] = self.neighbors['bottom']
        self.neighbors['bottom'] = self.neighbors['left']
        self.neighbors['left'] = tmp

        if self.neighbors['left'] and self.sides['left'] != self.neighbors['left'].sides['right']:
            self.neighbors['left'].rot_l()
        if self.neighbors['right'] and self.sides['right'] != self.neighbors['right'].sides['left']:
            self.neighbors['right'].rot_l()
        if self.neighbors['top'] and self.sides['top'] != self.neighbors['top'].sides['bottom']:
            self.neighbors['top'].rot_l()
        if self.neighbors['bottom'] and self.sides['bottom'] != self.neighbors['bottom'].sides['top']:
            self.neighbors['bottom'].rot_l()

    def __str__(self):
        s = "\nNUM: " + str(self.num) + "\n"
        s += f"top: {self.sides['top']}\n"
        s += f"right: {self.sides['right']}\n"
        s += f"bottom: {self.sides['bottom']}\n"
        s += f"left: {self.sides['left']}\n"
        s += "\n"
        if self.neighbors['top']:
            s += f"n top: {self.neighbors['top'].num}\n"
        else:
            s += f"n top: None\n"
        if self.neighbors['right']:
            s += f"n right: {self.neighbors['right'].num}\n"
        else:
            s += f"n right: None\n"
        if self.neighbors['bottom']:
            s += f"n bottom: {self.neighbors['bottom'].num}\n"
        else:
            s += f"n bottom: None\n"
        if self.neighbors['left']:
            s += f"n left: {self.neighbors['left'].num}\n"
        else:
            s += f"n left: None\n"
        return s

nodes = []
with open("day20.txt", "r") as f:
    while True:
        next_n_lines = list(islice(f, 12))
        if not next_n_lines:
            break
        l = next_n_lines.pop(0)
        title, num = l.split()
        num = num[:-1]
        lines = []
        for i in range(10):
            lines.append(next_n_lines.pop(0).strip())
        nodes.append(node(num, lines))

for i, n in enumerate(nodes):
    for j in range(i+1, len(nodes)):
        found = False
        for s in n.sides:
            if n.neighbors[s] == None:
                for t in n.sides:
                    if nodes[j].neighbors[t] == None:
                        if n.sides[s] == nodes[j].sides[t]:
                            found = True

                            # if they already match up
                            if (s == 'top' and t == 'bottom') or (s == 'bottom' and t == 'top') or (s == 'right' and t == 'left') or (s == 'left' and t == 'right'):
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors[t] = n

                            # rotate right to match
                            elif (s == 'top' and t == 'right'):
                                nodes[j].rot_r()
                                nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['bottom'] = n
                            elif s == 'right' and t == 'bottom':
                                nodes[j].rot_r()
                                # nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['left'] = n
                            elif s == 'bottom' and t == 'left':
                                nodes[j].rot_r()
                                nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['top'] = n
                            elif s == 'left' and t == 'top':
                                nodes[j].rot_r()
                                # nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['right'] = n

                            # rotate left to match
                            elif (s == 'top' and t == 'left'):
                                nodes[j].rot_l()
                                # nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['bottom'] = n
                            elif s == 'left' and t == 'bottom':
                                nodes[j].rot_l()
                                nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['right'] = n
                            elif s == 'bottom' and t == 'right':
                                nodes[j].rot_l()
                                # nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['top'] = n
                            elif s == 'right' and t == 'top':
                                nodes[j].rot_l()
                                nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['left'] = n

                            # flip to match
                            elif s == 'left' and t == 'left':
                                nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['right'] = n
                            elif s == 'right' and t == 'right':
                                nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['left'] = n
                            elif s == 'top' and t == 'top':
                                nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['bottom'] = n
                            elif s == 'bottom' and t == 'bottom':
                                nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['top'] = n

                            if found == True:
                                break
                if found == True:
                    break

        n.flip_lr()
        n.flip_ud()
        for s in n.sides:
            if n.neighbors[s] == None:
                for t in n.sides:
                    if nodes[j].neighbors[t] == None:
                        if n.sides[s] == nodes[j].sides[t]:
                            found = True
                            if (s == 'top' and t == 'bottom') or (s == 'bottom' and t == 'top') or (s == 'right' and t == 'left') or (s == 'left' and t == 'right'):
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors[t] = n
                            elif (s == 'top' and t == 'right'):
                                nodes[j].rot_r()
                                nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['bottom'] = n
                            elif s == 'right' and t == 'bottom':
                                nodes[j].rot_r()
                                # nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['left'] = n
                            elif s == 'bottom' and t == 'left':
                                nodes[j].rot_r()
                                nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['top'] = n
                            elif s == 'left' and t == 'top':
                                nodes[j].rot_r()
                                # nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['right'] = n

                            elif (s == 'top' and t == 'left'):
                                nodes[j].rot_l()
                                # nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['bottom'] = n
                            elif s == 'left' and t == 'bottom':
                                nodes[j].rot_l()
                                nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['right'] = n
                            elif s == 'bottom' and t == 'right':
                                nodes[j].rot_l()
                                # nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['top'] = n
                            elif s == 'right' and t == 'top':
                                nodes[j].rot_l()
                                nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['left'] = n

                            # flip to match
                            elif s == 'left' and t == 'left':
                                nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['right'] = n
                            elif s == 'right' and t == 'right':
                                nodes[j].flip_lr()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['left'] = n
                            elif s == 'top' and t == 'top':
                                nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['bottom'] = n
                            elif s == 'bottom' and t == 'bottom':
                                nodes[j].flip_ud()
                                n.neighbors[s] = nodes[j]
                                nodes[j].neighbors['top'] = n

                            if found == True:
                                break
                if found == True:
                    break

for n in nodes:
    if int(n.num) == 1427:
        n.flip_ud()
        break

product = 1
for n in nodes:
    if n.neighbors['top'] == None:
        if n.neighbors['left'] == None or n.neighbors['right'] == None:
            print(n.num)
            product *= int(n.num)
    if n.neighbors['bottom'] == None:
        if n.neighbors['left'] == None or n.neighbors['right'] == None:
            print(n.num)
            product *= int(n.num)

print(product)

