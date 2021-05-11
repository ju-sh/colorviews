import pytest

from colorviews.utils import validate, scale


class TestValidate:
    @pytest.mark.parametrize("val", [
        0, 0.25, 1
    ])
    def test_valid(self, val):
        assert validate(val) is None

    @pytest.mark.parametrize("val", [
        -1, 1.2
    ])
    def test_invalid(self, val):
        with pytest.raises(ValueError):
            validate(val)


@pytest.mark.parametrize("val, factor, expected", [
    (0.5, 0xff, 128),
    (0.75, 100, 75),
    (0, 100, 0),
])
def test_scale(val, factor, expected):
    assert scale(val, factor) == expected
