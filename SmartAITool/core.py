def cprint(text, color="red"):
    """
    Print text with color formatting in terminal using ANSI color codes.

    This function allows printing text with color formatting in a terminal
    that supports ANSI color codes.

    Args:
        text (str): The text to print.
        color (str, optional): The color to use. Defaults to "red".
            Supported colors: "black", "red", "green", "yellow", 
            "blue", "magenta", "cyan", "white".

    Returns:
        None

    Example:
        >>> cprint("Hello World", "green")
        # Prints "Hello World" in green color
    """
    colors = {
        "black": "\033[30m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m",
    }

    color_code = colors.get(color.lower(), colors["white"])
    print(f"{color_code}{text}{colors['reset']}")
