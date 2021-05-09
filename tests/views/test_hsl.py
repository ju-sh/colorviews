import pytest

from colorviews import Color


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("h", 0.75),
        ("s", 0.47),
        ("l", 0.29),
    ])
    def test_valid(self, attr, expected):
        color = Color.from_hsl(0.75, 0.47, 0.29)
        assert round(getattr(color.hsl, attr), 4) == expected

    @pytest.mark.parametrize("attr", [
        "r", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_hsl(0.75, 0.47, 0.29)
        with pytest.raises(AttributeError):
            getattr(color.hsl, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("h", 0.75),
        ("s", 0.5),
        ("l", 0.29),
    ])
    def test_valid(self, attr, val):
        color = Color.from_hsl(0.45, 0.15, 0.89)
        setattr(color.hsl, attr, val)
        assert round(getattr(color.hsl, attr), 4) == val

    @pytest.mark.parametrize("attr", [
        "r", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_hsl(0.75, 0.47, 0.29)
        with pytest.raises(AttributeError):
            setattr(color.hsl, attr, 0.1)


@pytest.mark.parametrize("h, s, l, expected", [
    (91 / 360, None, None, 0x496b29),
    (None, 0.15, None, 0x4a3f55),
    (None, None, 0.74, 0xbd9fdb),
    (91 / 360, 0.15, None, 0x4a553f),
    (91 / 360, None, 0.74, 0xbcdb9f),
    (None, 15 / 100, 0.74, 0xbdb3c7),
    (91 / 360, 15 / 100, 0.74, 0xbcc7b3),
])
def test_replace(h, s, l, expected):
    color = Color.from_hsl(0.75, 0.45, 0.29)
    assert int(color.hsl.replace(h, s, l)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [0.2, 0.4, 0.6],
        (0.6, 0.2, 0.4),
    ])
    def test_setter_valid(self, vals):
        color = Color.from_hsl(0.75, 0.45, 0.29)
        color.hsl.vals = vals
        assert [round(val, 4) for val in color.hsl] == list(vals)

    @pytest.mark.parametrize("wrong_vals", [
        [0.2, 0.4],
        (0.6, 0.2, 0.4, 1.0),
        (1.6, 0.2, 0.4),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = Color.from_hsl(0.75, 0.45, 0.29)
        with pytest.raises(ValueError):
            color.hsl.vals = wrong_vals


def test_vals_getter():
    color = Color.from_hsl(0.75, 0.45, 0.29)
    assert [round(val, 4) for val in color.hsl.vals] == [0.75, 0.45, 0.29]
