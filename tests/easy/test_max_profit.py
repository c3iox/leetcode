from easy.max_profit import max_profit


def test_empty():
    assert max_profit(list()) == 0


def test_one():
    assert max_profit([1]) == 0


def test_accend():
    stock = [1, 2, 3, 4]
    assert max_profit(stock) == stock[-1] - stock[0]


def test_decent():
    stock = [4, 3, 2, 1]
    assert max_profit(stock) == 0


def test_unsorted():
    stock = [4, 3, 2, 4, 5]
    assert max_profit(stock) == 3
