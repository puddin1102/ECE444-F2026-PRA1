class utils:
    def reversed(n):
        if type(n) != int:
            raise ValueError("Input must be an integer.")
        
        return int(str(abs(n))[::-1])

    def formatter(n):
        if type(n) != int:
            raise ValueError("Input must be an integer.")
        
        binary = bin(n)[2:]
        hexadecimal = hex(n)[2:]

        return f"Binary: {binary}, Hexadecimal: {hexadecimal}"