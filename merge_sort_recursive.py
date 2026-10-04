# Лабораторна робота №2. Варіант 12
# Рекурсивне сортування злиттям з підрахунком операцій і трасуванням.

DATA = [53, 100, 44, 74, 53, 38, 82, 65, 28]


def merge(left, right, trace=False, depth=0, detailed_assignments=False):
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0
    indent = "  " * depth

    if trace:
        print(f"{indent}Зливаємо {left} та {right}")

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            if trace:
                print(f"{indent}  Порівняння: {left[i]} <= {right[j]} -> True. Додаємо {left[i]}")
            merged_arr.append(left[i])
            i += 1
        else:
            if trace:
                print(f"{indent}  Порівняння: {left[i]} <= {right[j]} -> False. Додаємо {right[j]}")
            merged_arr.append(right[j])
            j += 1
        # Базовий лічильник рахує розміщення елемента;
        # детальний — також зміну індексу.
        assignments += 2 if detailed_assignments else 1

    while i < len(left):
        if trace:
            print(f"{indent}  Додаємо залишок з лівого масиву: {left[i]}")
        merged_arr.append(left[i])
        i += 1
        assignments += 1

    while j < len(right):
        if trace:
            print(f"{indent}  Додаємо залишок з правого масиву: {right[j]}")
        merged_arr.append(right[j])
        j += 1
        assignments += 1

    if trace:
        print(f"{indent}Злиття завершено. Результат: {merged_arr}")

    return merged_arr, comparisons, assignments


def merge_sort_recursive(arr, trace=False, depth=0, detailed_assignments=False):
    comparisons = 0
    assignments = 0
    recursive_calls = 0
    indent = "  " * depth

    if trace:
        print(f"{indent}Розділяємо масив: {arr}")

    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls

    mid = len(arr) // 2
    assignments += 1

    # Два дочірні рекурсивні виклики; початковий виклик не враховуємо.
    recursive_calls += 2
    left_half, c1, a1, r1 = merge_sort_recursive(
        arr[:mid], trace, depth + 1, detailed_assignments
    )
    right_half, c2, a2, r2 = merge_sort_recursive(
        arr[mid:], trace, depth + 1, detailed_assignments
    )

    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2

    merged_arr, c_merge, a_merge = merge(
        left_half, right_half, trace, depth, detailed_assignments
    )
    comparisons += c_merge
    assignments += a_merge

    return merged_arr, comparisons, assignments, recursive_calls


if __name__ == "__main__":
    original = DATA.copy()
    sorted_list, comps, assigs, calls = merge_sort_recursive(original.copy())
    print("Оригінальний список:", original)
    print("Відсортований список:", sorted_list)
    print("Загальна кількість порівнянь:", comps)
    print("Загальна кількість присвоювань:", assigs)
    print("Загальна кількість рекурсивних викликів:", calls)

    print()
    traced, trace_comps, trace_assigs, trace_calls = merge_sort_recursive(
        original.copy(), trace=True, detailed_assignments=True
    )
    print("Фінальний відсортований список:", traced)
    print("Загальна кількість порівнянь:", trace_comps)
    print("Загальна кількість присвоювань:", trace_assigs)
    print("Загальна кількість рекурсивних викликів:", trace_calls)
