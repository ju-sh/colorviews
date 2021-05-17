# colorviews

A module to handle colors.

---

# Quickstart
Colors may be represented using `Color` (for colors without alpha value) and `AlphaColor` (for colors with alpha value) objects.

All colors are stored internally using their RGB(A) values and are converted to other color schemes when needed using appropriate ColorView objects.

 - `ColorViewRGB`: RGB color view for `Color` objects.
 - `ColorViewHSL`: HSL color view for `Color` objects.
 - `ColorViewHSV`: HSV color view for `Color` objects.
 - `ColorViewRGBA`: RGBA color view for `AlphaColor` objects.
 - `ColorViewHSLA`: HSLA color view for `AlphaColor` objects.
 - `ColorViewHSVA`: HSVA color view for `AlphaColor` objects.

All color component values are handled as float values between and including 0.0 and 1.0.

These float values may be converted to their integer equivalent using `scale()`function of the colorviews package.

## Creating Color objects
`Color` objects can be created in one of the following ways.

### From RGB values
With constructor or `Color.from_rgb(r: float, g: float, b: float)`.

    from colorviews import Color
    color = Color(0.2, 0.4, 0.8)  # <Color(0x3366cc)>
    color = Color.from_rgb(0.2, 0.4, 0.8)  # <Color(0x3366cc)>

### From color RGB integer value
With `Color.from_int(value: int)`.

    from colorviews import Color
    color = Color.from_int(0xabcdef)  # <Color(<Color(0xabcdef)>)>

### From HSL values
With `Color.from_hsl(h: float, s: float, l: float)`.

    from colorviews import Color
    color = Color.from_hsl(0.5, 1.0, 0.52)  # <Color(0xaffff)>

### From HSV values
With `Color.from_hsv(h: float, s: float, v: float)`.

    from colorviews import Color
    color = Color.from_hsv(0.5, 1.0, 0.52)  # <Color(0x8585)>

### From color name
With `Color.from_name()`.

