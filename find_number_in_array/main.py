def find_number_in_array(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i  # возвращает индекс найденного элемента
    return -1  # если число не найдено

# Пример использования
numbers = [3, 7, 1, 9, 5]
target_number = 9

index = find_number_in_array(numbers, target_number)

if index != -1:
    print(f"Число {target_number} найдено на позиции {index}.")
else:
    print(f"Число {target_number} не найдено в массиве.")
