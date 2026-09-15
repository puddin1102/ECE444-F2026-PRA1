from utils import utils

try:
    print("Reverse Integer:", utils.reversed(123))
except Exception as e:
    print("Integer error:", e)

try:
    print("Reverse String:", utils.reversed("123"))
except Exception as e:
    print("String error:", e)

try:
    print("Reverse Float:", utils.reversed(123.0))
except Exception as e:
    print("Float error:", e)

try:
    print("Formatter Integer:", utils.formatter(16))
except Exception as e:
    print("Formatter error:", e)

try:
    print("Formatter String:", utils.formatter("16"))
except Exception as e:
    print("Formatter error:", e)

try:
    print("Formatter Float:", utils.formatter(16.0))
except Exception as e:
    print("Formatter error:", e)

    