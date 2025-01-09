def num_zeros(values: list) -> int:
    """Return the number of zeros in the given list of values."""
    count = 0
    for i in range(1, len(values)):
        if values[i] == 0:
            count += 1
    return count

