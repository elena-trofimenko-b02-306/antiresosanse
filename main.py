import pygame as pg
import numpy as np
import thorpy
import time
from draw_and_move import *
from phys_modelling import *
timer = None


alive = True

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

model_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

time_scale = 1 #1 секунда, так как, скорее всего, все величины будем задавать в СИ
"""Шаг по времени при моделировании.
Тип: float"""
def execution(delta):
    """Функция исполнения -- запускает прорисовку тел и пружин.
    """
    global model_time
    global displayed_time
    """Тут должно быть что-то из draw_and_move, но пока мы это еще не прописали""" #FIXME
    model_time += delta
def start_execution():
    """Обработчик события нажатия на кнопку Начать.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True

def pause_execution():
    global perform_execution
    perform_execution = False

def stop_execution():
    """Обработчик события нажатия на кнопку Выйти.
    Останавливает циклическое исполнение функции execution.
    """
    global alive
    alive = False






