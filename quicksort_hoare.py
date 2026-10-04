# Лабораторна робота №2. Варіант 12
# Швидке сортування за схемою Хоара з підрахунком операцій і трасуванням.

DATA = [53, 100, 44, 74, 53, 38, 82, 65, 28]


def partition(a, l, r, trace=False, depth=0):
    comparisons = 0
    assignments = 0
    indent = "  " * depth

    pivot = a[l]
    assignments += 1
    if trace:
        print(f"{indent}Вибираємо опорний елемент (pivot): {pivot}")

    i = l - 1
    j = r + 1
    assignments += 2

    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1

        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1

        comparisons += 1
        if i >= j:
            if trace:
                print(f"{indent}Поточні індекси: i={i}, j={j}. Індекси перетнулися; повертаємо j={j}.")
            return j, comparisons, assignments

        if trace:
            before_i, before_j = a[i], a[j]
        a[i], a[j] = a[j], a[i]
        assignments += 3
        if trace:
            print(
                f"{indent}Поточні індекси: i={i}, j={j}. "
                f"Обмінюємо {before_i} і {before_j}. Масив: {a}"
            )


def quicksort(a, l, r, trace=False, depth=0):
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    indent = "  " * depth

    if trace:
        print(f"{indent}Quicksort виклик: масив={a}, l={l}, r={r}")

    if l < r:
        q, c1, a1 = partition(a, l, r, trace, depth)
        comparisons += c1
        assignments += a1

        c2, a2, r2 = quicksort(a, l, q, trace, depth + 1)
        c3, a3, r3 = quicksort(a, q + 1, r, trace, depth + 1)
        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3

        if trace:
            print(f"{indent}Після Quicksort для l={l}, r={r}: масив={a}")
    else:
        # Як у методичних вказівках, базові виклики не додаються до лічильника.
        return 0, 0, 0

    return comparisons, assignments, recursive_calls


if __name__ == "__main__":
    my_list = DATA.copy()
    original_list = my_list.copy()
    total_comparisons, total_assignments, total_recursive_calls = quicksort(
        my_list, 0, len(my_list) - 1
    )
    print("Оригінальний список:", original_list)
    print("Відсортований список:", my_list)
    print("Загальна кількість порівнянь:", total_comparisons)
    print("Загальна кількість присвоювань:", total_assignments)
    print("Загальна кількість рекурсивних викликів:", total_recursive_calls)

    print("\n--- Quicksort за схемою Хоара з трасуванням ---")
    traced = DATA.copy()
    c, a, r = quicksort(traced, 0, len(traced) - 1, trace=True)
    print("Фінальний відсортований список:", traced)
    print("Загальна кількість порівнянь:", c)
    print("Загальна кількість присвоювань:", a)
    print("Загальна кількість рекурсивних викликів:", r)
