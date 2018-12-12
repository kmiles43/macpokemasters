
from OnevOne import oneVone
from OurStack import Stack


def fight(trainer1, trainer2):

    trainer1Party = Stack()
    trainer2Party = Stack()

    array1 = trainer1.getPokemon()
    array2 = trainer2.getPokemon()

    # array3 = []
    for i in range(len(array1)-1, -1, -1):
        trainer1Party.push(array1[i])
    for i in range(len(array2)-1,-1,-1):
        trainer2Party.push(array2[i])

        # array3.append(catch2)
    # for item in array3:
    #     print(item.getName())
    poke1 = trainer1Party.pop()
    # print(poke1.moves)

    # for move in poke1.moves:
    #     if move in AllMoves:
    #         print("The move is in AllMoves")
    #     else:
    #         print("the move is not there")
    poke2 = trainer2Party.pop()
    # print(poke2)

    while trainer1Party.size() > 0 and trainer2Party.size() > 0:


        winner = oneVone(poke1,poke2)
        if winner == poke1:
            poke2 = trainer2Party.pop()
        elif winner == poke2:
            poke1 = trainer1Party.pop()
        if trainer1Party.isEmpty():
            return trainer2.name
        elif trainer2Party.isEmpty():
            return trainer1.name

