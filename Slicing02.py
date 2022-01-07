def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a=str(s)
    answer=a[-4:]
    return answer
print(main('abcdefghijk'))