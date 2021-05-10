import pytest

from colorviews import Color


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("h", 0.75),
        ("s", 0.47),
        ("v", 0.29),
    ])
    def test_valid(self, attr, expected):
        color = Color.from_hsv(0.75, 0.47, 0.29)
        assert round(getattr(color.hsv, attr), 4) == expected

    @pytest.mark.parametrize("attr", [
        "r", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_hsv(0.75, 0.47, 0.29)
        with pytest.raises(AttributeError):
            getattr(color.hsv, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("h", 0.75),
        ("s", 0.5),
        ("v", 0.29),
    ])
    def test_valid(self, attr, val):
        color = Color.from_hsv(0.45, 0.15, 0.89)
        setattr(color.hsv, attr, val)
        assert round(getattr(color.hsv, attr), 4) == val

    @pytest.mark.parametrize("attr", [
        "r", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_hsv(0.75, 0.47, 0.29)
        with pytest.raises(AttributeError):
            setattr(color.hsv, attr, 0.1)


@pytest.mark.parametrize("hsv_dict, expected", [
    ({"h": 91 / 360}, 0x394a29),
    ({"s": 0.15}, 0x443f4a),
    ({"v": 0.74}, 0x9268bd),
    ({"h": 91 / 360, "s": 0.15}, 0x444a3f),
    ({"h": 91 / 360, "v": 0.74}, 0x91bd68),
    ({"s": 0.15, "v": 0.74}, 0xafa0bd),
    ({"h": 91 / 360, "s": 0.15, "v": 0.74}, 0xaebda0),
])
def test_replace(hsv_dict, expected):
    color = Color.from_hsv(0.75, 0.45, 0.29)
    assert int(color.hsv.replace(**hsv_dict)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [0.2, 0.4, 0.6],
        (0.6, 0.2, 0.4),
    ])
    def test_setter_valid(self, vals):
        color = Color.from_hsv(0.75, 0.45, 0.29)
        color.hsv.vals = vals
        assert [round(val, 4) for val in color.hsv] == list(vals)

    @pytest.mark.parametrize("wrong_vals", [
        [0.2, 0.4],
        (0.6, 0.2, 0.4, 1.0),
        (1.6, 0.2, 0.4),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = Color.from_hsv(0.75, 0.45, 0.29)
        with pytest.raises(ValueError):
            color.hsv.vals = wrong_vals


def test_vals_getter():
    color = Color.from_hsv(0.75, 0.45, 0.29)
    assert [round(val, 4) for val in color.hsv.vals] == [0.75, 0.45, 0.29]
