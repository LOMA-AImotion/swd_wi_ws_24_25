def subsample_to_half(values:list) -> list:
    """Return a new list containing every second value from the given list."""
    return values[:len(values)//2:2]

if __name__ == "__main__":
    print(subsample_to_half([3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]))