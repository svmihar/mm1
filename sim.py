import random
import pandas as pd
import datetime
random.seed(69)  # because reasons


class Simulation:
    def __init__(self):
        self.df = pd.read_csv('tabel.csv')
        self.kol1 = list(self.df['kol1'])
        self.kol2 = list(self.df['kol2'])
        self.orang_di_rs = 0
        self.waktu = 0.0
        self.clock = datetime.datetime.now()
        self.t_dateng = self.generate_interarrival()
        self.t_pergi = float('inf')
        self.n_dateng = 0
        self.n_pergi = 0
        self.total_nunggu = 0.0

    def advance_time(self):
        t_event = min(self.t_dateng, self.t_pergi)
        self.total_nunggu += self.orang_di_rs*(t_event - self.waktu)

        self.waktu = t_event
        if self.t_dateng <= self.t_pergi:
            self.handle_arrival_event()
        else:
            self.handle_depart_event()

    def handle_arrival_event(self):
        self.orang_di_rs += 1
        self.n_dateng += 1

        if self.orang_di_rs <= 1:
            self.t_pergi = self.waktu + self.generate_service()
        self.t_dateng = self.waktu + self.generate_interarrival()
        print('dateng: ',self.t_dateng)

    def handle_depart_event(self):
        self.orang_di_rs -= 1
        self.n_pergi += 1

        # handle last departure, else, schedule next departure
        if self.orang_di_rs > 0:
            self.t_pergi = self.waktu + self.generate_service()
        else:
            self.t_pergi = float('inf')
        print('pergi: ',self.t_pergi)

    def generate_interarrival(self):
        r = random.choice(self.kol1)
        wait = 0
        if 0 < r < .125:
            wait = 45
        elif 0.1251 < r < .25:
            wait = 40
        elif .2501 < r < 0.3750:
            wait = 35
        elif .3751 < r < .5:
            wait = 30
        elif .5001 < r < .6250:
            wait = 25
        elif .6251 < r < .775:
            wait = 20
        elif .7751 < r < 1:
            wait = 15
        return wait

    def generate_service(self):
        r = random.choice(self.kol2)
        waktu = 0
        if 0 < r < .125:
            wait = 80
        elif 0.1251 < r < .25:
            wait = 75
        elif .2501 < r < 0.3750:
            wait = 70
        elif .3751 < r < .5:
            wait = 65
        elif .5001 < r < .6250:
            wait = 60
        elif .6251 < r < .775:
            wait = 55
        elif .7751 < r < 1:
            wait = 50
        return wait


if __name__ == '__main__':
    s = Simulation()
    while s.n_pergi < 5:
        s.advance_time()
    print(f"""
    total orang yang datang: {s.n_dateng}
    total orang yang ditangangi: {s.n_pergi}
    total orang yang tidak ditangangi: {s.n_dateng - s.n_pergi}
    rata-rata waktu menunggu: {s.total_nunggu/s.n_dateng}
    """)