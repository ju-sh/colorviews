"""
ColorView classes for Color and AlphaColor objects

For Color:

 - ColorViewRGB
 - ColorViewHSL
 - ColorViewHSV

For AlphaColor:

 - ColorViewRGBA
 - ColorViewHSLA
 - ColorViewHSVA
"""

import colorsys

from typing import cast, List, Sequence, TYPE_CHECKING
import colorviews.utils as utils

if TYPE_CHECKING:
    import colorviews.colors as colors


class BaseColorView:
    """
    Base class of all ColorView classes.
    """
    __slots__ = ["color"]

    def __init__(self, color: "colors.BaseColor"):
        self.color = color


class BaseAlphaColorView(BaseColorView):
    """
    Base class of all ColorView classes with alpha value.
    """
    __slots__: List[str] = []

    @property
    def a(self) -> float:
        """Alpha component as a float value"""
        self.color = cast("colors.AlphaColor", self.color)
        return self.color._a

    @a.setter
    def a(self, val: float):
        utils.validate(val)
        self.color = cast("colors.AlphaColor", self.color)
        self.color._a = val


class BaseAlphaColorView_(BaseColorView):
    __slots__: List[str] = []

    @property
    def a(self) -> float:
        """Alpha component as a float value"""
        self.color = cast("colors.AlphaColor", self.color)
        return utils.scale(self.color._a, 100)

    @a.setter
    def a(self, val: float):
        intval = utils.validate_cent(val)
        self.color = cast("colors.AlphaColor", self.color)
        self.color._a = intval / 100


class BaseColorViewRGB_(BaseColorView):
    """
    Base class of ColorViewRGB_ and ColorViewRGBA_ classes.
    """
    __slots__: List[str] = []

    @property
    def r(self) -> float:
        """Red component as an int value"""
        return utils.scale(self.color._r, 255)

    @r.setter
    def r(self, val: float):
        uint_val = utils.validate_uint(val)
        self.color._r = uint_val / 255

    @property
    def g(self) -> float:
        """Green component as an int value"""
        return utils.scale(self.color._g, 255)

    @g.setter
    def g(self, val: float):
        uint_val = utils.validate_uint(val)
        self.color._g = uint_val / 255

    @property
    def b(self) -> float:
        """Blue component as an int value"""
        return utils.scale(self.color._b, 255)

    @b.setter
    def b(self, val: float):
        uint_val = utils.validate_uint(val)
        self.color._b = uint_val / 255


class ColorViewRGB_(BaseColorViewRGB_):
    """
    RGB view of Color objects in float values
    """
    __slots__: List[str] = []

    @property
    def vals(self) -> Sequence[float]:
        """
        Tuple of RGB values as floats.
        """
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[float]):
        if len(values) != 3:
            raise ValueError("Needs exactly 3 floats")
        r = utils.validate_uint(values[0])
        g = utils.validate_uint(values[1])
        b = utils.validate_uint(values[2])
        self.r, self.g, self.b = r, g, b

    def __iter__(self):
        yield from [self.r, self.g, self.b]

    def replace(self, r=None, g=None, b=None) -> "colors.Color":
        if r is None:
            r = self.r
        if g is None:
            g = self.g
        if b is None:
            b = self.b
        self.color = cast("colors.Color", self.color)
        return self.color.from_rgb_(r, g, b)


class ColorViewRGBA_(BaseColorViewRGB_, BaseAlphaColorView_):
    __slots__: List[str] = []

    @property
    def vals(self) -> Sequence[int]:
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[int]):
        if len(values) != 4:
            raise ValueError("Needs exactly 4 ints")
        r = utils.validate_uint(values[0])
        g = utils.validate_uint(values[1])
        b = utils.validate_uint(values[2])
        a = utils.validate_cent(values[3])
        self.r, self.g, self.b, self.a = r, g, b, a

    def __iter__(self):
        yield from [self.r, self.g, self.b, self.a]

    def replace(self, r=None, g=None, b=None, a=None) -> "colors.AlphaColor":
        if r is None:
            r = self.r
        if g is None:
            g = self.g
        if b is None:
            b = self.b
        if a is None:
            a = self.a
        self.color = cast("colors.AlphaColor", self.color)
        return self.color.from_rgba_(r, g, b, a)


