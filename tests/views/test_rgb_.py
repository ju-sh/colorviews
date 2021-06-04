import pytest

from colorviews import Color


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("r", 191),
        ("g", 115),
        ("b", 74),
    ])
    def test_valid(self, attr, expected):
        color = Color.from_rgb_(191, 115, 74)
        assert getattr(color.rgb_, attr) == expected

    @pytest.mark.parametrize("attr", [
        "s", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_rgb_(191, 115, 74)
        with pytest.raises(AttributeError):
            getattr(color.rgb_, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("r", 115),
        ("g", 38),
        ("b", 227),
    ])
    def test_valid(self, attr, val):
        color = Color.from_rgb_(191, 115, 74)
        setattr(color.rgb_, attr, val)
        assert round(getattr(color.rgb_, attr), 4) == val

    def test_vals(self):
        color = Color.from_rgb_(191, 115, 74)
        color.rgb_.vals = (51, 102, 153)
        assert color.rgb_.vals == (51, 102, 153)

    @pytest.mark.parametrize("attr", [
        "s", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_rgb_(191, 115, 74)
        with pytest.raises(AttributeError):
            setattr(color.rgb_, attr, 15)


@pytest.mark.parametrize("rgb_dict, expected", [
    ({"r": 91}, 0x5b734a),
    ({"g": 15}, 0xbf0f4a),
    ({"b": 174}, 0xbf73ae),
    ({"r": 91, "g": 15}, 0x5b0f4a),
    ({"r": 91, "b": 174}, 0x5b73ae),
    ({"g": 15, "b": 174}, 0xbf0fae),
    ({"r": 91, "g": 15, "b": 174}, 0x5b0fae),
])
def test_replace(rgb_dict, expected):
    color = Color.from_rgb_(191, 115, 74)
    assert int(color.rgb_.replace(**rgb_dict)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [51, 102, 153],
        (153, 51, 102),
    ])
    def test_setter_valid(self, vals):
        color = Color.from_rgb_(191, 115, 74)
        color.rgb_.vals = vals
        assert list(color.rgb_) == list(vals)

    @pytest.mark.parametrize("wrong_vals", [
        [51, 102],
        (153, 51, 102, 100),
        (408, 51, 102),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = Color.from_rgb_(191, 115, 74)
        with pytest.raises(ValueError):
            color.rgb_.vals = wrong_vals

    def test_getter(self):
        color = Color.from_rgb_(191, 115, 74)
        assert color.rgb_.vals == (191, 115, 74)