[CSS3 extended color keywords](https://www.w3.org/wiki/CSS3/Color/Extended_color_keywords) are recognized.

Case of the color name doesn't matter.

    from colorviews import Color
    color = Color.from_name("darkgrey")  # <Color(0xa9a9a9)>

## Accessing color component values
### Hex value of color

    from colorviews import Color
    color = Color.from_int(0xabcdef)  # <Color(0xabcdef)>
    hex(color)  # '0xabcdef'
    str(color)  # 'abcdef'

### RGB color view
RGB color view has the following attributes which may be read or written:

 - `r`: red component of RGB color value.
 - `g`: green component of RGB color value.
 - `b`: blue component of RGB color value.
 - `vals`: red, green and blue components as a tuple.

```
from colorviews import Color
color = Color.from_int(0xabcdef)  # <Color(0xabcdef)>

# Red component
color.rgb.r  # 0.6705882352941176

# Green component
color.rgb.g  # 0.803921568627451

# Blue component
color.rgb.b  # 0.9372549019607843

# All RGB components as a tuple
color.rgb.vals  # (0.6705882352941176, 0.803921568627451,
                #  0.9372549019607843)

# New red component value
color.rgb.r = 0.52
color.rgb.vals  # (0.52, 0.803921568627451, 0.9372549019607843)

# Change all RGB values
color.rgb.vals = (0.25, 0.50, 0.75)
color  # <Color(0x4080bf)>
```

### HSL color view
HSL color view has the following attributes which may be read or written:

 - `h`: hue component of HSL color value.
 - `s`: saturation component of HSL color value.
 - `l`: lightness component of HSL color value.
 - `vals`: hue, saturation and lightness components as a tuple.

```
from colorviews import Color
color = Color.from_int(0xabcdef)  # <Color(0xabcdef)>

# Hue component
color.hsl.h  # 0.5833333333333334

# Saturation component
color.hsl.s  # 0.68

# Lightness component
color.hsl.l  # 0.803921568627451

# All HSL components as a tuple
color.hsl.vals  # (0.5833333333333334, 0.68, 0.803921568627451)

# New saturation component value
color.hsl.s = 0.87
color.hsl.vals  # (0.5833333333333334, 0.8700000000000002, 0.68)

# Change all HSL values
color.hsl.vals = (0.25, 0.50, 0.75)
color  # <Color(0xbfdf9f)>
```

### HSV color view
HSV color view has the following attributes which may be read or written:

 - `h`: hue component of HSV color value.
 - `s`: saturation component of HSV color value.
 - `v`: value component of HSV color value.
 - `vals`: hue, saturation and value components as a tuple.

```
from colorviews import Color
color = Color.from_int(0xabcdef)  # <Color(0xabcdef)>

# Hue component
color.hsv.h  # 0.5833333333333334

# Saturation component
color.hsv.s  # 0.2845188284518829

# Value component
color.hsv.v  # 0.9372549019607843

# All HSV components as a tuple
color.hsv.vals
# (0.5833333333333334, 0.2845188284518829, 0.9372549019607843)

# New hue component value
color.hsv.h = 0.82
color.hsv.vals  # (0.82, 0.6799999999999992, 0.803921568627451)

# Change all HSV values
color.hsv.vals = (0.25, 0.50, 0.75)
color  # <Color(0x8fbf60)>
```

## Creating AlphaColor objects

`AlphaColor` objects can also be created in more than one way.

###  From RGBA values
With the constructor or `AlphaColor.from_rgba(r: float, g: float, b: float, a: float)`.

```
from colorviews import AlphaColor
color = AlphaColor(0.2, 0.4, 0.8, 0.5)  # <AlphaColor(0x3366cc80)>
color = AlphaColor.from_rgba(0.2, 0.4, 0.8, 0.75)  # <AlphaColor(0x3366ccbf)>
```
    
### From color RGBA integer value
With `AlphaColor.from_int()`.

```
from colorviews import AlphaColor
color = AlphaColor.from_int(0xabcdef80)  # <AlphaColor(0xabcdef80)>
```

### From HSLA values
With `AlphaColor.from_hsla(h: float, s: float, l: float, a: float)`.

```
from colorviews import AlphaColor
color = AlphaColor.from_hsla(0.5, 1.0, 0.52, 0.8)  # <AlphaColor(0xaffffcc)>
```
    
### From HSVA values
With `Color.from_hsva(h: float, s: float, v: float, a: float)`.

```
from colorviews import AlphaColor
color = AlphaColor.from_hsva(0.5, 1.0, 0.52, 0.8)  # <AlphaColor(0x8585cc)>
```
    
### From color name
With `AlphaColor.from_name()`.

Just like `Color.from_name()` but with an alpha value which is set to zero.
    
```
from colorviews import AlphaColor
color = AlphaColor.from_name("darkgrey")  # <AlphaColor(0xa9a9a900)>
```


## Accessing color component values
### Hex value of color

```
from colorviews import AlphaColor
color = AlphaColor.from_int(0xabcdef80)  # <AlphaColor(0xabcdef80)>
hex(color)  # '0xabcdef80'
str(color)  # 'abcdef80'
```

### RGBA color view
RGBA color view has the following attributes which may be read or written:

 - `r`: red component of RGBA color value.
 - `g`: green component of RGBA color value.
 - `b`: blue component of RGBA color value.
 - `a`: alpha component of RGBA color value.
 - `vals`: red, green and blue components as a tuple.

```
from colorviews import AlphaColor
color = AlphaColor.from_int(0xabcdef80)  # <AlphaColor(0xabcdef80)>

# Red component
color.rgba.r  # 0.6705882352941176

# Green component
color.rgba.g  # 0.803921568627451

# Blue component
color.rgba.b  # 0.9372549019607843

# Alpha component
color.rgba.a  # 0.5019607843137255

# All RGBA components as a tuple
color.rgba.vals
# (0.6705882352941176, 0.803921568627451, 0.9372549019607843,
#  0.5019607843137255)

# New red component value
color.rgba.r = 0.52
color.rgba.vals  # (0.52, 0.803921568627451, 0.9372549019607843)

# Change all RGBA values
color.rgba.vals = (0.25, 0.50, 0.75, 0.2)
color  # <AlphaColor(0x4080bf33)>
```

### HSLA color view
HSLA color view has the following attributes which may be read or written:

 - `h`: hue component of HSLA color value.
 - `s`: saturation component of HSLA color value.
 - `l`: lightness component of HSLA color value.
 - `a`: alpha component of HSLA color value.
 - `vals`: hue, saturation and lightness components as a tuple.

```
from colorviews import AlphaColor
color = AlphaColor.from_int(0xabcdef80)  # <AlphaColor(0xabcdef80)>

# Hue component
color.hsla.h  # 0.5833333333333334

# Saturation component
color.hsla.s  # 0.68

# Lightness component
color.hsla.l  # 0.803921568627451

# Alpha component
color.hsla.a  # 0.5019607843137255

# All HSLA components as a tuple
color.hsla.vals
# (0.5833333333333334, 0.68, 0.803921568627451, 0.5019607843137255)

# New lightness component value
color.hsla.l = 0.24
color.hsla.vals
# (0.5833333333333334, 0.803921568627451, 0.24, 0.5019607843137255)

# Change all HSLA values
color.hsla.vals = (0.25, 0.50, 0.75, 0.2)
color  # <AlphaColor(0xbfdf9f33)>
```

### HSVA color view
HSVA color view has the following attributes which may be read or written:

 - `h`: hue component of HSVA color value.
 - `s`: saturation component of HSVA color value.
 - `v`: value component of HSVA color value.
 - `a`: alpha component of HSVA color value.
 - `vals`: hue, saturation and value components as a tuple.

```
from colorviews import AlphaColor
color = AlphaColor.from_int(0xabcdef80)  # <AlphaColor(0xabcdef80)>

# Hue component
color.hsva.h  # 0.5833333333333334

# Saturation component
color.hsva.s  # 0.2845188284518829

# Value component
color.hsva.v  # 0.9372549019607843

# Alpha component
color.hsva.a  # 0.5019607843137255

# All HSVA components as a tuple
color.hsva.vals
# (0.5833333333333334, 0.2845188284518829, 0.9372549019607843,
#  0.5019607843137255)

# New value (brightness) component value
color.hsva.v = 0.11
color.hsva.vals
# (0.5833333333333334, 0.28451882845188287, 0.11, 0.5019607843137255)

# Change all HSVA values
color.hsva.vals = (0.25, 0.50, 0.75, 0.2)
color  # <AlphaColor(0x8fbf6033)>
```


# Converting values to int equivalent
`scale()` function may be used to convert the color component values from float values to integer equivalent.

It multiplies a value with another scaling factor and returns this product value rounded off to the closest integer.

For example,

```
from colorviews import Color, AlphaColor, scale
color = Color.from_int(0xabcdef)
alphacolor = AlphaColor.from_int(0xabcdef80)

# Unsigned integer values: [0.0, 1.0] -> [0, 255]
red = [color.rgb.r, scale(color.rgb.r, 255)]
# [0.6705882352941176, 171]

# Percentage values: [0.0, 1.0] -> [0, 100]
alpha = [alphacolor.hsla.a, scale(alphacolor.hsla.a, 100)]
# [0.5019607843137255, 50]

# Angle value in degrees: [0.0, 1.0] -> [0, 360)
hue = [color.hsv.h, scale(color.hsv.h, 360)]
# [0.5833333333333334, 210]
```

# Comparing colors
Colors can be compared using the usual comparison operators.

Comparions will done based on the integer RGB(A) values.

```
darkred = Color.from_name("darkred")  # <Color(0x8b0000)>
crimson = Color.from_name("crimson")  # <Color(0xdc143c)>
crimson < darkred  # False
crimson > darkred  # True
crimson <= darkred  # False
crimson >= darkred  # True
crimson == darkred  # False
crimson != darkred  # True
```

Likewise with `AlphaColor`:

```
faint_red = AlphaColor.from_name("red", 0.5)  # <AlphaColor(0xff000080)>
fainter_red = AlphaColor.from_name("red", 0.2)  # <AlphaColor(0xff000033)>
faint_red < fainter_red  # False
faint_red > fainter_red  # True
```
    
But comparison between a `Color` object and a `AlphaColor` object is not supported. Even when their RGB values match.

```
red_noalpha = Color.from_name("red")  # <Color(0xff0000)>
red_alpha = AlphaColor.from_name("red")  # <AlphaColor(0xff0000)>
red_noalpha < red_alpha  # Exception!
```

# Duplicating or copying color objects
`copy()` method of the color classes can be used to duplicate a color object.

```
# Duplicating Color objects
color = Color.from_int(0xabcdef)  # <Color(0xabcdef)>
color_copy = color.copy()
id(color_copy) != id(color)  # True

# Duplicating AlphaColor objects
alphacolor = AlphaColor.from_name("red")  # <AlphaColor(0xff0000)>
alphacolor_copy = alphacolor.copy()
id(alphacolor_copy) != id(alphacolor)  # True
```

# Caveats
The color component values are stored internally as RGB(A) float values in the [0.0, 1.0] range.

Depending on the way in which the color objects are created, there may be a slight difference in this RGB(A) values.

For example, consider two AlphaColor objects where one as is made using an integer value and the other is made using RGBA values as in

```
t1=cvs.AlphaColor.from_int(0xffffff80)  # <AlphaColor(0xffffff80)>
t2=cvs.AlphaColor.from_rgba(1,1,1,0.5)  # <AlphaColor(0xffffff80)>
```

Both `t1` and `t2` would have the same integer value.

```
t1 == t2  # True
```

But their alpha values would be slighlty different.

```
t1.rgba.a  # 0.5019607843137255
t2.rgba.a  # 0.5
```

This is because the alpha value 0x80 being converted to its float equivalent like

```
0x80 / 0xff  # 0.5019607843137255
```











# Long version

## Color objects
Represents colors without alpha value.

Color value is stored internally using RGB color scheme.

```
class Color(red: float, green: float, blue: float)
```

Arguments:

 - `r`: Value of red component.
 - `g`: Value of green component.
 - `b`: Value of blue component.

All arguments must have value between 0.0 and 1.0, inclusive of the limits.

### Attributes

 - `rgb`: RGB color view. A `ColorViewRGB` object.
 - `hsl`: HSL color view. A `ColorViewHSL` object.
 - `hsv`: HSV color view. A `ColorViewHSV` object.

### Methods

#### `Color.from_int(value: int)`

Create a `Color` object using the RGB integer value of the color.

Arguments:

 - value: RGB integer value of color

Returns: `Color` object whose RGB value is the given integer.

#### `Color.from_name(name: str)`

Create a `Color` object using the color's name.

[CSS3 extended color keywords](https://www.w3.org/wiki/CSS3/Color/Extended_color_keywords) are recognized.

Case of the color name doesn't matter.

Arguments:

 - `name`: Name of the color

Returns: `Color` object for color corresponding to given color name.

#### `Color.from_rgb(r: float, g: float, b: float)`

Create a `Color` object from RGB values.

Same as using the constructor of `Color`.

Arguments:

 - `r`: Value of red component.
 - `g`: Value of green component.
 - `b`: Value of blue component.

Returns: `Color` object of given RGB value.


#### `Color.from_hsl(h: float, s: float, l: float)`

Create a `Color` object from HSL values.

Arguments:

 - `h`: Value of hue component.
 - `s`: Value of saturation component.
 - `l`: Value of lightness component.

Returns: `Color` object of given HSL value.


#### `Color.from_hsv(h: float, s: float, v: float)`

Create a `Color` object from HSV values.

Arguments:

 - `h`: Value of hue component.
 - `s`: Value of saturation component.
 - `v`: Value of the value component.

Returns: `Color` object of given HSV value.


#### `Color.copy()`

Duplicate the `Color` object.

Returns: A separate copy of the `Color` object.


## AlphaColor objects
Represents colors with alpha value.

Color value is stored internally using RGBA color scheme.

```
class AlphaColor(red: float, green: float, blue: float, alpha: float)
```

Arguments:

 - `r`: Value of red component
 - `g`: Value of green component
 - `b`: Value of blue component
 - `a`: Value of alpha component

All arguments must have value between 0.0 and 1.0, inclusive of the limits.

### Attributes

 - `rgba`: RGBA color view. A `ColorViewRGBA` object.
 - `hsla`: HSLA color view. A `ColorViewHSLA` object.
 - `hsva`: HSVA color view. A `ColorViewHSVA` object.

### Methods

#### `AlphaColor.from_int(value: int)`

Create an `AlphaColor` object using the RGBA integer value of the color.

Arguments:

 - `value`: RGBA integer value of color

Returns: `AlphaColor` object whose RGBA value is the given integer.

#### `AlphaColor.from_name(name: str)`

Create an `AlphaColor` object using the color's name.

Alpha value of returned `AlphaColor` object will be 0 (ie, fully transparent color).

[CSS3 extended color keywords](https://www.w3.org/wiki/CSS3/Color/Extended_color_keywords) are recognized.

Case of the color name doesn't matter.

Arguments:

 - `name`: Name of the color

Returns: `AlphaColor` object for color corresponding to given color name with its alpha value set to zero.

#### `AlphaColor.from_rgba(r: float, g: float, b: float, a: float)`

Create an `AlphaColor` object from RGBA values.

Same as using the constructor of `AlphaColor`.

Arguments:

 - `r`: Value of red component.
 - `g`: Value of green component.
 - `b`: Value of blue component.
 - `a`: Value of alpha component.

Returns: `AlphaColor` object of given RGBA value.


#### `AlphaColor.from_hsla(h: float, s: float, l: float, a: float)`

Create an `AlphaColor` object from HSLA values.

Arguments:

 - `h`: Value of hue component.
 - `s`: Value of saturation component.
 - `l`: Value of lightness component.
 - `a`: Value of alpha component.

Returns: `AlphaColor` object of given HSLA value.


#### `AlphaColor.from_hsva(h: float, s: float, v: float, a: float)`

Create an `AlphaColor` object from HSVA values.

Arguments:

 - `h`: Value of hue component.
 - `s`: Value of saturation component.
 - `v`: Value of the value component.
 - `a`: Value of alpha component.

Returns: `AlphaColor` object of given HSVA value.


#### `AlphaColor.copy()`

Duplicate the `AlphaColor` object.

Returns: A separate copy of the `AlphaColor` object.


## ColorViewRGB objects
RGB color view for `Color` objects.

```
class ColorViewRGB(color: Color)
```

Arguments:

 - `color`: `Color` object to be associated with the RGB view

### Attributes

 - `r`: Red component of RGB value.
 - `g`: Green component of RGB value.
 - `b`: Blue component of RGB value.
 - `vals`: Red, green and blue component values as a tuple.
 - `color`: `Color` object associated with the RGB view.

### Methods

#### `ColorViewRGB.replace(r: float = None, g: float = None, b: float = None) -> Color`

Creates a new `Color` object by replacing RGB components of the `Color` object associated with the RGB color view.

Arguments:

 - `r`: New value for red component.
 - `g`: New value for green component.
 - `b`: New value for blue component.

Returns: A new `Color` object made by replacing RGB components of the `Color` object with given values.

## ColorViewHSL objects
HSL color view for `Color` objects.

```
class ColorViewHSL(color: Color)
```

Arguments:

 - `color`: `Color` object to be associated with the HSL view.

### Attributes

 - `h`: Hue component of HSL value.
 - `s`: Saturation component of HSL value.
 - `l`: Lightness component of HSL value.
 - `vals`: Hue, saturation and lightness component values as a tuple.
 - `color`: `Color` object associated with the HSL view.

### Methods

#### `ColorViewHSL.replace(h: float = None, s: float = None, l: float = None) -> Color`

Creates a new `Color` object by replacing HSL components of the `Color` object associated with the HSL color view.

Arguments:

 - `h`: New value for hue component.
 - `s`: New value for saturation component.
 - `l`: New value for lightness component.

Returns: A new `Color` object made by replacing HSL components of the `Color` object with given values.

## ColorViewHSV objects
HSV color view for `Color` objects.

```
class ColorViewHSV(color: Color)
```

Arguments:

 - `color`: `Color` object to be associated with the HSV view.

### Attributes

 - `h`: Hue component of HSV value.
 - `s`: Saturation component of HSV value.
 - `v`: Value component of HSV value.
 - `vals`: Hue, saturation and value component values as a tuple.
 - `color`: `Color` object associated with the HSV view.

### Methods

#### `ColorViewHSV.replace(h: float = None, s: float = None, v: float = None) -> Color`

Creates a new `Color` object by replacing HSV components of the `Color` object associated with the HSV color view.

Arguments:

 - `h`: New value for hue component.
 - `s`: New value for saturation component.
 - `v`: New value for value component.

Returns: A new `Color` object made by replacing HSV components of the `Color` object with given values.

## ColorViewRGBA objects
RGBA color view for `AlphaColor` objects.

```
class ColorViewRGBA(color: AlphaColor)
```

Arguments:

 - `color`: `AlphaColor` object to be associated with the RGBA view

### Attributes

 - `r`: Red component of RGBA value.
 - `g`: Green component of RGBA value.
 - `b`: Blue component of RGBA value.
 - `a`: Alpha component of RGBA value.
 - `vals`: Red, green and blue component values as a tuple.
 - `color`: `AlphaColor` object associated with the RGBA view.

### Methods

#### `ColorViewRGBA.replace(r: float = None, g: float = None, b: float = None, a: float = None) -> AlphaColor`

Creates a new `AlphaColor` object by replacing RGBA components of the `AlphaColor` object associated with the RGBA color view.

Arguments:

 - `r`: New value for red component.
 - `g`: New value for green component.
 - `b`: New value for blue component.
 - `a`: New value for alpha component.

Returns: A new `AlphaColor` object made by replacing RGBA components of the `AlphaColor` object with given values.

## ColorViewHSLA objects
HSLA color view for `AlphaColor` objects.

```
class ColorViewHSLA(color: AlphaColor)
```

Arguments:

 - `color`: `AlphaColor` object to be associated with the HSLA view.

### Attributes

 - `h`: Hue component of HSLA value.
 - `s`: Saturation component of HSLA value.
 - `l`: Lightness component of HSLA value.
 - `a`: Alpha component of HSLA value.
 - `vals`: Hue, saturation and lightness component values as a tuple.
 - `color`: `AlphaColor` object associated with the HSLA view.

### Methods

#### `ColorViewHSLA.replace(h: float = None, s: float = None, l: float = None, a: float = None) -> AlphaColor`

Creates a new `AlphaColor` object by replacing HSLA components of the `AlphaColor` object associated with the HSLA color view.

Arguments:

 - `h`: New value for hue component.
 - `s`: New value for saturation component.
 - `l`: New value for lightness component.
 - `a`: New value for alpha component.

Returns: A new `AlphaColor` object made by replacing HSLA components of the `AlphaColor` object with given values.

## ColorViewHSVA objects
HSVA color view for `AlphaColor` objects.

```
class ColorViewHSVA(color: AlphaColor)
```

Arguments:

 - `color`: `AlphaColor` object to be associated with the HSVA view.

### Attributes

 - `h`: Hue component of HSVA value.
 - `s`: Saturation component of HSVA value.
 - `v`: Lightness component of HSVA value.
 - `a`: Alpha component of HSVA value.
 - `vals`: Hue, saturation and lightness component values as a tuple.
 - `color`: `AlphaColor` object associated with the HSVA view.

### Methods

#### `ColorViewHSVA.replace(h: float = None, s: float = None, v: float = None, a: float = None) -> AlphaColor`

Creates a new `AlphaColor` object by replacing HSVA components of the `AlphaColor` object associated with the HSVA color view.

Arguments:

 - `h`: New value for hue component.
 - `s`: New value for saturation component.
 - `v`: New value for value component.
 - `a`: New value for alpha component.

Returns: A new `AlphaColor` object made by replacing HSVA components of the `AlphaColor` object with given values.


# Scaling float values to integers

## `scale(val: float, multiplier: int) -> int`

Scales a value by a factor.

Multiplies a value with a scaling factor and returns the product value rounded off to the closest integer.

Arguments:

 - `val`: Value to be scaled.
 - `factor`: Scaling factor.

Returns: Integer closest to the product of `val` and `factor`.
