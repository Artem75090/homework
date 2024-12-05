name1 = 'Мастера кода'
name2 = 'Волшебники данных'
team1_num = 6
team2_num = 5
score_1 = 23
score_2 = 19
team1_time = 18015.2
team2_time = 19125.5
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time)/(score_1 + score_2), 2)
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды {name1}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды {name2}!'
else:
    result = 'Ничья!'
print("В команде %s участников: %s ! " %(name1, team1_num))
print('В команде %s участников: %s !' %(name2, team2_num))
print("Итого сегодня в командах участников: %s и %s !" %(team1_num, team2_num))
print("Команда {} решила задач: {} !".format(name1, score_1))
print("Команда {} решила задач: {} !".format(name2, score_2))
print("{} решили задачи за {} с !".format(name1, team1_time))
print("{} решили задачи за {} с !".format(name2, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')