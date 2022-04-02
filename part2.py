class adjacency_list:
    def __init__(self):
        self.nodes = {}
    def __str__(self):
        return str(self.nodes)
    def add_tuple(self,input_tuple):
        self.nodes.setdefault(input_tuple[0],[]).append(input_tuple[1])
        if(input_tuple[1] not in self.nodes):
            self.nodes[input_tuple[1]] = []
    def add_tuples(self,tuples):
        for i in range(0,len(tuples)):
            self.add_tuple(tuples[i])
    def add_tuples_with_direction(self,input_tuples):
        for x in input_tuples:
            print(x)
            self.add_tuple_with_direction(x)
    def add_tuple_with_direction(self,input_tuple):
        if(input_tuple[2] == '->'):
            self.add_tuple((input_tuple[0],input_tuple[1]))
        elif(input_tuple[2] == '<-'):
            self.add_tuple((input_tuple[1],input_tuple[0]))
        elif(input_tuple[2] == '<>'):
            self.add_tuple((input_tuple[0],input_tuple[1]))
            self.add_tuple((input_tuple[1],input_tuple[0]))
    def set_of_nodes(self):
        nodes_set = set()
        for node in self.nodes:
            nodes_set.add(node)
            for edges in self.nodes[node]:
                nodes_set.add(edges)
        return nodes_set
    def most_away(self,counts):
        most = next(iter(counts))
        print(most)
        for i in counts:
            if(counts[i][0] > counts[most][0]):
                most = i
        return most
    def most_toward(self,counts):
        most = next(iter(counts))
        for i in counts:
            if(counts[i][1] > counts[most][1]):
                most = i
        return most
    def most_toward_and_away(self,counts):
        most = next(iter(counts))
        for i in counts:
            if(counts[i][0] + counts[i][1] > counts[most][0] + counts[most][1]):
                most = i
        return most
    def most_edges(self):
        counts = {}
        for edge in self.set_of_nodes():
            counts.setdefault(edge,[]).append(0)
            counts.setdefault(edge,[]).append(0)
        # MOST AWAY
        for edge in counts:
            if edge in self.nodes:
                counts[edge][0] = len(self.nodes[edge])
        #MOST TOWARD
        for edge in counts:
            if edge in self.nodes:
                for outgoing in self.nodes[edge]:
                    counts[outgoing][1] += 1
        most = 0
        print("Most edges leaving the node: ", self.most_away(counts))
        print("Most edges pointing toward the node: ", self.most_toward(counts))
        print("Most edges leaving and pointing toward the node: ", self.most_toward_and_away(counts))
    def BFS(self,start):
        print("BFS Traversal")
        if start not in self.nodes:
            return False
        visited = [False] * (max(self.nodes) + 1)
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            s = queue.pop(0)
            print(s,end=" ")
            for i in self.nodes[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print("\n")
        return True
    def DFS_helper(self,node,visited):
        visited.add(node)
        print(node,end=" ")
        for i in self.nodes[node]:
            if i not in visited:
                self.DFS_helper(i,visited)
    def DFS(self,start):
        print("DFS Traversal")
        visited = set()
        if start not in self.nodes:
            return False
        self.DFS_helper(start,visited)
        print("\n")
        return True
    def path(self,start,end):
        print("Path:")
        if start not in self.nodes:
            return False
        if end not in self.nodes:
            return False
        keys = self.nodes.keys()
        visited = dict.fromkeys(keys, False)
        queue = []
        queue.append(start)
        visited[start] = True
        path = ""
        while queue:
            s = queue.pop(0)
            path += str(s) + " "
            index = 0
            for i in self.nodes[s]:
                if i == end:
                    path += str(end) + " "
                    print(path)
                    return True
                if visited[s] == False:
                    queue.append(s)
                    visited[index] = True
                index += 1
        print("No path")
        return False

class adjacency_matrix:
    def __init__(self):
        self.nodes = []
        self.indices = {}
    def __str__(self):
        s = "  "
        labels = []
        for x in self.indices:
            s += str(x) + " "
            labels.append(str(x))
        s += "\n"
        for i in range(len(self.nodes)):
            s += labels[i] + " "
            for j in self.nodes[i]:
                s += str(j) + " "
            s += "\n"
        return s
    def count_nodes(self,tuples):
        set_of_nodes = set()
        for edge_pair in tuples:
            set_of_nodes.add(edge_pair[0])
            set_of_nodes.add(edge_pair[1])
        x = list(set_of_nodes)
        for i in range(len(x)):
            self.indices[x[i]] = i
        return set_of_nodes, len(set_of_nodes)
    def to_adj_matrix(self,user_input):
        count = self.count_nodes(user_input)[1]
        adj_matrix = []
        list_to_append = []
        for value in range(count):
            list_to_append.append(0)

        for value in range(count):
            adj_matrix.append(list_to_append[:])

        for edge_value in user_input:
            adj_matrix[self.indices[edge_value[0]]][self.indices[edge_value[1]]] = 1
        return adj_matrix
    def initialize_with_tuples(self,tuples):
        self.nodes = self.to_adj_matrix(tuples)
    def add_tuples(self,input_tuples):
        for t in input_tuples:
            self.add_tuple(t)
    def add_tuple(self,input_tuple):
        if input_tuple[0] not in self.indices:
            for i in range(len(self.nodes)):
                self.nodes[i].append(0)
            temp = [0] * len(self.nodes[0])
            self.nodes.append(temp)
            self.indices[input_tuple[0]] = len(self.nodes[0]) - 1
        if input_tuple[1] not in self.indices:
            for i in range(len(self.nodes)):
                self.nodes[i].append(0)
            temp = [0] * len(self.nodes[0])
            self.nodes.append(temp)
            self.indices[input_tuple[1]] = len(self.nodes[0]) - 1
        self.nodes[self.indices[input_tuple[0]]][self.indices[input_tuple[1]]] = 1
    def add_tuple_with_direction(self,input_tuple):
        if(input_tuple[2] == '->'):
            self.add_tuple((input_tuple[0],input_tuple[1]))
        elif(input_tuple[2] == '<-'):
            self.add_tuple((input_tuple[1],input_tuple[0]))
        elif(input_tuple[2] == '<>'):
            self.add_tuple((input_tuple[0],input_tuple[1]))
            self.add_tuple((input_tuple[1],input_tuple[0]))
    def add_tuples_with_direction(self,input_tuples):
        for x in input_tuples:
            self.add_tuple_with_direction(x)
    def most_away(self):
        largest_node = 0
        largest_count = 0
        counts = []
        legend = [x for x in self.indices]
        for i in range(len(self.nodes)):
            count = self.nodes[i].count(1)
            counts.append(count)
            largest_count = max(largest_count,count)
            if largest_count == count:
                largest_node = legend[i]
        return counts,largest_node
    def most_toward(self):
        largest_node = 0
        largest_count = 0
        counts = []
        legend = [x for x in self.indices]
        for i in range(len(self.nodes)):
            count = [row[i] for row in self.nodes].count(1)
            counts.append(count)
            largest_count = max(largest_count,count)
            if largest_count == count:
                largest_node = legend[i]
        return counts,largest_node
    def most_toward_and_away(self):
        away = self.most_away()
        toward = self.most_toward()
        largest_node = 0
        largest_count = 0
        legend = [x for x in self.indices]
        for i in range(len(self.nodes)):
            count = away[0][i] + toward[0][i]
            largest_count = max(largest_count,count)
            if largest_count == count:
                largest_node = legend[i]
        return [away[1], toward[1], largest_node]
    def most_edges(self):
        most_counts = self.most_toward_and_away()
        print("Most edges leaving the node: ", most_counts[0])
        print("Most edges pointing toward the node: ", most_counts[1])
        print("Most edges leaving and pointing toward the node: ", most_counts[2])
    def BFS(self,start):
        print("BFS Traversal")
        if start not in self.indices:
            return False
        visited = [False] * (len(self.nodes[0]))
        queue = []
        legend = [x for x in self.indices]
        queue.append(start)
        visited[self.indices[start]] = True
        path = ""
        while queue:
            s = queue.pop(0)
            path += str(s) + " "
            index = 0
            for i in self.nodes[self.indices[s]]:
                if i == 1 and visited[self.indices[legend[index]]] == False:
                    queue.append(legend[index])
                    visited[index] = True
                index += 1
        print(path,"\n")
        return True
    def DFS_helper(self,node,visited):
        visited.add(node)
        print(node,end=" ")
        legend = [x for x in self.indices]
        index = 0
        for i in self.nodes[self.indices[node]]:
            if i == 1 and legend[index] not in visited:
                self.DFS_helper(legend[index],visited)
            index += 1
    def DFS(self,start):
        print("DFS Traversal")
        visited = set()
        legend = [x for x in self.indices]
        if start not in legend:
            return False
        self.DFS_helper(start,visited)
        print("\n")
        return True
    def path(self,start,end):
        print("Path:")
        if start not in self.indices:
            return False
        if end not in self.indices:
            return False
        visited = [False] * (len(self.nodes[0]))
        queue = []
        legend = [x for x in self.indices]
        queue.append(start)
        visited[start] = True
        path = ""
        while queue:
            s = queue.pop(0)
            path += str(s) + " "
            index = 0
            for i in self.nodes[self.indices[s]]:
                if i == 1 and legend[index] == end:
                    path += str(end) + " "
                    print(path)
                    return True
                if i == 1 and visited[index] == False:
                    queue.append(legend[index])
                    visited[index] = True
                index += 1
        print("No path")
        return False

def main():
    x = adjacency_matrix();
    x.initialize_with_tuples([(1,2),(2,1),(1,3),(3,2),(4,2),(6,2)])
    print(x)
    x.add_tuples_with_direction([(1,4,'<>'),(2,5,'<-'),(2,3,'->')])
    print(x)
    x.BFS(1)
    x.DFS(1)
    x.path(4,2)
    x.most_edges()
    y = adjacency_list();
    y.add_tuples([(1,2),(2,1),(1,3),(3,2),(4,2),(6,2)])
    y.BFS(1)
    y.DFS(1)
    y.add_tuples_with_direction([(1,4,'<>'),(2,5,'<-'),(2,3,'->')])
    y.path(2,3)
    print(y)
if __name__ == "__main__":
    main()
