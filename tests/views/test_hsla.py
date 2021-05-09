import pytest

from colorviews import AlphaColor


class TestGetAttr:
    @pytest.mark.parametrize("attr, expected", [
        ("h", 0.75),
        ("s", 0.47),
        ("l", 0.29),
        ("a", 0.79),
    ])
    def test_valid(self, attr, expected):
        color = AlphaColor.from_hsla(0.75, 0.47, 0.29, 0.79)
        assert round(getattr(color.hsla, attr), 4) == expected

    @pytest.mark.parametrize("attr", [
        "r", "b",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_hsla(0.75, 0.47, 0.29, 0.79)
        with pytest.raises(AttributeError):
            getattr(color.hsla, attr)


class TestSetAttr:
    @pytest.mark.parametrize("attr, val", [
        ("h", 0.75),
        ("s", 0.5),
        ("l", 0.29),
        ("a", 0.49),
    ])
    def test_valid(self, attr, val):
        color = AlphaColor.from_hsla(0.45, 0.15, 0.89, 0.79)
        setattr(color.hsla, attr, val)
        assert round(getattr(color.hsla, attr), 4) == val

    @pytest.mark.parametrize("attr", [
        "r", "g",
    ])
    def test_invalid(self, attr):
        color = AlphaColor.from_hsla(0.75, 0.47, 0.29, 0.79)
        with pytest.raises(AttributeError):
            setattr(color.hsla, attr, 0.1)


@pytest.mark.parametrize("hsla_dict, expected", [
    ({"h": 91 / 360}, 0x496b2980),
    ({"s": 0.15}, 0x4a3f5580),
    ({"l": 0.74}, 0xbd9fdb80),
    ({"a": 0.80}, 0x4a296bcc),
    ({"h": 91 / 360, "s": 0.15}, 0x4a553f80),
    ({"h": 91 / 360, "l": 0.74}, 0xbcdb9f80),
    ({"h": 91 / 360, "l": 0.74, "a": 0.25}, 0xbcdb9f40),
    ({"s": 0.15, "l": 0.74}, 0xbdb3c780),
    ({"h": 91 / 360, "s": 0.15, "l": 0.74}, 0xbcc7b380),
])
def test_replace(hsla_dict, expected):
    color = AlphaColor.from_hsla(0.75, 0.45, 0.29, 0.5)
    assert int(color.hsla.replace(**hsla_dict)) == expected


class TestVals:
    @pytest.mark.parametrize("vals", [
        [0.2, 0.4, 0.6, 0.1],
        (0.6, 0.2, 0.4, 0.54),
    ])
    def test_setter_valid(self, vals):
        color = AlphaColor.from_hsla(0.75, 0.45, 0.29, 0.79)
        color.hsla.vals = vals
        assert [round(val, 4) for val in color.hsla] == list(vals)

    @pytest.mark.parametrize("wrong_vals", [
        [0.2, 0.4],
        (1.6, 0.2, 0.4),
        (0.6, 0.2, 0.4, 1.0, 0.8),
    ])
    def test_setter_invalid(self, wrong_vals):
        color = AlphaColor.from_hsla(0.75, 0.45, 0.29, 0.79)
        with pytest.raises(ValueError):
            color.hsla.vals = wrong_vals


def test_vals_getter():
    vals = (0.75, 0.45, 0.29, 0.79)
    color = AlphaColor.from_hsla(0.75, 0.45, 0.29, 0.79)
    assert [round(val, 4) for val in color.hsla.vals] == list(vals)
