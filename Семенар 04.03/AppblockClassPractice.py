class AppBlocks(object):
    def __init__(self, floors, entrances, district, workers = [], const_fin = '01.01.2001'):
        self.floors = floors
        self.entrances = entrances
        self.district = district
        self.workers = workers
        self.const_fin = const_fin

    def YearAndTeam(self):
        if self.floors<=3:
            self.const_fin = '01.02.2026'
            self.workers = self.workers[:2]
        elif 3<self.floors<=5:
            self.const_fin = '02.03.2027'
            self.workers = self.workers[1:]
        elif self.floors>5:
            self.const_fin = '12.01.2029'
            self.workers = self.workers[::1]

    def workers(self):
        return self.workers

    def Info(self):
        return f'Floors: {self.floors} Entrances: {self.entrances} District: {self.district} {self.const_fin}'


class Workers(object):
    def __init__(self, b_c_name, qualification):
        self.b_c_name = b_c_name
        self.qualification = qualification

    def Info(self):
            return (f'Название строительной компании: {self.b_c_name}\n '
                    f'Квалификация рабочего: {self.qualification}')

    def WorkerAdd():
        workers = []
        for i in range(0,3):
            b_c_name = input('Введите название строительной компании имя: ')
            qualification = input('Введите квалификацию рабочего: ')
            workers.append(Workers(b_c_name, qualification))
        return workers


worker_list = Workers.WorkerAdd()

for i in worker_list:
    print(i.Info())

appblock_1 = AppBlocks(3, 4, 'NE district', worker_list)
appblock_1.YearAndTeam()
appblock_2 = AppBlocks(5, 3, 'NW district', worker_list)
appblock_2.YearAndTeam()
appblock_3 = AppBlocks(10, 1, 'SW district', worker_list)
appblock_3.YearAndTeam()
print(appblock_1.Info())
print(appblock_2.Info())
print(appblock_3.Info())


