# Example:

sorteio = {1, 23}

sorteio.add(25) # >>> {1, 23, 25}
sorteio.add(42) # >>> {1, 23, 25, 42}
sorteio.add(25) # >>> {1, 23, 25, 42}
sorteio.add(73)

print(sorteio)