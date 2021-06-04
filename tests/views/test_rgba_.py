import pytest

from colorviews import AlphaColor


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("r", 191),
        ("g", 115),
        ("b", 74),
        ("a", 79),
    ])
    def test_valid(self, attr, expected):
        color = AlphaColor.from_rgba_(191, 115, 74, 79)
        assert getattr(color.rgba_, attr) == expected

    def test_vals(self):
        color = AlphaColor.from_rgba_(191, 115, 74, 81)
        assert color.rgba_.vals == (191, 115, 74, 81)

    @pytest.mark.parametrize("attr", [
        "s", "v",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_rgba_(191, 115, 74, 81)
        with pytest.raises(AttributeError):
            getattr(color.rgba_, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("r", 115),
        ("g", 38),
        ("b", 227),
        ("a", 49),
    ])
    def test_valid(self, attr, val):
        color = AlphaColor.from_rgba_(191, 115, 74, 75)
        setattr(color.rgba_, attr, val)
        assert round(getattr(color.rgba_, attr), 4) == val

    @pytest.mark.parametrize("attr", [
        "s", "v",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_rgba_(191, 115, 74, 75)
        with pytest.raises(AttributeError):
            setattr(color.rgba_, attr, 0.1)


@pytest.mark.parametrize("rgba_dict, expected", [
    ({"r": 0x5b}, 0x5b734a80),
    ({"g": 0x0f}, 0xbf0f4a80),
    ({"b": 0xae}, 0xbf73ae80),
    ({"a": 23}, 0xbf734a3b),
    ({"r": 0x5b, "g": 0x0f}, 0x5b0f4a80),
    ({"r": 0x5b, "b": 0xae}, 0x5b73ae80),
    ({"g": 0x0f, "b": 0xae, "a": 52}, 0xbf0fae85),
    ({"r": 0xff, "g": 0x0f, "a": 52}, 0xff0f4a85),
])
def test_replace(rgba_dict, expected):
    color = AlphaColor.from_int(0xbf734a80)  # rgba(191,115,74,50%)
    assert int(color.rgba_.replace(**rgba_dict)) == expected


class TestVals:
    def test_getter(self):
        color = AlphaColor.from_rgba_(191, 115, 74, 75)
        color.rgba_.vals = (72, 40, 60, 23)
        assert color.rgba_.vals == (72, 40, 60, 23)

    @pytest.mark.parametrize("vals", [
        [72, 40, 60, 23],
        (216, 20, 40, 93),
    ])
    def test_setter_valid(self, vals):
        color = AlphaColor.from_rgba_(191, 115, 74, 20)
        color.rgba_.vals = vals
        assert list(color.rgba_) == list(vals)

    @pytest.mark.parametrize("wrong_vals", [
        [72, 40],
        (216, 20, 40),
        (216, 20, 40, 120),
        (216, 20, 40, 100, 20),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = AlphaColor.from_rgba_(191, 115, 74, 10)
        with pytest.raises(ValueError):
            color.rgba_.vals = wrong_vals
