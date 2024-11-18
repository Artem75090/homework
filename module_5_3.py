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
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors == other
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors < other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors > other
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors <= other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors >= other
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors != other
    def __add__(self, value):
        if isinstance(value, (int, float)):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return self.number_of_floors + value.number_of_floors
    def __radd__(self, value):
        return self + value
    def __iadd__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, (int, float)):
            self.number_of_floors +=value
        return self

h1 = House('ЖК Эльбрус', 125)
h2 = House('ЖК Акация', 125)
h1 += 5
print(h1)














