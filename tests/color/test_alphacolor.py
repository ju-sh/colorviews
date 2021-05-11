import pytest
from colorviews import AlphaColor


class TestComparisons:
    def test_eq(self):
        color_a = AlphaColor.from_int(0xefab332)
        color_b = AlphaColor.from_int(0xefab332)
        assert color_a == color_b

    def test_ne(self):
        color_a = AlphaColor.from_int(0xffab322)
        color_b = AlphaColor.from_int(0xffab323)
        assert color_a != color_b

    def test_lt(self):
        color_a = AlphaColor.from_int(0xefab380)
        color_b = AlphaColor.from_int(0xffab3ef)
        assert color_a < color_b

    def test_le(self):
        color_a = AlphaColor.from_int(0xefab332)
        color_b = AlphaColor.from_int(0xefab332)
        assert color_a <= color_b

    def test_gt(self):
        color_a = AlphaColor.from_int(0xffab332)
        color_b = AlphaColor.from_int(0xefab332)
        assert color_a > color_b

    def test_ge(self):
        color_a = AlphaColor.from_int(0xefab321)
        color_b = AlphaColor.from_int(0xefab321)
        assert color_a >= color_b


class TestFromInt:
    @pytest.mark.parametrize("colorint, rgba", [
        # can't get exact 0.5 for alpha here
        (0x5b734a80, [0.3569, 0.4510, 0.2902, 0.502]),

        (0xbf0f4abf, [0.7490, 0.0588, 0.2902, 0.749]),
    ])
    def test_valid(self, colorint, rgba):
        color = AlphaColor.from_int(colorint)
        rounded_comps = [round(comp, 4) for comp in color.rgba]
        assert rounded_comps == rgba

    @pytest.mark.parametrize("colorint", [
        0xa1fabcdef,
        -234,
    ])
    def test_invalid(self, colorint):
        with pytest.raises(ValueError):
            AlphaColor.from_int(colorint)


class TestFromRGBA:
    def test_valid(self):
        assert int(AlphaColor.from_rgba(0.6, 0.2, 0.8, 0.8)) == 0x9933cccc

    def test_invalid(self):
        with pytest.raises(ValueError):
            AlphaColor.from_rgba(0.6, 0.2, 0xcc, 0.1)


class TestFromHSLA:
    def test_valid(self):
        assert int(AlphaColor.from_hsla(0.625, 0.15, 0.74, 0.8)) == 0xb3b8c7cc

    def test_invalid(self):
        with pytest.raises(ValueError):
            AlphaColor.from_hsla(25, 1.0, 0.74, 0.8)


class TestFromHSVA:
    def test_valid(self):
        assert int(AlphaColor.from_hsva(0.625, 0.15, 0.74, 0.8)) == 0xa0a7bdcc

    def test_invalid(self):
        with pytest.raises(ValueError):
            AlphaColor.from_hsva(25, 1.0, 0.74, 0.8)


def test_hex():
    color = AlphaColor.from_int(0xabcdef12)
    assert hex(color) == "0xabcdef12"


@pytest.mark.parametrize("name, a, expected", [
    ("gray", 0.0, 0x80808000),
    ("red", 0.4, 0xff000066),
])
def test_from_name(name, a, expected):
    color = AlphaColor.from_name(name, a)
    assert int(color) == expected


def test_copy():
    orig = AlphaColor.from_hsla(0.2583, 0.1515, 0.7412, 0.25)
    copy = orig.copy()
    assert id(orig) != id(copy)
    assert orig.rgba.vals == copy.rgba.vals
