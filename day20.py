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
                self.top.add(h)

        for h, i in enumerate(lines[9]):
            if i == '#':
                self.bottom.add(h)

        for i, l in enumerate(lines):
            if l[0] == '#':
                self.left.add(i)
            if l[9] == '#':
                self.right.add(i)

    def flip(line):
        newset = set()
        for i in line:
            newset.add(9-i)
        return newset

    def flip_ud(self, from = None):
        self.sides['left'] = self.flip(self.sides['left'])
        self.sides['right'] = self.flip(self.sides['right'])
        tmp = self.sides['top']
        self.sides['top'] = self.sides['bottom']
        self.sides['bottom'] = tmp

        tmp = self.neighbors['top']
        self.neighbors['top'] = self.neighbors['bottom']
        self.neighbors['bottom'] = tmp
        self.neighbors['left'].flip_ud()
        self.neighbors['right'].flip_ud()


    def flip_lr(self, from = None):
        self.sides['top'] = self.flip(self.sides['top'])
        self.sides['bottom'] = self.flip(self.sides['bottom'])
        tmp = self.sides['left']
        self.sides['left'] = self.sides['right']
        self.sides['right'] = tmp

        tmp = self.neighbors['right']
        self.neighbors['right'] = self.neighbors['left']
        self.neighbors['left'] = tmp
        self.neighbors['top'].flip_lr()
        self.neighbors['bottom'].flip_lr()

    def rot_r(self, from = None):
        tmp = self.sides['top']
        self.sides['top'] = self.sides['left']
        self.sides['left'] = self.sides['bottom']
        self.sides['bottom'] = self.sides['right']
        self.sides['right'] = tmp

        tmp = self.neighbors['top']
        self.neighbors['top'] = self.neighbors['left']
        self.neighbors['left'] = self.neighbors['bottom']
        self.neighbors['bottom'] = self.neighbors['right']
        self.neighbors['right'] = tmp

    def rot_l(self, from = None):
        tmp = self.sides['top']
        self.sides['top'] = self.sides['right']
        self.sides['right'] = self.sides['bottom']
        self.sides['bottom'] = self.sides['left']
        self.sides['left'] = tmp


        tmp = self.neighbors['top']
        self.neighbors['top'] = self.neighbors['right']
        self.neighbors['right'] = self.neighbors['bottom']
        self.neighbors['bottom'] = self.neighbors['left']
        self.neighbors['left'] = tmp

    def __str__(self):
        s = "\nNUM: " + str(self.num) + "\n"
        s += f"top: {self.sides['top']}\n"
        s += f"right: {self.sides['right']}\n"
        s += f"bottom: {self.sides['bottom']}\n"
        s += f"left: {self.sides['left']}\n"
        return s

nodes = []
with open("day20test.txt", "r") as f:
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

for n in nodes:
    for o in nodes:
        if n.