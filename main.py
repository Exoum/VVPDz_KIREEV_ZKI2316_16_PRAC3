from typing import List

def syracuse_sequence(n: int) -> List[int]:
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    while True:
        print("\nСиракузская последовательность")
        print("1. Получить Сиракузскую последовательность")
        print("2. Найти максимальное значение в Сиракузской последовательности")
        print("3. Выход")
        
        choice = input("Выберите опцию (1/2/3): ")

        if choice == '3':
            print("Выход из программы.")
            break

        try:
            n = int(input("Введите целое положительное число N: "))
            if n <= 0:
                print("Пожалуйста, введите положительное число.")
                continue
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
            continue
        
        if choice == '1':
            sequence = syracuse_sequence(n)
            print(f"Сиракузская последовательность для {n}: {sequence}")
        elif choice == '2':
            max_value = syracuse_max(n)
            print(f"Максимальное значение в Сиракузской последовательности для {n}: {max_value}")
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()