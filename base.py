class Cell():
        def __init__(self, value):
            self.value = value
            self.right = 0
            self.diag = 0
            self.down = 0

        def print(self):
            print("{} {} {} {}".format(self.value, self.right, self.diag, self.down))

def get_base(prompt):
    while True:
        string = input(prompt)
        isBad = 0
        for base in string:
            if not (base == 'A' or base == 'C' or base == 'G' or base == 'T'):
                print("Invalid string, use only ACGT bases:")
                isBad = 1
                break
        if isBad == 0:
            return string

a = get_base("First base string a is: ")
a += '-'
b = get_base("Second base string b is: ")
b += '-'
cell = [[Cell(0) for y in range(len(b))] for x in range(len(a))]

def main():
    for i in range(len(a)-2, -1, -1):
        cell[i][len(b)-1].value = cell[i+1][len(b)-1].value + 2
        cell[i][len(b)-1].right = 1
    for j in range(len(b)-2, -1, -1):
        cell[len(a)-1][j].value = cell[len(a)-1][j+1].value + 2
        cell[len(a)-1][j].down = 1

    for j in range (len(b)-2, -1, -1):
        for i in range (len(a)-2, -1, -1):
            m = min(cell[i+1][j].value + 2, cell[i][j+1].value + 2, cell[i+1][j+1].value + match(a[i], b[j]))
            if cell[i+1][j].value + 2 == m:
                cell[i][j].right = 1
            if cell[i][j+1].value + 2 == m:
                cell[i][j].down = 1
            if cell[i+1][j+1].value + match(a[i], b[j]) == m:
                cell[i][j].diag = 1
            cell[i][j].value = m

    concatenate("", "", 0, 0)


def match (baseA, baseB):
    if baseA == baseB:
        return 0
    return 1

def concatenate(word1, word2, i, j):
    if cell[i][j].right == 1:
        concatenate(word1 + a[i], word2 + '_', i + 1, j)
    if cell[i][j].diag == 1:
        concatenate(word1 + a[i], word2 + b[j], i + 1, j + 1)
    if cell[i][j].down == 1:
        concatenate(word1 + '_', word2 + b[j], i, j + 1)
    if (i == len(a) - 1 ) and (j == len(b) -1 ):
        print(word1)
        print(word2)
        print()


if __name__ == "__main__":
    main()