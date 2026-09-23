class utils:
    @staticmethod
    def reversed(value: int) -> int:
        """Return an integer with its digits reversed."""
        if type(value) is not int:
            raise TypeError("value must be an integer")

        sign = -1 if value < 0 else 1
        return sign * int(str(abs(value))[::-1])

    @staticmethod
    def formatter(value: int) -> tuple[str, str]:
        """Return the binary and octal representations of an integer."""
        if type(value) is not int:
            raise TypeError("value must be an integer")

        return bin(value), oct(value)
