import pytest

from colorviews import AlphaColor


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("h", 0.75),
        ("s", 0.47),
        ("v", 0.29),
        ("a", 0.79),
    ])
    def test_valid(self, attr, expected):
        color = AlphaColor.from_hsva(0.75, 0.47, 0.29, 0.79)
        assert round(getattr(color.hsva, attr), 4) == expected

    @pytest.mark.parametrize("attr", [
        "r", "b",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_hsva(0.75, 0.47, 0.29, 0.79)
        with pytest.raises(AttributeError):
            getattr(color.hsva, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("h", 0.75),
        ("s", 0.5),
        ("v", 0.29),
        ("a", 0.49),
    ])
    def test_valid(self, attr, val):
        color = AlphaColor.from_hsva(0.45, 0.15, 0.89, 0.79)
        setattr(color.hsva, attr, val)
        assert round(getattr(color.hsva, attr), 4) == val

    @pytest.mark.parametrize("attr", [
        "r", "g",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_hsva(0.75, 0.47, 0.29, 0.79)
        with pytest.raises(AttributeError):
            setattr(color.hsva, attr, 0.1)


@pytest.mark.parametrize("hsva_dict, expected", [
    ({"h": 91 / 360}, 0x394a2980),
    ({"s": 0.15}, 0x443f4a80),
    ({"v": 0.74}, 0x9268bd80),
    ({"a": 0.80}, 0x39294acc),
    ({"h": 91 / 360, "s": 0.15}, 0x444a3f80),
    ({"h": 91 / 360, "v": 0.74}, 0x91bd6880),
    ({"h": 91 / 360, "v": 0.74, "a": 0.25}, 0x91bd6840),
    ({"s": 0.15, "v": 0.74}, 0xafa0bd80),
    ({"h": 91 / 360, "s": 0.15, "v": 0.74}, 0xaebda080),
])
def test_replace(hsva_dict, expected):
    color = AlphaColor.from_hsva(0.75, 0.45, 0.29, 0.5)
    assert int(color.hsva.replace(**hsva_dict)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [0.2, 0.4, 0.6, 0.1],
        (0.6, 0.2, 0.4, 0.54),
    ])
    def test_setter_valid(self, vals):
        color = AlphaColor.from_hsva(0.75, 0.45, 0.29, 0.79)
        color.hsva.vals = vals
        assert [round(val, 4) for val in color.hsva] == list(vals)

    @pytest.mark.parametrize("wrong_vals", [
        [0.2, 0.4],
        (1.6, 0.2, 0.4),
        (0.6, 0.2, 0.4, 1.0, 0.8),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = AlphaColor.from_hsva(0.75, 0.45, 0.29, 0.79)
        with pytest.raises(ValueError):
            color.hsva.vals = wrong_vals


def test_vals_getter():
    vals = (0.75, 0.45, 0.29, 0.79)
    color = AlphaColor.from_hsva(0.75, 0.45, 0.29, 0.79)
    assert [round(val, 4) for val in color.hsva.vals] == list(vals)
