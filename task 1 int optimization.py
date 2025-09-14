import time

# Простой перебор.
def find_range_simple() -> list[int]:

    # Нижняя граница
    n1 = 0
    n2 = 0
    while True:
        if n1 is not n2:
            break
        n1 -= 1
        n2 -= 1

    N = n1 + 1

    # Верхняя граница
    m1 = 0
    m2 = 0
    while True:
        if m1 is not m2:
            break
        m1 += 1
        m2 += 1
    M = m1 - 1

    return -N, M

if __name__ == "__main__":

    print("Поиск границ.")
    start = time.time()
    N, M = find_range_simple()
    end = time.time()
    print(f"Границы найдены! [{N}, {M}]")
    print(f"На это потребовалось {end - start} секунд.")
    
