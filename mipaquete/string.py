"""
This module converts strings into lower and uppercase
"""


def lowercase(text: str) -> str:
    """Converts all uppercase characters in a string into lowercase
    characters and returns it. Symbols and Numbers are ignored.

    Args:
        text (str): Input string

    Returns:
        str: String where all characters are lower case

    Examples:
        >>> from mipaquete.string import lowercase
        >>> text = "TexT with 2 numb3rs and 5 SymbOls !*¨´-"
        >>> lowercase(text)
        'text with 2 numb3rs and 5 symbols !*¨´-'
    """
    return text.lower()


def uppercase(text: str) -> str:
    """Converts all uppercase characters in a string into uppercase
    characters and returns it.Symbols and Numbers are ignored.

    Args:
        text (str): Input string

    Returns:
        str: String where all characters are upper case

    Examples:
        >>> from mipaquete.string import uppercase
        >>> text = "TexT with 2 numb3rs and 5 SymbOls !*¨´-"
        >>> uppercase(text)
        'TEXT WITH 2 NUMB3RS AND 5 SYMBOLS !*¨´-'
    """
    return text.upper()
