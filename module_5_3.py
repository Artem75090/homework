class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print("Такого этажа не существует")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
    def __eq__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        return self.number_of_floors == other
    def __lt__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        return self.number_of_floors < other
    def __gt__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        return self.number_of_floors > other
    def __le__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        return self.number_of_floors <= other
    def __ge__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        return self.number_of_floors >= other
    def __ne__(self, other):
        if isinstance(other, House):
            other = other.number_of_floors
        return self.number_of_floors != other
    def __add__(self, value):
        if isinstance(value, (int, float)):
            return House(self.name, self.number_of_floors + value)
        if isinstance(value, House):
            return self.number_of_floors + value
    def __radd__(self, value):
        return self + value
    def __iadd__(self, value):
        if isinstance(value, House):
            value = value.number_of_floors
        self.number_of_floors += value
        return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)










