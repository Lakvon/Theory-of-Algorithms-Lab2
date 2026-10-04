# Лабораторна робота №2. Варіант 12
# Ітеративне сортування злиттям з підрахунком операцій і трасуванням.

DATA = [53, 100, 44, 74, 53, 38, 82, 65, 28]


def merge(a, left, mid, right, trace=False, detailed_assignments=False):
    comparisons = 0
    assignments = 0

    n1 = mid - left
    n2 = right - mid
    L = a[left:mid]
    R = a[mid:right]
    assignments += n1 + n2

    if trace:
        print(f"Об'єднуємо підмасиви: a[{left}:{mid}] ({L}) і a[{mid}:{right}] ({R})")

    it1 = 0
    it2 = 0
    k = left
    assignments += 3

    while it1 < n1 and it2 < n2:
        comparisons += 1
        if trace:
            print(f"  Порівняння: {L[it1]} < {R[it2]}")
        if L[it1] < R[it2]:
            a[k] = L[it1]
            it1 += 1
        else:
            a[k] = R[it2]
            it2 += 1
        k += 1
        # У Лістингу 2.1 враховано дві базові операції,
        # у детальному трасуванні — усі три присвоювання.
        assignments += 3 if detailed_assignments else 2

    while it1 < n1:
        a[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 3 if detailed_assignments else 1

    while it2 < n2:
        a[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 3 if detailed_assignments else 1

    if trace:
        print(f"Масив після об'єднання: {a}")
        print("-" * 54)

    return comparisons, assignments


def merge_sort_iterative(a, trace=False, detailed_assignments=False):
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1

    if trace:
        print("--- ІТЕРАТИВНА ВЕРСІЯ ---")
        print("Початковий масив:", a)
        print("-" * 54)

    while i < n:
        j = 0
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)
            c, a_count = merge(
                a, left, mid, right,
                trace=trace,
                detailed_assignments=detailed_assignments,
            )
            comparisons += c
            assignments += a_count
            j += 2 * i
        i *= 2

    return a, comparisons, assignments


if __name__ == "__main__":
    original = DATA.copy()
    sorted_list, comps, assigs = merge_sort_iterative(original.copy())
    print("Оригінальний список:", original)
    print("Відсортований список:", sorted_list)
    print("Кількість порівнянь:", comps)
    print("Кількість присвоювань:", assigs)

    print()
    traced, trace_comps, trace_assigs = merge_sort_iterative(
        original.copy(), trace=True, detailed_assignments=True
    )
    print("Фінальний відсортований список:", traced)
    print("Загальна кількість порівнянь:", trace_comps)
    print("Загальна кількість присвоювань:", trace_assigs)
