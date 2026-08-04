from lab10 import eval_rpn, decode_string, daily_temperatures, num_islands


def test_eval_rpn():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["3", "4", "+"]) == 7
    assert eval_rpn(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22


def test_decode_string():
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("abc") == "abc"


def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
    assert daily_temperatures([50]) == [0]


# STRETCH (optional) - skipping this still passes the three problems above.
def test_num_islands():
    assert num_islands(["11110", "11010", "11000", "00000"]) == 1
    assert num_islands(["11000", "11000", "00100", "00011"]) == 3
    assert num_islands(["000"]) == 0
    assert num_islands(["1"]) == 1
    assert num_islands([]) == 0
