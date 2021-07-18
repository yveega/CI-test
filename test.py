from main import sum1, mult

def test_sum():
    assert sum1(3, 4, 5) == 12, "Incorrect sum"


def test_mult():
    assert mult(1, 2, 3) == 6, "Incorrect mult"


if __name__ == "__main__":
    test_sum()
    test_mult()
    print("Tests passed")