import pytest
from colorviews import AlphaColor


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
