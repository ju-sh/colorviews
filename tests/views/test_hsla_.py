import pytest

from colorviews import AlphaColor


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("h", 270),
        ("s", 47),
        ("l", 29),
        ("a", 79),
    ])
    def test_valid(self, attr, expected):
        color = AlphaColor.from_hsla_(270, 47, 29, 79)
        assert getattr(color.hsla_, attr) == expected

    @pytest.mark.parametrize("attr", [
        "r", "b",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_hsla_(270, 47, 29, 79)
        with pytest.raises(AttributeError):
            getattr(color.hsla_, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("h", 270),
        ("s", 50),
        ("l", 29),
        ("a", 49),
    ])
    def test_valid(self, attr, val):
        color = AlphaColor.from_hsla_(162, 15, 89, 79)
        setattr(color.hsla_, attr, val)
        assert getattr(color.hsla_, attr) == val

    @pytest.mark.parametrize("attr", [
        "r", "g",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_hsla_(270, 47, 29, 79)
        with pytest.raises(AttributeError):
            setattr(color.hsla_, attr, 10)


@pytest.mark.parametrize("hsla_dict, expected", [
    ({"h": 91}, 0x496b2980),
    ({"s": 15}, 0x4a3f5580),
    ({"l": 74}, 0xbd9fdb80),
    ({"a": 80}, 0x4a296bcc),
    ({"h": 91, "s": 15}, 0x4a553f80),
    ({"h": 91, "l": 74}, 0xbcdb9f80),
    ({"h": 91, "l": 74, "a": 25}, 0xbcdb9f40),
    ({"s": 15, "l": 74}, 0xbdb3c780),
    ({"h": 91, "s": 15, "l": 74}, 0xbcc7b380),
])
def test_replace(hsla_dict, expected):
    color = AlphaColor.from_hsla_(270, 45, 29, 50)
    assert int(color.hsla_.replace(**hsla_dict)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [72, 40, 60, 10],
        (216, 20, 40, 54),
    ])
    def test_setter_valid(self, vals):
        color = AlphaColor.from_hsla_(270, 45, 29, 79)
        color.hsla_.vals = vals
        assert color.hsla_.vals == tuple(vals)

    def test_setter_valid_round_h(self):
        color = AlphaColor.from_hsla_(270, 45, 29, 79)
        color.hsla_.vals = (576, 20, 40, 89)
        assert color.hsla_.vals == (216, 20, 40, 89)

    @pytest.mark.parametrize("wrong_vals", [
        [72, 40],
        (216, 20, 40, 100, 80),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = AlphaColor.from_hsla_(270, 45, 29, 79)
        with pytest.raises(ValueError):
            color.hsla_.vals = wrong_vals


def test_vals_getter():
    color = AlphaColor.from_hsla_(270, 45, 29, 79)
    assert color.hsla_.vals == (270, 45, 29, 79)
