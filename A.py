from pokemonCaptureAlgorithm import pokeCaptureGenI


def A():
    name = input('Which Pokemon are you trying to catch?')
    health = int(input("What is the full health of the pokemon?"))
    print(pokeCaptureGenI(health,name))