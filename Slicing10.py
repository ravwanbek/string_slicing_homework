def main(s,n,k):
    """
    The s string variable is given. return from index n to index k.
    Args:
        s(str): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        str: answer
    """
    s=str(s)
    n=int(n)
    k=int(k)
    answer=s[n:k]
    return answer
print(main('salomat',2,4))



    