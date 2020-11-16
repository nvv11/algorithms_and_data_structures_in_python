# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по
# одному разу). Сколько рукопожатий было?

def friends(num):
    if num < 2:
        return 'Слишком мало друзей'

    graph = []

    for i in range(num):
        for j in range(num):
            if i != j:
                graph.append((i, j))

    print(graph)

    return len(graph) // 2


print(friends(int(input('Сколько друзей встретилось: '))))
