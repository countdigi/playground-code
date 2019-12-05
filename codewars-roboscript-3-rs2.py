import re

def tokenize(code):
    tokens = []

    for (command, paren_open, paren_close, number) in re.findall(r"(F|L|R)|(\()|(\))|([0-9]+)", code):
        if command:
            tokens.append(("command", command))

        elif paren_open:
            tokens.append(("paren_open", paren_open))

        elif paren_close:
            tokens.append(("paren_close", paren_close))

        elif number:
            tokens.append(("number", number))

        else:
            raise("Error in tokenize parsing code")

    return tokens


def parse(tokens):
    tree = []

    for t in tokens:
        if t[0] == "paren_open":
            tree.append(("subtree", parse(tokens)))

        elif t[0] == "paren_close":
            return tree

        else:
            tree.append(t)

    return tree


def build_command(tree):
    command = ""
    store = None

    for node in tree:
        if node[0] == "command":
            if store:
                command += store

            store = node[1]

        elif node[0] == "number":
            if store:
                command += store * int(node[1])
                store = None


        elif node[0] == "subtree":
            if store:
                command += store

            store = build_command(node[1])

    if store:
        command += store

    return command


def render_grid(grid):
    x_max = max(grid.keys())
    x_min = min(grid.keys())
    y_max = max(max(s) for s in grid.values())
    y_min = min(min(s) for s in grid.values())

    lines = []

    for y in range(y_max, y_min - 1, -1):
        line = ""
        for x in range(x_min, x_max + 1):
            if x in grid and y in grid[x]:
                line += "*"
            else:
                line += " "

        lines.append(line)

    return "\r\n".join(lines)


def execute(code):
    tokens = tokenize(code)
    tree = parse(iter(tokens))
    commands = build_command(iter(tree))

    x = 0
    y = 0

    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    grid = {0: set([0])}

    for c in commands:
        if c == "F":
            x += direction[0][0]
            y += direction[0][1]

            grid.setdefault(x, set()).add(y)

        if c == "R":
            direction = direction[1:] + [direction[0]]

        if c == "L":
            direction = [direction[-1]] + direction[0:-1]

    return render_grid(grid)
