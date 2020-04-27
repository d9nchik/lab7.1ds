def get_data():
    data = []
    with open("input.txt") as iFile:
        while True:
            line = iFile.readline()
            if not line:
                break
            temp = list(map(int, (line[:len(line)] + line[len(line) + 1:]).split()))
            data.append(temp)
    return data


def create_adjacency_matrix(idata):
    matrix = [0] * idata[0][0]
    for x in range(idata[0][0]):
        matrix[x] = [0] * idata[0][0]

    for y in range(1, len(idata)):
        matrix[idata[y][0] - 1][idata[y][1] - 1] = 1
        matrix[idata[y][1] - 1][idata[y][0] - 1] = 1
    return matrix


def find_leaf(adjacency_matrix):
    for i in range(len(adjacency_matrix)):
        total = 0
        for j in range(len(adjacency_matrix)):
            total += adjacency_matrix[i][j]
        if total == 1:
            return i
    print("Заданий граф не є деревом")
    exit(1)


def find_leaf_parent(leaf, adjacency_matrix):
    for j in range(len(adjacency_matrix)):
        if adjacency_matrix[leaf][j] == 1:
            return j
    print("Вершина є ізольованою")
    exit(2)


def get_prufer_code(adjacency_matrix):
    prufer_code = ""
    for x in range(len(adjacency_matrix) - 2):
        leaf = find_leaf(adjacency_matrix)
        parent = find_leaf_parent(leaf, adjacency_matrix)
        adjacency_matrix[leaf][parent] = adjacency_matrix[parent][leaf] = 0
        prufer_code += str(parent + 1) + " "
    return prufer_code


def get_prufer_adjacency_matrix(prufer_code):
    matrix = [0] * (len(prufer_code) + 2)
    for x in range(len(prufer_code) + 2):
        matrix[x] = [0] * (len(prufer_code) + 2)
    numbers = [i for i in range(1, len(prufer_code) + 3)]
    for x in range(len(prufer_code)):
        for number in numbers:
            if number not in prufer_code:
                numbers.remove(number)
                matrix[number - 1][prufer_code[0] - 1] = 1
                matrix[prufer_code[0] - 1][number - 1] = 1
                del prufer_code[0]
                break
    matrix[numbers[0] - 1][numbers[1] - 1] = 1
    matrix[numbers[1] - 1][numbers[0] - 1] = 1
    return matrix


def show_adjacency_matrix(adjacency_matrix):
    print("Знайдена матриця суміжності: ")
    for x in adjacency_matrix:
        for y in x:
            print("%2d" % y, end=" ")
        print()


answer = int(input("Шукати код прюфера(1) чи шукати граф(2): "))
if answer == 1:
    print("Код прюфера:", end=" ")
    print(get_prufer_code(create_adjacency_matrix(get_data())))
elif answer == 2:
    string = input("Введііть код прюфера: ")
    code = list(map(int, (string[:len(string)] + string[len(string) + 1:]).split()))
    show_adjacency_matrix(get_prufer_adjacency_matrix(code))
