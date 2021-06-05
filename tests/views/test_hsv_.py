import pytest

from colorviews import Color


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("h", 270),
        ("s", 47),
        ("v", 29),
    ])
    def test_valid(self, attr, expected):
        color = Color.from_hsv_(270, 47, 29)
        assert getattr(color.hsv_, attr) == expected

    @pytest.mark.parametrize("attr", [
        "r", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_hsv_(270, 47, 29)
        with pytest.raises(AttributeError):
            getattr(color.hsv_, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("h", 270),
        ("s", 50),
        ("v", 29),
    ])
    def test_valid(self, attr, val):
        color = Color.from_hsv_(162, 15, 89)
        setattr(color.hsv_, attr, val)
        assert getattr(color.hsv_, attr) == val

    @pytest.mark.parametrize("val, expected", [
        (570, 210),
        (-270, 90),
    ])
    def test_valid_round_h(self, val, expected):
        color = Color.from_hsv_(270, 47, 29)
        color.hsv_.h = val
        assert color.hsv_.h == expected

    @pytest.mark.parametrize("attr", [
        "r", "a",
    ])
    def test_invalid(self, attr):
        color = Color.from_hsv_(270, 47, 29)
        with pytest.raises(AttributeError):
            setattr(color.hsv_, attr, 0.1)


@pytest.mark.parametrize("hsv_dict, expected", [
    ({"h": 91}, 0x394a29),
    ({"s": 15}, 0x443f4a),
    ({"v": 74}, 0x9268bd),
    ({"h": 91, "s": 15}, 0x444a3f),
    ({"h": 91, "v": 74}, 0x91bd68),
    ({"s": 15, "v": 74}, 0xafa0bd),
    ({"h": 91, "s": 15, "v": 74}, 0xaebda0),
])
def test_replace(hsv_dict, expected):
    color = Color.from_hsv_(270, 45, 29)
    assert int(color.hsv_.replace(**hsv_dict)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [72, 40, 60],
        (216, 20, 40),
    ])
    def test_setter_valid(self, vals):
        color = Color.from_hsv_(270, 45, 29)
        color.hsv_.vals = vals
        assert list(color.hsv_) == list(vals)

    def test_setter_valid_round_h(self):
        color = Color.from_hsv_(270, 45, 29)
        color.hsv_.vals = (576, 20, 40)
        assert color.hsv_.vals == (216, 20, 40)

    @pytest.mark.parametrize("wrong_vals", [
        [72, 40],
        (216, 20, 40, 100),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = Color.from_hsv_(270, 45, 29)
        with pytest.raises(ValueError):
            color.hsv_.vals = wrong_vals


def test_vals_getter():
    color = Color.from_hsv_(270, 45, 29)
    assert color.hsv_.vals == (270, 45, 29)
