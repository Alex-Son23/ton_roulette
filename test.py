from ton.utils import Address


s = "EQAKbVR4hAH208GY2VZmJ0sIF7cXAUIbIjPmmz2Hqc1dJofx"

a = Address(s)
print(a.to_string(is_user_friendly=True, is_bounceable=False))
