import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Позитивные тесты для capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitilize(input_str) == expected

# Позитивные тесты для trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world  ", "hello world  "),  # Убедитесь, что это ожидаемое поведение
    ("", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Позитивные тесты для to_list
@pytest.mark.positive
@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
])
def test_to_list_positive(input_str, delimiter, expected):
    assert string_utils.to_list(input_str, delimiter) == expected

# Позитивные тесты для contains
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "a", False),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# Позитивные тесты для delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("", "a", ""),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

# Позитивные тесты для starts_with
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("", "a", False),
])
def test_starts_with_positive(string, symbol, expected):
    assert string_utils.starts_with(string, symbol) == expected

# Позитивные тесты для end_with
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    ("", "a", False),
])
def test_end_with_positive(string, symbol, expected):
    assert string_utils.end_with(string, symbol) == expected

# Позитивные тесты для is_empty
@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
    ("", True),
    (" ", True),
    ("SkyPro", False),
])
def test_is_empty_positive(string, expected):
    assert string_utils.is_empty(string) == expected

# Позитивные тесты для list_to_string
@pytest.mark.positive
@pytest.mark.parametrize("lst, joiner, expected", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([], ", ", ""),
])
def test_list_to_string_positive(lst, joiner, expected):
    assert string_utils.list_to_string(lst, joiner) == expected

    # Негативные тесты для capitalize
@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    None,
    123,
])
def test_capitalize_negative(input_str):
    with pytest.raises(AttributeError):
        string_utils.capitilize(input_str)

# Негативные тесты для trim
@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    None,
    123,
])
def test_trim_negative(input_str):
    with pytest.raises(AttributeError):
        string_utils.trim(input_str)

# Негативные тесты для to_list
@pytest.mark.xfail
@pytest.mark.parametrize("input_str, delimiter", [
    (None, ","),
    ("a,b,c,d", None),
])
def test_to_list_negative(input_str, delimiter):
    with pytest.raises(TypeError):
        string_utils.to_list(input_str, delimiter)

# Негативные тесты для contains
@pytest.mark.xfail
@pytest.mark.parametrize("string, symbol", [
    (None, "S"),
    ("SkyPro", None),
])
def test_contains_negative(string, symbol):
    with pytest.raises(TypeError):
        string_utils.contains(string, symbol)

# Негативные тесты для delete_symbol
@pytest.mark.xfail
@pytest.mark.parametrize("string, symbol", [
    (None, "k"),
    ("SkyPro", None),
])
def test_delete_symbol_negative(string, symbol):
    with pytest.raises(TypeError):
        string_utils.delete_symbol(string, symbol)

# Негативные тесты для starts_with
@pytest.mark.xfail
@pytest.mark.parametrize("string, symbol", [
    (None, "S"),
    ("SkyPro", None),
])
def test_starts_with_negative(string, symbol):
    with pytest.raises(TypeError):
        string_utils.starts_with(string, symbol)

# Негативные тесты для end_with
@pytest.mark.xfail
@pytest.mark.parametrize("string, symbol", [
    (None, "o"),
    ("SkyPro", None),
])
def test_end_with_negative(string, symbol):
    with pytest.raises(TypeError):
        string_utils.end_with(string, symbol)

# Негативные тесты для is_empty
@pytest.mark.negative
@pytest.mark.parametrize("string", [
    None,
    123,
])
def test_is_empty_negative(string):
    with pytest.raises(AttributeError):
        string_utils.is_empty(string)

# Негативные тесты для list_to_string
@pytest.mark.negative
@pytest.mark.parametrize("lst, joiner", [
    (None, ", "),
    ([1, 2, 3], None),
])
def test_list_to_string_negative(lst, joiner):
    with pytest.raises(TypeError):
        string_utils.list_to_string(lst, joiner)