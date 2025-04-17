class Graph:

    def __init__(self, con_list: list):
        self.connectivity_list = con_list
        self.visited: list = [0] * len(self.connectivity_list)

    def __repr__(self):
        return ' '.join(map(str, self.connectivity_list))

    def dfs(self, vertex: int, visited:list[int]):
        visited[vertex] = 1
        print(f'we are in {vertex} now')
        for v in self.connectivity_list[vertex]:
            if not visited[v]:
                dfs(self.connectivity_list, v, visited)
        print(f'we are in {vertex} again')
        return

    @property
    def length(self):
        return len(self.connectivity_list)


def dfs(graph: list[list[int]], vertex: int, visited: list[int]):
    visited[vertex] = 1
    print(f'we are in {vertex} now')
    for v in graph[vertex]:
        if not visited[v]:
            dfs(graph, v, visited)
    print(f'we are in {vertex} again')
    return


def main():
    graph = [
        [1],
        [0, 2, 4, 6],
        [1, 3],
        [2, 4],
        [1, 3, 5],
        [4, 6],
        [1, 5]
    ]
    vertex = 2

    visited = [0] * len(graph)
    #print(visited)

    #dfs(graph, vertex, visited)
    gr = Graph(graph)
    print(gr)
    gr.dfs(3, visited)
    print()
    visited = [0] * gr.length
    gr.dfs(2, visited)

if __name__ == '__main__':
    main()
