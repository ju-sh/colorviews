import pytest

from colorviews import AlphaColor


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("h", 270),
        ("s", 47),
        ("v", 29),
        ("a", 79),
    ])
    def test_valid(self, attr, expected):
        color = AlphaColor.from_hsva_(270, 47, 29, 79)
        assert getattr(color.hsva_, attr) == expected

    @pytest.mark.parametrize("attr", [
        "r", "b",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_hsva_(270, 47, 29, 79)
        with pytest.raises(AttributeError):
            getattr(color.hsva_, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("h", 270),
        ("s", 50),
        ("v", 29),
        ("a", 49),
    ])
    def test_valid(self, attr, val):
        color = AlphaColor.from_hsva_(162, 15, 89, 79)
        setattr(color.hsva_, attr, val)
        assert getattr(color.hsva_, attr) == val

    @pytest.mark.parametrize("attr", [
        "r", "g",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_hsva_(270, 47, 29, 79)
        with pytest.raises(AttributeError):
            setattr(color.hsva_, attr, 0.1)


@pytest.mark.parametrize("hsva_dict, expected", [
    ({"h": 91}, 0x394a2980),
    ({"s": 15}, 0x443f4a80),
    ({"v": 74}, 0x9268bd80),
    ({"a": 80}, 0x39294acc),
    ({"h": 91, "s": 15}, 0x444a3f80),
    ({"h": 91, "v": 74}, 0x91bd6880),
    ({"h": 91, "v": 74, "a": 25}, 0x91bd6840),
    ({"s": 15, "v": 74}, 0xafa0bd80),
    ({"h": 91, "s": 15, "v": 74}, 0xaebda080),
])
def test_replace(hsva_dict, expected):
    color = AlphaColor.from_hsva_(270, 45, 29, 50)
    assert int(color.hsva_.replace(**hsva_dict)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [72, 40, 60, 10],
        (216, 20, 40, 54),
    ])
    def test_setter_valid(self, vals):
        color = AlphaColor.from_hsva_(270, 45, 29, 79)
        color.hsva_.vals = vals
        assert color.hsva_.vals == tuple(vals)

    @pytest.mark.parametrize("wrong_vals", [
        [0.2, 0.4],
        (1.6, 0.2, 0.4),
        (0.6, 0.2, 0.4, 1.0, 0.8),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = AlphaColor.from_hsva_(270, 45, 29, 79)
        with pytest.raises(ValueError):
            color.hsva_.vals = wrong_vals


def test_vals_getter():
    color = AlphaColor.from_hsva_(270, 45, 29, 79)
    assert color.hsva_.vals == (270, 45, 29, 79)
