import heapq

def merge_k_lists(lists):
    min_heap = []

    # Додаємо перші елементи з кожного списку в купу
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, що список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, позиція в списку)

    result = []

    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        # Якщо в цьому списку є ще елементи, додаємо наступний
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))

    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
