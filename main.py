import pygame as pg
import numpy as np
import thorpy
import time
from draw_and_move import *
from phys_modelling import *

class Spring():
    """Класс, задающий пружину.Пружина имеет жесткость, длину в нерастянутом состоянии и текущую длину
    """
    def __init__(self):
        self.x0=1     #длина нерастянутого состояние
        self.x = 1  #текущая длина, я пока вбила случанйые значения.
        self.k = 4

class Gruz():
    """Класс, задающий груз. У груза есть масса, текущие координата, скорость и ускорение"""
    def __init__(self):
        self.m=1 #масса
        self.x = 1 # координата x
        self.v = 1 #проекция скорости на ось x, может быть отрицательной
        self.a = 1 #проекция ускорения на ось x, может быть отрицательным




"""Думаю, прописать силы стоит уже в phys_mpdelling"""