class BaseColorViewRGB(BaseColorView):
    """
    Base class of ColorViewRGB and ColorViewRGBA classes.
    """
    __slots__: List[str] = []

    @property
    def r(self) -> float:
        """Red component as a float value"""
        return self.color._r

    @r.setter
    def r(self, val: float):
        utils.validate(val)
        self.color._r = val

    @property
    def g(self) -> float:
        """Green component as a float value"""
        return self.color._g

    @g.setter
    def g(self, val: float):
        utils.validate(val)
        self.color._g = val

    @property
    def b(self) -> float:
        """Blue component as a float value"""
        return self.color._b

    @b.setter
    def b(self, val: float):
        utils.validate(val)
        self.color._b = val


class ColorViewRGB(BaseColorViewRGB):
    """
    RGB view of Color objects in float values
    """
    __slots__: List[str] = []

    @property
    def vals(self) -> Sequence[float]:
        """
        Tuple of RGB values as floats.
        """
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[float]):
        if len(values) != 3:
            raise ValueError("Needs exactly 3 floats")
        utils.validate(values[0])
        utils.validate(values[1])
        utils.validate(values[2])
        self.r, self.g, self.b = values

    def __iter__(self):
        yield from [self.r, self.g, self.b]

    def replace(self, r=None, g=None, b=None) -> "colors.Color":
        """
        Create a new Color object by replacing the RGB values of the Color
        object associated with the colorview.

        Arguments:
          r: Red component of RGB value as a float in the range [0, 0.1].
          g: Green component of RGB value as a float in the range [0, 0.1].
          b: Blue component of RGB value as a float in the range [0, 0.1].

        Returns:
          Color object with modified RGB values.
        """
        if r is None:
            r = self.r
        if g is None:
            g = self.g
        if b is None:
            b = self.b
        self.color = cast("colors.Color", self.color)
        return self.color.from_rgb(r, g, b)


class ColorViewRGBA(BaseColorViewRGB, BaseAlphaColorView):
    """
    RGBA view of Color objects in float values
    """
    __slots__: List[str] = []

    @property
    def vals(self) -> Sequence[float]:
        """
        Tuple of RGBA values as floats.
        """
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[float]):
        if len(values) != 4:
            raise ValueError("Needs exactly 4 floats")
        utils.validate(values[0])
        utils.validate(values[1])
        utils.validate(values[2])
        utils.validate(values[3])
        self.r, self.g, self.b, self.a = values

    def __iter__(self):
        yield from [self.r, self.g, self.b, self.a]

    def replace(self, r=None, g=None, b=None, a=None) -> "colors.AlphaColor":
        """
        Create a new Color object by replacing the RGBA values of the Color
        object associated with the colorview.

        Arguments:
          r: Red component of RGBA value as a float in the range [0, 0.1].
          g: Green component of RGBA value as a float in the range [0, 0.1].
          b: Blue component of RGBA value as a float in the range [0, 0.1].
          a: Alpha component of RGBA value as a float in the range [0, 0.1].

        Returns:
          Color object with modified RGBA values.
        """
        if r is None:
            r = self.r
        if g is None:
            g = self.g
        if b is None:
            b = self.b
        if a is None:
            a = self.a
        self.color = cast("colors.AlphaColor", self.color)
        return self.color.from_rgba(r, g, b, a)

