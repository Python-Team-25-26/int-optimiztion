def find_range() -> tuple[int, int]:

    def check(num: int) -> bool:
        a = num
        b = num + 1 - 1
        return a is b

    # нижняя граница
    low = 0
    step = 1
    while check(low - step):
        step *= 2
    left = low - step * 2
    right = low - step // 2
    while left < right - 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    lower_bound = right

    #верхняя граница
    high = 0
    step = 1
    while check(high + step):
        step *= 2
    left = high + step // 2
    right = high + step * 2

    while left < right - 1:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    upper_bound = left

    return lower_bound, upper_bound


if __name__ == "__main__":
    lower, upper = find_range()
    print(f"Границы: [{lower}, {upper}]")