"""
Utility functions to help other modules.
"""


def validate(val: float) -> None:
    """
    Check if val is between 0.0 and 1.0, including the limits.

    Arguments:
      val: Value to be validated.

    Raises:
      ValueError: If val is not in the range [0.0, 1.0].
    """
    if val < 0 or val > 1:
        raise ValueError(f"{val}: Expected value in [0.0, 1.0]")


def scale(val: float, factor: int) -> int:
    """
    Multiply val with factor and convert result to an integer with proper
    rounding.

    Arguments:
      val: Float value to rounded
      factor: Value with which val is multiplied.

    Returns:
      Rounded integer value of the product of val and factor.
    """
    num = val * factor
    floor_int = int(num)
    if num - floor_int < 0.5:
        return floor_int
    return floor_int + 1
