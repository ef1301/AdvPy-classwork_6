from pprint import pprint

def handle_input(s):
    edge_pair_inputs = []
    print("Conversion to " + s + "\n")
    while(True):
        user = input('Enter your edge pair tuple and ensure you have WHITESPACE between your nodes and direction [Ex: 1 -> 2]. Enter q to quit inputs. ')
        split_user = user.split()
        if(split_user[0] == 'q'):
            break
        if(len(split_user) != 3):
            print(user, " was an invalid input. \n")
            continue
        if(split_user[0].isdigit() == False or split_user[2].isdigit() == False):
            print("Please use numeric nodes. \n")
            continue
        if(split_user[1] == '->'):
            edge_pair_inputs.append((int(split_user[0]),int(split_user[2])))
        elif(split_user[1] == '<-'):
            edge_pair_inputs.append((int(split_user[2]),int(split_user[0])))
        elif(split_user[1] == '<>'):
            edge_pair_inputs.append((int(split_user[0]),int(split_user[2])))
            edge_pair_inputs.append((int(split_user[2]),int(split_user[0])))
        else:
            continue
    return edge_pair_inputs

def to_adj_list():
    user_input = handle_input("adjacency lists")
    adj_list = {}
    for i in range(0,len(user_input)):
        adj_list.setdefault(user_input[i][0],[]).append(user_input[i][1])
    pprint(adj_list)
    return adj_list

def count_nodes(tuples):
    set_of_nodes = set()
    greatest_val = 0
    for edge_pair in tuples:
        greatest_val = max([greatest_val, edge_pair[0], edge_pair[1]])
        set_of_nodes.add(edge_pair[0])
        set_of_nodes.add(edge_pair[1])
    return set_of_nodes, greatest_val

def to_adj_matrix():
    user_input = handle_input("adjacency matrices")
    count = count_nodes(user_input)[1]
    adj_matrix = []
    list_to_append = []
    for value in range(count+1):
        list_to_append.append(0)

    for value in range(count+1):
        adj_matrix.append(list_to_append[:])

    for edge_value in user_input:
        adj_matrix[edge_value[0]][edge_value[1]] = 1

    pprint(adj_matrix)
    return adj_matrix

def main():
    #to_adj_list()
    to_adj_matrix()

if __name__ == "__main__":
    main()
