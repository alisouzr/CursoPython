def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if int(sq**0.5)*int(sq**0.5) == sq:
        num = (sq**0.5) + 1
        return int(num * num)
    return -1


print(find_next_square(625))
