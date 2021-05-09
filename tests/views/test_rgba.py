import pytest

from colorviews import AlphaColor


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("r", 0.75),
        ("g", 0.45),
        ("b", 0.29),
        ("a", 0.79),
    ])
    def test_valid(self, attr, expected):
        color = AlphaColor.from_rgba(0.75, 0.45, 0.29, 0.79)
        assert round(getattr(color.rgba, attr), 4) == expected

    def test_vals(self):
        color = AlphaColor.from_rgba(0.75, 0.45, 0.29, 0.81)
        assert color.rgba.vals == (0.75, 0.45, 0.29, 0.81)

    @pytest.mark.parametrize("attr", [
        "s", "v",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_rgba(0.75, 0.45, 0.29, 0.81)
        with pytest.raises(AttributeError):
            getattr(color.rgba, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("r", 0.45),
        ("g", 0.15),
        ("b", 0.89),
        ("a", 0.49),
    ])
    def test_valid(self, attr, val):
        color = AlphaColor.from_rgba(0.75, 0.45, 0.29, 0.75)
        setattr(color.rgba, attr, val)
        assert round(getattr(color.rgba, attr), 4) == val

    @pytest.mark.parametrize("attr", [
        "s", "v",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_rgba(0.75, 0.45, 0.29, 0.75)
        with pytest.raises(AttributeError):
            setattr(color.rgba, attr, 0.1)


@pytest.mark.parametrize("rgba_dict, expected", [
    ({"r": 0x5b / 0xff}, 0x5b734a80),
    ({"g": 0x0f / 0xff}, 0xbf0f4a80),
    ({"b": 0xae / 0xff}, 0xbf73ae80),
    ({"a": 0.23}, 0xbf734a3b),
    ({"r": 0x5b / 0xff, "g": 0x0f / 0xff}, 0x5b0f4a80),
    ({"r": 0x5b / 0xff, "b": 0xae / 0xff}, 0x5b73ae80),
    ({"g": 0x0f / 0xff, "b": 0xae / 0xff, "a": 0.52}, 0xbf0fae85),
    ({"r": 0xff / 0xff, "g": 0x0f / 0xff, "a": 0.52}, 0xff0f4a85),
])
def test_replace(rgba_dict, expected):
    color = AlphaColor.from_int(0xbf734a80)  # rgba(191,115,74,50%)
    assert int(color.rgba.replace(**rgba_dict)) == expected


class TestVals:
    def test_getter(self):
        color = AlphaColor.from_rgba(0.75, 0.45, 0.29, 0.75)
        color.rgba.vals = (0.2, 0.4, 0.6, 0.23)
        assert color.rgba.vals == (0.2, 0.4, 0.6, 0.23)

    @pytest.mark.parametrize("vals", [
        [0.2, 0.4, 0.6, 0.23],
        (0.6, 0.2, 0.4, 0.93),
    ])
    def test_setter_valid(self, vals):
        color = AlphaColor.from_rgba(0.75, 0.45, 0.29, 0.2)  # rgba(191,115,74)
        color.rgba.vals = vals
        assert list(color.rgba) == list(vals)

    @pytest.mark.parametrize("wrong_vals", [
        [0.2, 0.4],
        (0.6, 0.2, 0.4),
        (0.6, 0.2, 0.4, 1.2),
        (0.6, 0.2, 0.4, 1.0, 0.2),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = AlphaColor.from_rgba(0.75, 0.45, 0.29, 0.1)  # rgba(191,115,74)
        with pytest.raises(ValueError):
            color.rgba.vals = wrong_vals
