from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __str__(self):
        return self.nickname
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now
class UrTube:
    def __init__(self):
        self.users = []
        self.current_user = None
        self.videos = []
    def register(self, nickname, password, age):
        user_verification = True
        for i in range(len(self.users)):
            if nickname == self.users[i].nickname:
                user_verification =False
        if user_verification:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')
    def log_in (self, nickname, password):
        for i in range(len(self.users)):
            if nickname == self.users[i].nickname and hash(password) == hash(self.users[i].password):
                self.current_user = self.users[i]
    def log_out(self):
        print(f'Пока {self.current_user.nickname}')
        self.current_user = None
    def add(self, *args):
        counter = 0
        while counter < len(args):
            counter_2 = 0
            for i in range(len(self.videos)):
                if args[counter].title == self.videos[i].title:
                    continue
                else:
                    counter_2 += 1
            if counter_2 == len(self.videos):
                self.videos.append(args[counter])
            counter += 1
    def get_videos(self, search):
        search_list = []
        for i in self.videos:
            segment = len(search)
            for j in range(len(i.title) - len(search)):
                if search.lower() == i.title[j:segment].lower():
                    search_list.append(i.title)
                    break
                segment += 1
        return search_list
    def watch_video (self, video_title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for i in range(len(self.videos)):
                if self.videos[i].title == video_title and self.current_user.age < 18 and self.videos[i].adult_mode == True:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    break
                elif self.videos[i].title == video_title:
                    for j in range(self.videos[i].duration):
                        self.videos[i].time_now += 1
                        print(self.videos[i].time_now, end=' ')
                        sleep(1)
                        if self.videos[i].time_now == self.videos[i].duration:
                            print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')











































