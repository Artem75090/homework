from time import sleep, time
import threading


def wite_words(word_count, file_name):
    for i in range(word_count):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write('Какое-то слово № ' + str(i + 1) + '\n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
print(f'Работа потоков: {round(time() - start_time, 2)}')

start_time2 = time()
thread_1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread_1.start()
thread_2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread_2.start()
thread_3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread_3.start()
thread_4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
print(f'Работа потоков: {round(time() - start_time2, 2)}')
