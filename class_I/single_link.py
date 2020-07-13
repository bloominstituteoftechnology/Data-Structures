commands_1 = ["n","s","e","w"]

commands_2 = ["get","take","drop","use"]

for x in commands_1:
    for y in commands_2:
        command_pairs = list((zip(x,y)))
        print(command_pairs)
