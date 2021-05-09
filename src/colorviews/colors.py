"""
Classes to represent colors with and without alpha value.

Color represents color values without alpha and AlphaColor represents color
values that have alpha.
"""

import colorsys

import colorviews.names
import colorviews.views
import colorviews.utils as utils


class BaseColor:
    """
    Base class of all Color classes.
    """
    def __lt__(self, other: object):
        if isinstance(other, self.__class__):
            return int(self) < int(other)
        return NotImplemented

    def __le__(self, other: object):
        if isinstance(other, self.__class__):
            return int(self) <= int(other)
        return NotImplemented

    def __eq__(self, other: object):
        if isinstance(other, self.__class__):
            return int(self) == int(other)
        return NotImplemented

    def __ne__(self, other: object):
        if isinstance(other, self.__class__):
            return int(self) != int(other)
        return NotImplemented

    def __gt__(self, other: object):
        if isinstance(other, self.__class__):
            return int(self) > int(other)
        return NotImplemented

    def __ge__(self, other: object):
        if isinstance(other, self.__class__):
            return int(self) >= int(other)
        return NotImplemented

    def __init__(self,
                 r: float,
                 g: float,
                 b: float):
        utils.validate(r)
        utils.validate(g)
        utils.validate(b)
        self._r = r
        self._g = g
        self._b = b

    def __int__(self):
        red = utils.multround(self._r, 0xff)
        green = utils.multround(self._g, 0xff)
        blue = utils.multround(self._b, 0xff)
        intval = ((red << 16) | (green << 8) | blue)
        return intval

    def __str__(self):
        # integer color value in hex form as a string with any prefix
        return f"{int(self):x}"

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"<{cls_name}(0x{int(self):x})>"

    def __index__(self):
        # for hex()
        return int(self)


class Color(BaseColor):
    """
    Class representing colors without alpha value.

    Information is stored using rgb values.
    """
    @property
    def rgb(self):
        """RGB colorview as float values"""
        return colorviews.views.ColorViewRGB(self)

    @property
    def hsl(self):
        """HSL colorview as float values"""
        return colorviews.views.ColorViewHSL(self)

    @classmethod
    def from_name(cls, name: str) -> 'Color':
        """
        Creates a Color object based on the given color name.

        Only CSS3 extended color keyword names are recognized.

        Arguments:
          name: Name of color.

        Returns:
          Color object with value corresponding to the given color name.
        """
        name = name.lower()
        return cls.from_int(colorviews.names.COLORS[name])

    @classmethod
    def from_int(cls, value: int):
        """
        Creates a Color object from the given integer color value.

        Arguments:
          value: Integer color value.

        Returns:
          Color object with given integer value.

        Raises:
          ValueError: If value is outside the valid range.
        """
        if value < 0 or value > 0xffffff:
            raise ValueError(f"{value}: invalid color value")
        red = ((value >> 16) & 0xff) / 0xff
        green = ((value >> 8) & 0xff) / 0xff
        blue = (value & 0xff) / 0xff
        return cls(red, green, blue)

    @classmethod
    def from_rgb(cls, r: float, g: float, b: float) -> "Color":
        """
        Creates a Color object from the given RGB float values.

        Arguments:
          r: Red component of RGB value as a float in the range [0.0, 1.0]
          g: Green component of RGB value as a float in the range [0.0, 1.0]
          b: Blue component of RGB value as a float in the range [0.0, 1.0]

        Returns:
          Color object with given RGB values.

        Raises:
          ValueError: If value is outside the valid range.
        """
        return cls(r, g, b)

    @classmethod
    def from_hsl(cls, h: float, s: float, l: float) -> "Color":
        """
        Creates a Color object from the given HSL float values.

        Arguments:
          h: Hue component of HSL value as a float in the range [0.0, 1.0]
          s: Saturation component of HSL value as a float in the
             range [0.0, 1.0]
          l: Lightness component of HSL value as a float in the
             range [0.0, 1.0]

        Returns:
          Color object with given HSL values.

        Raises:
          ValueError: If any argument is outside valid range.
        """
        utils.validate(h)
        utils.validate(s)
        utils.validate(l)
        rgb = colorsys.hls_to_rgb(h, l, s)
        return cls(*rgb)


class AlphaColor(BaseColor):
    """
    Class representing colors with alpha value.

    Information is stored using rgba values.
    """
    def __init__(self,
                 r: float,
                 g: float,
                 b: float,
                 a: float):
        super().__init__(r, g, b)
        utils.validate(a)
        self._a = a

    def __int__(self):
        alpha = utils.multround(self._a, 0xff)
        nonalphaint = super().__int__()
        intval = (nonalphaint << 8) | alpha
        return intval

    @property
    def rgba(self):
        """RGBA colorview as float values"""
        return colorviews.views.ColorViewRGBA(self)

    @property
    def hsla(self):
        """HSLA colorview as float values"""
        return colorviews.views.ColorViewHSLA(self)

    @classmethod
    def from_name(cls, name: str) -> "AlphaColor":
        """
        Creates an AlphaColor object based on the given color name.

        Only CSS3 extended color keyword names are recognized.
        Returned AlphaColor would be totally transparent with alpha value 0.

        Arguments:
          name: Name of color.

        Returns:
          AlphaColor object with value corresponding to the given color name.
        """
        name = name.lower()
        rgbintval = colorviews.names.COLORS[name]
        return cls.from_int(rgbintval << 8)  # by default transparent

    @classmethod
    def from_int(cls, value: int) -> "AlphaColor":
        """
        Creates an AlphaColor object from the given integer color value.

        Arguments:
          value: Integer color value.

        Returns:
          AlphaColor object with given integer value.

        Raises:
          ValueError: If value is outside the valid range.
        """
        if value < 0 or value > 0xffffffff:
            raise ValueError(f"{value}: invalid alphacolor value")
        red = ((value >> 24) & 0xff) / 0xff
        green = ((value >> 16) & 0xff) / 0xff
        blue = ((value >> 8) & 0xff) / 0xff
        alpha = (value & 0xff) / 0xff
        return cls(red, green, blue, alpha)

    @classmethod
    def from_rgba(cls, r: float, g: float, b: float, a: float) -> "AlphaColor":
        """
        Creates an AlphaColor object from the given RGBA float values.

        Arguments:
          r: Red component of RGBA value as a float in the range [0.0, 1.0].
          g: Green component of RGBA value as a float in the range [0.0, 1.0].
          b: Blue component of RGBA value as a float in the range [0.0, 1.0].
          a: Alpha component of RGBA value as a float in the range [0.0, 1.0].

        Returns:
          AlphaColor object with given RGBA values.

        Raises:
          ValueError: If value is outside the valid range.
        """
        return cls(r, g, b, a)

    @classmethod
    def from_hsla(cls, h: float, s: float, l: float, a: float) -> "AlphaColor":
        """
        Creates an AlphaColor object from the given HSLA float values.

        Arguments:
          h: Hue component of HSLA value as a float in the range [0.0, 1.0]
          s: Saturation component of HSLA value as a float in the
             range [0.0, 1.0].
          l: Lightness component of HSLA value as a float in the
             range [0.0, 1.0].
          a: Alpha component of HSLA value as a float in the range [0.0, 1.0].

        Returns:
          AlphaColor object with given HSLA values.

        Raises:
          ValueError: If value is outside the valid range.
        """
        utils.validate(h)
        utils.validate(s)
        utils.validate(l)
        utils.validate(a)
        rgba = colorsys.hls_to_rgb(h, l, s) + (a, )
        return cls(*rgba)
