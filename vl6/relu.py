# Definiere die ReLU-Funktion relu(x) = max(x, 0) und 
# rufe sie für Werte von -10 bis 10 auf
def relu(x: int) -> int:
    """berechnet relu(x) = max(x, 0)

    Args:
        x (int): _description_

    Returns:
        int: _description_
    """
    if x < 0:
        return 0
    else:
        return x
    
if __name__ == "__main__":
    for i in range(-10, 11):
        print(f"x = {i}, relu({i}) = {relu(i)}")