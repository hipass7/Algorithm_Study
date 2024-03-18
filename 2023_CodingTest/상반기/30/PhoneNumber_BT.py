table = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

num_input = input()
result_list = []

def BT(index, letter):
    if index == len(num_input):
        result_list.append(letter)
        return

    graph = table[int(num_input[index])]
    for a in graph:
        BT(index + 1, letter + a)
    letter = ""

BT(0, "")
print(result_list)