class BaseColorViewHSL_(BaseColorView):
    __slots__: List[str] = []

    @property
    def h(self):
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        return utils.scale(hls[0], 360)

    @h.setter
    def h(self, val: float):
        intval = utils.validate_angle(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        rgb = colorsys.hls_to_rgb(intval / 360, hls[1], hls[2])
        self.color._r, self.color._g, self.color._b = rgb

    @property
    def s(self):
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        return utils.scale(hls[2], 100)

    @s.setter
    def s(self, val: float):
        intval = utils.validate_cent(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        rgb = colorsys.hls_to_rgb(hls[0], hls[2], intval / 100)
        self.color._r, self.color._g, self.color._b = rgb

    @property
    def l(self):
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        return utils.scale(hls[1], 100)

    @l.setter
    def l(self, val: float):
        intval = utils.validate_cent(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        rgb = colorsys.hls_to_rgb(hls[0], intval / 100, hls[1])
        self.color._r, self.color._g, self.color._b = rgb


class ColorViewHSL_(BaseColorViewHSL_):
    __slots__: List[str] = []

    def __iter__(self):
        hls = colorsys.rgb_to_hls(*self.color.rgb.vals)
        h = utils.scale(hls[0], 360)
        s = utils.scale(hls[2], 100)
        l = utils.scale(hls[1], 100)
        yield from [h, s, l]

    @property
    def vals(self) -> Sequence[int]:
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[int]):
        if len(values) != 3:
            raise ValueError("Needs exactly 3 ints")
        h = utils.validate_angle(values[0])
        s = utils.validate_cent(values[1])
        l = utils.validate_cent(values[2])
        rgb = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
        #self.color = cast("colors.Color", self.color)
        self.color.rgb.vals = rgb

    def replace(self, h=None, s=None, l=None) -> "colors.Color":
        hsl = list(self)
        if h is None:
            h = hsl[0]
        if s is None:
            s = hsl[1]
        if l is None:
            l = hsl[2]
        self.color = cast("colors.Color", self.color)
        return self.color.from_hsl_(h, s, l)


class ColorViewHSLA_(BaseColorViewHSL_, BaseAlphaColorView_):
    __slots__: List[str] = []

    def __iter__(self):
        yield from [self.h, self.s, self.l, self.a]

    @property
    def vals(self) -> Sequence[int]:
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[int]):
        if len(values) != 4:
            raise ValueError("Needs exactly 4 ints")
        h = utils.validate_angle(values[0])
        s = utils.validate_cent(values[1])
        l = utils.validate_cent(values[2])
        a = utils.validate_cent(values[3])
        rgb = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
        self.color = cast("colors.AlphaColor", self.color)
        self.color.rgba.vals = rgb + (a / 100, )

    def replace(self, h=None, s=None, l=None, a=None) -> "colors.AlphaColor":
        hsla = list(self)
        if h is None:
            h = hsla[0]
        if s is None:
            s = hsla[1]
        if l is None:
            l = hsla[2]
        if a is None:
            a = hsla[3]
        self.color = cast("colors.AlphaColor", self.color)
        return self.color.from_hsla_(h, s, l, a)


class BaseColorViewHSL(BaseColorView):
    """
    Base class of ColorViewHSL and ColorViewHSLA classes.
    """
    __slots__: List[str] = []

    @property
    def h(self):
        """Hue component as a float value"""
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        return hls[0]

    @h.setter
    def h(self, val: float):
        utils.validate(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        rgb = colorsys.hls_to_rgb(val, hls[1], hls[2])
        self.color._r, self.color._g, self.color._b = rgb

    @property
    def s(self):
        """Saturation component as a float value"""
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        return hls[2]

    @s.setter
    def s(self, val: float):
        utils.validate(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        rgb = colorsys.hls_to_rgb(hls[0], hls[2], val)
        self.color._r, self.color._g, self.color._b = rgb

    @property
    def l(self):
        """Lightness component as a float value"""
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        return hls[1]

    @l.setter
    def l(self, val: float):
        utils.validate(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hls = colorsys.rgb_to_hls(*rgb)
        rgb = colorsys.hls_to_rgb(hls[0], val, hls[1])
        self.color._r, self.color._g, self.color._b = rgb


class ColorViewHSL(BaseColorViewHSL):
    """
    HSL view of Color objects in float values
    """
    __slots__: List[str] = []

    def __iter__(self):
        hls = colorsys.rgb_to_hls(*self.color.rgb.vals)
        yield from [hls[0], hls[2], hls[1]]

    @property
    def vals(self) -> Sequence[float]:
        """
        Tuple of HSL values as floats.
        """
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[float]):
        if len(values) != 3:
            raise ValueError("Needs exactly 3 floats")
        utils.validate(values[0])
        utils.validate(values[1])
        utils.validate(values[2])
        rgb = colorsys.hls_to_rgb(values[0], values[2], values[1])
        self.color = cast("colors.Color", self.color)
        self.color.rgb.vals = rgb

    def replace(self, h=None, s=None, l=None) -> "colors.Color":
        """
        Create a new Color object by replacing the HSL values of the Color
        object associated with the colorview.

        Arguments:
          h: Hue component of HSL value as a float in the range [0, 0.1].
          s: Saturation component of HSL value as a float in the
             range [0, 0.1].
          l: Lightness component of HSL value as a float in the range [0, 0.1].

        Returns:
          Color object with modified HSL values.
        """
        hsl = list(self)
        if h is None:
            h = hsl[0]
        if s is None:
            s = hsl[1]
        if l is None:
            l = hsl[2]
        self.color = cast("colors.Color", self.color)
        return self.color.from_hsl(h, s, l)


class ColorViewHSLA(BaseColorViewHSL, BaseAlphaColorView):
    """
    HSLA view of Color objects in float values
    """
    __slots__: List[str] = []

    def __iter__(self):
        yield from [self.h, self.s, self.l, self.a]

    @property
    def vals(self) -> Sequence[float]:
        """
        Tuple of HSLA values as floats.
        """
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[float]):
        if len(values) != 4:
            raise ValueError("Needs exactly 4 floats")
        utils.validate(values[0])
        utils.validate(values[1])
        utils.validate(values[2])
        utils.validate(values[3])
        rgb = colorsys.hls_to_rgb(values[0], values[2], values[1])
        self.color = cast("colors.AlphaColor", self.color)
        self.color.rgba.vals = rgb + (values[3], )

    def replace(self, h=None, s=None, l=None, a=None) -> "colors.AlphaColor":
        """
        Create a new AlphaColor object by replacing the HSLA values of the
        AlphaColor object associated with the colorview.

        Arguments:
          h: Hue component of HSLA value as a float in the range [0, 0.1].
          s: Saturation component of HSLA value as a float in the
             range [0, 0.1].
          l: Lightness component of HSLA value as a float in the
             range [0, 0.1].
          a: Alpha component of HSLA value as a float in the range [0, 0.1].

        Returns:
          AlphaColor object with modified HSLA values.
        """
        hsla = list(self)
        if h is None:
            h = hsla[0]
        if s is None:
            s = hsla[1]
        if l is None:
            l = hsla[2]
        if a is None:
            a = hsla[3]
        self.color = cast("colors.AlphaColor", self.color)
        return self.color.from_hsla(h, s, l, a)


class BaseColorViewHSV_(BaseColorView):
    __slots__: List[str] = []

    @property
    def h(self):
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        return utils.scale(hsv[0], 360)

    @h.setter
    def h(self, val: float):
        intval = utils.validate_angle(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        rgb = colorsys.hsv_to_rgb(intval / 360, hsv[1], hsv[2])
        self.color._r, self.color._g, self.color._b = rgb

    @property
    def s(self):
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        return utils.scale(hsv[1], 100)

    @s.setter
    def s(self, val: float):
        intval = utils.validate_cent(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        rgb = colorsys.hsv_to_rgb(hsv[0], intval / 100, hsv[2])
        self.color._r, self.color._g, self.color._b = rgb

    @property
    def v(self):
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        return utils.scale(hsv[2], 100)

    @v.setter
    def v(self, val: float):
        intval = utils.validate_cent(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], intval / 100)
        self.color._r, self.color._g, self.color._b = rgb


class ColorViewHSV_(BaseColorViewHSV_):
    __slots__: List[str] = []

    def __iter__(self):
        hsv = colorsys.rgb_to_hsv(*self.color.rgb.vals)
        h = utils.scale(hsv[0], 360)
        s = utils.scale(hsv[1], 100)
        v = utils.scale(hsv[2], 100)
        yield from [h, s, v]

    @property
    def vals(self) -> Sequence[int]:
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[int]):
        if len(values) != 3:
            raise ValueError("Needs exactly 3 ints")
        h = utils.validate_angle(values[0])
        s = utils.validate_cent(values[1])
        v = utils.validate_cent(values[2])
        rgb = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)
        #self.color = cast("colors.Color", self.color)
        self.color.rgb.vals = rgb

    def replace(self, h=None, s=None, v=None) -> "colors.Color":
        hsv = list(self)
        if h is None:
            h = hsv[0]
        if s is None:
            s = hsv[1]
        if v is None:
            v = hsv[2]
        self.color = cast("colors.Color", self.color)
        return self.color.from_hsv_(h, s, v)

class ColorViewHSVA_(BaseColorViewHSV_, BaseAlphaColorView_):
    __slots__: List[str] = []

    def __iter__(self):
        yield from [self.h, self.s, self.v, self.a]

    @property
    def vals(self) -> Sequence[int]:
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[int]):
        if len(values) != 4:
            raise ValueError("Needs exactly 4 ints")
        h = utils.validate_angle(values[0])
        s = utils.validate_cent(values[1])
        v = utils.validate_cent(values[2])
        a = utils.validate_cent(values[3])
        rgb = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)
        self.color = cast("colors.AlphaColor", self.color)
        self.color.rgba.vals = rgb + (a / 100, )

    def replace(self, h=None, s=None, v=None, a=None) -> "colors.AlphaColor":
        hsva = list(self)
        if h is None:
            h = hsva[0]
        if s is None:
            s = hsva[1]
        if v is None:
            v = hsva[2]
        if a is None:
            a = hsva[3]
        self.color = cast("colors.AlphaColor", self.color)
        return self.color.from_hsva_(h, s, v, a)

