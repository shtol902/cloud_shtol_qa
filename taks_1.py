def main():
    # Чтение списка чисел
    input_numbers = input("Введите список чисел через запятую: ")
    numbers = [int(num.strip()) for num in input_numbers.split(",")]

    # Вывод четных чисел
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Четные числа: {even_numbers}")

    # Нахождение максимального и минимального числа
    max_number = max(numbers)
    min_number = min(numbers)
    print(f"Максимальное число: {max_number}")
    print(f"Минимальное число: {min_number}")

    # Сортировка списка в порядке возрастания без использования sorted()
    list_sorted_numbers = sort(numbers.copy())
    print(f"Отсортированный список: {list_sorted_numbers}")

def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Обмен значениями
    return arr

if __name__ == "__main__":
    main()
