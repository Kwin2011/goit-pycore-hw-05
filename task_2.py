import re
from typing import Generator, Callable

# Функція generator_numbers, яка приймає рядок та повертає генератор дійсних чисел
def generator_numbers(text: str) -> Generator[float, None, None]:
    # Використовуємо регулярний вираз для знаходження всіх дійсних чисел, відокремлених пробілами
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

# Функція sum_profit, яка підсумовує всі дійсні числа, знайдені у тексті, використовуючи generator_numbers
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")