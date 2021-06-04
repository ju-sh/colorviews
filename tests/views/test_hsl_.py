import pytest

from colorviews import Color


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("h", 270),
        ("s", 47),
        ("l", 29),
    ])
    def test_valid(self, attr, expected):
        color = Color.from_hsl_(270, 47, 29)
        assert getattr(color.hsl_, attr) == expected

    @pytest.mark.parametrize("attr", [
        "r", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_hsl_(270, 47, 29)
        with pytest.raises(AttributeError):
            getattr(color.hsl_, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("h", 270),
        ("s", 50),
        ("l", 29),
    ])
    def test_valid(self, attr, val):
        color = Color.from_hsl_(162, 15, 89)
        setattr(color.hsl_, attr, val)
        assert getattr(color.hsl_, attr) == val

    @pytest.mark.parametrize("attr", [
        "r", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_hsl_(270, 47, 29)
        with pytest.raises(AttributeError):
            setattr(color.hsl_, attr, 10)


@pytest.mark.parametrize("hsl_dict, expected", [
    ({"h": 91}, 0x496b29),
    ({"s": 15}, 0x4a3f55),
    ({"l": 74}, 0xbd9fdb),
    ({"h": 91, "s": 15}, 0x4a553f),
    ({"h": 91, "l": 74}, 0xbcdb9f),
    ({"s": 15, "l": 74}, 0xbdb3c7),
    ({"h": 91, "s": 15, "l": 74}, 0xbcc7b3),
])
def test_replace(hsl_dict, expected):
    color = Color.from_hsl_(270, 45, 29)
    assert int(color.hsl_.replace(**hsl_dict)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [72, 40, 60],
        (216, 20, 40),
    ])
    def test_setter_valid(self, vals):
        color = Color.from_hsl_(270, 45, 29)
        color.hsl_.vals = vals
        assert color.hsl_.vals == tuple(vals)

    def test_setter_valid_round_h(self):
        color = Color.from_hsl_(270, 45, 29)
        color.hsl_.vals = (576, 20, 40)
        assert color.hsl_.vals == (216, 20, 40)

    @pytest.mark.parametrize("wrong_vals", [
        [72, 40],
        (216, 20, 40, 100),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = Color.from_hsl_(270, 45, 29)
        with pytest.raises(ValueError):
            color.hsl_.vals = wrong_vals


def test_vals_getter():
    color = Color.from_hsl_(270, 45, 29)
    assert color.hsl_.vals == (270, 45, 29)
