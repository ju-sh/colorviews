import pytest
from colorviews import Color, AlphaColor


class TestComparisons:
    def test_eq(self):
        color_a = Color.from_int(0xefab3)
        color_b = Color.from_int(0xefab3)
        assert color_a == color_b

    def test_ne(self):
        color_a = Color.from_int(0xefab3)
        color_b = Color.from_int(0xffab3)
        assert color_a != color_b

    def test_lt(self):
        color_a = Color.from_int(0xefab3)
        color_b = Color.from_int(0xffab3)
        assert color_a < color_b

    def test_le(self):
        color_a = Color.from_int(0xefab3)
        color_b = Color.from_int(0xefab3)
        assert color_a <= color_b

    def test_gt(self):
        color_a = Color.from_int(0xffab3)
        color_b = Color.from_int(0xefab3)
        assert color_a > color_b

    def test_ge(self):
        color_a = Color.from_int(0xefab3)
        color_b = Color.from_int(0xefab3)
        assert color_a >= color_b

    @pytest.mark.parametrize("func,arg", [
        ("__lt__", 12),
        ("__le__", "string"),
        ("__gt__", 12),
        ("__ge__", 12),
        ("__eq__", 12),
        ("__ne__", 1.2),
    ])
    def test_invalid_comparison(self, func, arg):
        color = Color.from_int(0xefab3)
        assert getattr(color, func)(arg) == NotImplemented

    @pytest.mark.parametrize("func", [
        "__lt__",
        "__le__",
        "__gt__",
        "__ge__",
        "__eq__",
        "__ne__",
    ])
    def test_alphacolor_comparison(self, func):
        color = Color.from_int(0xefab3)
        alphacolor = AlphaColor.from_name("red")
        assert getattr(color, func)(alphacolor) == NotImplemented


class TestFromInt:
    @pytest.mark.parametrize("colorint, rgb", [
        (0x5b734a, [0.3569, 0.4510, 0.2902]),
        (0xbf0f4a, [0.7490, 0.0588, 0.2902]),
    ])
    def test_valid(self, colorint, rgb):
        color = Color.from_int(colorint)
        rounded_comps = [round(comp, 4) for comp in color.rgb]
        assert rounded_comps == rgb

    @pytest.mark.parametrize("colorint", [
        0x1fabcdef,
        -234,
    ])
    def test_invalid(self, colorint):
        with pytest.raises(ValueError):
            Color.from_int(colorint)


class TestFromRGB:
    def test_valid(self):
        assert int(Color.from_rgb(0.6, 0.2, 0.8)) == 0x9933cc

    def test_invalid(self):
        with pytest.raises(ValueError):
            Color.from_rgb(0.6, 0.2, 0xcc)


class TestFromHSL:
    def test_valid(self):
        assert int(Color.from_hsl(0.625, 0.15, 0.74)) == 0xb3b8c7

    def test_invalid(self):
        with pytest.raises(ValueError):
            Color.from_hsl(25, 1.0, 0.74)


class TestFromHSV:
    def test_valid(self):
        assert int(Color.from_hsv(0.625, 0.15, 0.74)) == 0xa0a7bd

    def test_invalid(self):
        with pytest.raises(ValueError):
            Color.from_hsv(25, 1.0, 0.74)


def test_str():
    color = Color.from_int(0xabcdef)
    assert str(color) == "abcdef"


def test_repr():
    color = Color.from_int(0xabcdef)
    assert repr(color) == "<Color(0xabcdef)>"


def test_hex():
    color = Color.from_int(0xabcdef)
    assert hex(color) == "0xabcdef"


def test_from_name():
    color = Color.from_name("gray")
    assert int(color) == 0x808080


def test_from_rgb():
    assert int(Color.from_rgb(0.3569, 0.4510, 0.2902)) == 0x5b734a


def test_from_hsl():
    assert int(Color.from_hsl(0.2583, 0.1515, 0.7412)) == 0xbcc7b3


def test_copy():
    orig = Color.from_hsl(0.2583, 0.1515, 0.7412)
    copy = orig.copy()
    assert id(orig) != id(copy)
    assert orig.rgb.vals == copy.rgb.vals
