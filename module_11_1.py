import numpy as np
import matplotlib.pyplot as plt

test_list = [1, 2, 3, 7, 9]

print(np.array(test_list))
print(np.mean(test_list))
print(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(10 * np.random.rand(2, 3))
print(np.linspace(10, 30, num=9))


x = [1, 2.9, 3.5, 4.8]
y = [8, 21, 25, 39]

plt.plot(x, y, label='Линейный график', color='blue', marker='o')
plt.title("Пример линейного графика")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.legend()
plt.grid()
plt.show()
