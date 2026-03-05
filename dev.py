def total_price(position_1: int, position_2: int, position_3: bool = True):
    if position_3 is not False:
        total = int((position_1 * position_2) / 2)
        return total


result = total_price(150, 210)
print(result)
