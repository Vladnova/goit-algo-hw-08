import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # Перетворюємо список у мінімальну купу
    total_cost = 0

    while len(cables) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(min_cost_to_connect_cables(cables))  # Виведе 29
