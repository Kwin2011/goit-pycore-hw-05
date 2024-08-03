def caching_fibonacci():
    # Створюємо порожній словник для кешування обчислених значень
    cache = {}
    
    def fibonacci(n):
        # Обробляємо базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Якщо значення вже є у кеші, повертаємо його
        if n in cache:
            return cache[n]
        
        # Обчислюємо значення та зберігаємо у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    
    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10))
print(fib(15))

# Terminal
# 55
# 610