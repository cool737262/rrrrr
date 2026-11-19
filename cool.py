import numpy as np
 
numbers = [3, 7, 1, 9, 4]
arr = np.array(numbers)
 
print(type(arr))     # класс массива
print(arr.shape)     # форма
print(arr.size)      # размер
print(arr)           # сам массив
celsius = np.array([0, 10, 20, 30, 40])
fahrenheit = celsius * 9 / 5 + 32
 
print("Цельсии:   ", celsius)
print("Фаренгейты:", fahrenheit)
times = np.array([120, 95, 88, 102, 77, 110, 85])
 
print("Среднее время:     ", np.mean(times))
print("Максимум:          ", np.max(times))
print("Минимум:           ", np.min(times))
print("Станд. отклонение: ", np.std(times))
print("Сумма:             ", np.sum(times))
weights = np.array([[0.1, 0.2, 0.3],
                    [0.4, 0.5, 0.6],
                    [0.7, 0.8, 0.9]])
 
print("Матрица:\n", weights)
print("Первая строка:     ", weights[0, :])
print("Последний столбец: ", weights[:, -1])
print("Элемент [1][2]:    ", weights[1, 2])
randoms = np.random.randint(1, 101, size=100)
 
mask = randoms > 50        # булев массив: True/False
big = randoms[mask]        # фильтруем через маску
 
print("Всего чисел:      ", randoms.size)
print("Чисел больше 50:  ", big.size)
print("Отобранные числа: ", big)
grades = np.array([[5, 4, 3],
                   [4, 4, 5],
                   [3, 5, 5],
                   [4, 3, 4],
                   [5, 5, 4]])
 
by_student = grades.mean(axis=1)   # средний балл каждого студента
by_subject = grades.mean(axis=0)   # средний балл по каждому предмету
 
print("Средний балл каждого студента:", by_student)
print("Средний балл по предметам:    ", by_subject)
