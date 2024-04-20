# -*- coding: utf-8 -*-
import random
import string
from model.project import Project
from enums.letter import Letter


def get_random_string(length, letter=None):
    rus_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if letter == Letter.eng or letter is None:
        letters = string.ascii_letters
    elif letter == Letter.dig:
        letters = string.digits
    elif letter == Letter.eng_rus:
        letters = rus_letters + string.ascii_letters
    elif letter == Letter.eng_rus_dig:
        letters = rus_letters + string.ascii_letters + string.digits
    elif letter == Letter.rus:
        letters = rus_letters
    elif letter == Letter.all:
        letters = string.ascii_letters + string.digits + string.punctuation + rus_letters
    # если ничего из  перечисленного
    else:
        letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_random_status():
    statuses = ["development", "release", "stable", "obsolete"]
    return random.choice(statuses)


def get_random_view_status():
    statuses = ["public", "private"]
    return random.choice(statuses)


def get_random_project():
    return Project(project_name="Project-name-" + get_random_string(10, Letter.eng_rus_dig),
                   status=get_random_status(), inherit_global_categories=bool(random.getrandbits(1)),
                   view_status=get_random_view_status(),
                   description="Description-" + get_random_string(10, Letter.eng_rus_dig))