class BaseColorViewHSV(BaseColorView):
    """
    Base class of ColorViewHSV and ColorViewHSVA classes.
    """
    __slots__: List[str] = []

    @property
    def h(self):
        """Hue component as a float value"""
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        return hsv[0]

    @h.setter
    def h(self, val: float):
        utils.validate(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        rgb = colorsys.hsv_to_rgb(val, hsv[1], hsv[2])
        self.color._r, self.color._g, self.color._b = rgb

    @property
    def s(self):
        """Saturation component as a float value"""
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        return hsv[1]

    @s.setter
    def s(self, val: float):
        utils.validate(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        rgb = colorsys.hsv_to_rgb(hsv[0], val, hsv[2])
        self.color._r, self.color._g, self.color._b = rgb

    @property
    def v(self):
        """Value component as a float value"""
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        return hsv[2]

    @v.setter
    def v(self, val: float):
        utils.validate(val)
        rgb = (self.color._r, self.color._g, self.color._b)
        hsv = colorsys.rgb_to_hsv(*rgb)
        rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], val)
        self.color._r, self.color._g, self.color._b = rgb


class ColorViewHSV(BaseColorViewHSV):
    """
    HSV view of Color objects in float values
    """
    __slots__: List[str] = []

    def __iter__(self):
        hsv = colorsys.rgb_to_hsv(*self.color.rgb.vals)
        yield from hsv

    @property
    def vals(self) -> Sequence[float]:
        """
        Tuple of HSV values as floats.
        """
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[float]):
        if len(values) != 3:
            raise ValueError("Needs exactly 3 floats")
        utils.validate(values[0])
        utils.validate(values[1])
        utils.validate(values[2])
        rgb = colorsys.hsv_to_rgb(values[0], values[1], values[2])
        self.color = cast("colors.Color", self.color)
        self.color.rgb.vals = rgb

    def replace(self, h=None, s=None, v=None) -> "colors.Color":
        """
        Create a new Color object by replacing the HSV values of the Color
        object associated with the colorview.

        Arguments:
          h: Hue component of HSV value as a float in the range [0, 0.1].
          s: Saturation component of HSV value as a float in the
             range [0, 0.1].
          v: Value component of HSV value as a float in the range [0, 0.1].

        Returns:
          Color object with modified HSV values.
        """
        hsv = list(self)
        if h is None:
            h = hsv[0]
        if s is None:
            s = hsv[1]
        if v is None:
            v = hsv[2]
        self.color = cast("colors.Color", self.color)
        return self.color.from_hsv(h, s, v)


