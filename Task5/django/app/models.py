from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    rarity = models.CharField(max_length=50, verbose_name='Редкость')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50, verbose_name='Никнейм персонажа')
    class_name = models.CharField(max_length=10, verbose_name='Класс')
    lvl = models.IntegerField(verbose_name='Уровень')
    inventory = models.OneToOneField(Item, on_delete=models.CASCADE, verbose_name='Инвентарь')

    def __str__(self):
        return self.name


class Profile(models.Model):
    username = models.CharField(unique=True, max_length=50, verbose_name='Никнейм')
    hours_played = models.IntegerField(verbose_name='Количество часов сыграно')
    characters_count = models.IntegerField(verbose_name='Количество персонажей')
    characters = models.ManyToManyField(Character, verbose_name='Персонажи')

    def __str__(self):
        return self.username