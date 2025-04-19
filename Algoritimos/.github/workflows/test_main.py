# This is a simple test that will always pass
def test_const():
    assert True

# Tests basic math
def test_math():
    assert 1 + 1 == 2

# This tests string concatenation
def test_string_concatenation():
    assert "hello" + " " + "world" == "hello world"