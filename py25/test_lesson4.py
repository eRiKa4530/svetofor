from for_test import is_palindrom
def test_palindrom_fucition():
    test_case = [
        ('hello', False),
        ('dad', True),
        ('John', False),
        ('lol', True)
    ]
    for i in test_case:
        print(i)
    for i in test_case:
        assert is_palindrom(i[0]) == i[1]