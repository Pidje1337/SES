
def malloc(numbers):
    return [None] * numbers

def realloc(old_memory, old_size, new_size):
    new_memory = malloc(new_size)

    for i in range(0, old_size, 1):
        new_memory[i] = old_memory[i]

    return new_memory