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


print(get_prufer_code(create_adjacency_matrix(get_data())))
