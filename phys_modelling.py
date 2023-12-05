"""Отвечает за физическое моделирование процесса"""


class Spring:
    """Класс, задающий пружину.Пружина имеет жесткость, длину в нерастянутом состоянии и текущую длину
    """

    def __init__(self):
        self.x0 = 1  # длина нерастянутого состояние
        self.x = 1  # текущая длина, я пока вбила случанйые значения.
        self.k = 4


class Gruz:
    """Класс, задающий груз. У груза есть масса, текущие координата, скорость и ускорение"""

    def __init__(self):
        self.m = 1  # масса
        self.x = 1  # координата x
        self.v = 1  # проекция скорости на ось x, может быть отрицательной
        self.a = 1  # проекция ускорения на ось x, может быть отрицательным
        self.F = 0  #

    def calc_force_driven(self, time, ampl, omega_ext, obj, spring1, spring2):
        """"Функция, вычисляющая суммарную силу, действующую на груз, к которому приложена вынуждающая сила"""
        """Принимает время, амплитуду и частоту вынуждающей силы, а так же данные о втором грузе  пружинах"""
        self.F = ampl * np.cos(omega_ext * time)
        self.F -= spring1.k * (self.x - spring1.x0) + spring2.k * (self.x - obj.x - spring2.x0)

    def calc_force_free(self, obj, spring2):
        """"Функция, вычисляющая суммарную силу, действующую на свободный груз"""
        self.F = -spring2.k * (self.x - obj.x - spring2.x0)

    def move(self, dt):
        """Функция, пересчитывающая координаты грузов, принимает минимальный интервал времени"""
        self.a = self.F / self.m
        self.x += self.v * dt + self.a * dt**2 / 2
        self.v += self.a * dt



"""Думаю, прописать силы стоит уже в phys_mpdelling.зщкмлжди"""