class ColorViewHSVA(BaseColorViewHSV, BaseAlphaColorView):
    """
    HSVA view of Color objects in float values
    """
    __slots__: List[str] = []

    def __iter__(self):
        yield from [self.h, self.s, self.v, self.a]

    @property
    def vals(self) -> Sequence[float]:
        """
        Tuple of HSVA values as floats.
        """
        return tuple(self)

    @vals.setter
    def vals(self, values: Sequence[float]):
        if len(values) != 4:
            raise ValueError("Needs exactly 4 floats")
        utils.validate(values[0])
        utils.validate(values[1])
        utils.validate(values[2])
        utils.validate(values[3])
        rgb = colorsys.hsv_to_rgb(values[0], values[1], values[2])
        self.color = cast("colors.AlphaColor", self.color)
        self.color.rgba.vals = rgb + (values[3], )

    def replace(self, h=None, s=None, v=None, a=None) -> "colors.AlphaColor":
        """
        Create a new AlphaColor object by replacing the HSVA values of the
        AlphaColor object associated with the colorview.

        Arguments:
          h: Hue component of HSVA value as a float in the range [0, 0.1].
          s: Saturation component of HSVA value as a float in the
             range [0, 0.1].
          v: Value component of HSVA value as a float in the
             range [0, 0.1].
          a: Alpha component of HSVA value as a float in the range [0, 0.1].

        Returns:
          AlphaColor object with modified HSVA values.
        """
        hsva = list(self)
        if h is None:
            h = hsva[0]
        if s is None:
            s = hsva[1]
        if v is None:
            v = hsva[2]
        if a is None:
            a = hsva[3]
        self.color = cast("colors.AlphaColor", self.color)
        return self.color.from_hsva(h, s, v, a)
