import pytest

from colorviews import Color


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("r", 0.75),
        ("g", 0.45),
        ("b", 0.29),
    ])
    def test_valid(self, attr, expected):
        color = Color.from_rgb(0.75, 0.45, 0.29)
        assert round(getattr(color.rgb, attr), 4) == expected

    @pytest.mark.parametrize("attr", [
        "s", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_rgb(0.75, 0.45, 0.29)
        with pytest.raises(AttributeError):
            getattr(color.rgb, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("r", 0.45),
        ("g", 0.15),
        ("b", 0.89),
    ])
    def test_valid(self, attr, val):
        color = Color.from_rgb(0.75, 0.45, 0.29)
        setattr(color.rgb, attr, val)
        assert round(getattr(color.rgb, attr), 4) == val

    def test_vals(self):
        color = Color.from_rgb(0.75, 0.45, 0.29)
        color.rgb.vals = (0.2, 0.4, 0.6)
        assert color.rgb.vals == (0.2, 0.4, 0.6)

    @pytest.mark.parametrize("attr", [
        "s", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_rgb(0.75, 0.45, 0.29)
        with pytest.raises(AttributeError):
            setattr(color.rgb, attr, 0.1)


@pytest.mark.parametrize("rgb_dict, expected", [
    ({"r": 91 / 0xff}, 0x5b734a),
    ({"g": 15 / 0xff}, 0xbf0f4a),
    ({"b": 174 / 0xff}, 0xbf73ae),
    ({"r": 91 / 0xff, "g": 15 / 0xff}, 0x5b0f4a),
    ({"r": 91 / 0xff, "b": 174 / 0xff}, 0x5b73ae),
    ({"g": 15 / 0xff, "b": 174 / 0xff}, 0xbf0fae),
    ({"r": 91 / 0xff, "g": 15 / 0xff, "b": 174 / 0xff}, 0x5b0fae),
])
def test_replace(rgb_dict, expected):
    color = Color.from_rgb(0.75, 0.45, 0.29)  # rgb(191,115,74)
    assert int(color.rgb.replace(**rgb_dict)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [0.2, 0.4, 0.6],
        (0.6, 0.2, 0.4),
    ])
    def test_setter_valid(self, vals):
        color = Color.from_rgb(0.75, 0.45, 0.29)  # rgb(191,115,74)
        color.rgb.vals = vals
        assert list(color.rgb) == list(vals)

    @pytest.mark.parametrize("wrong_vals", [
        [0.2, 0.4],
        (0.6, 0.2, 0.4, 1.0),
        (1.6, 0.2, 0.4),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = Color.from_rgb(0.75, 0.45, 0.29)  # rgb(191,115,74)
        with pytest.raises(ValueError):
            color.rgb.vals = wrong_vals

    def test_getter(self):
        color = Color.from_rgb(0.75, 0.45, 0.29)
        assert color.rgb.vals == (0.75, 0.45, 0.29)
