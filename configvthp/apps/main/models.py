from django.db import models

DAYS = (
    (1, "Понедельник"),
    (2, "Вторник"),
    (3, "Среда"),
    (4, "Четверг"),
    (5, "Пятница"),

)
SEASON = (
    (1, "Лето"),
    (2, "Осень"),
    (3, "Зима"),
    (4, "Весна"),
)
EDUCATION = (
    (1, "Школа"),
    (2, "Высшее"),
    (3, "Аспирантура"),
    (4, "Докторантура"),
)
REASON_FOR_SKIPPING = (
    (1, "Некоторые инфекционные и паразитарные болезни"),
    (2, "Новообразования"),
    (3, "Болезни крови, кроветворных органов и отдельные нарушения, вовлекающие иммунный механизм"),
    (4, ""),
    (5, ""),
    (6, ""),
    (7, ""),
    (8, ""),
    (9, ""),
    (10, ""),
    (11, ""),
    (12, ""),
    (13, ""),
    (14, ""),
    (15, ""),
    (16, ""),
    (17, ""),
    (18, ""),
    (19, ""),
    (20, ""),
    (21, ""),
    (22, ""),
    (23, ""),
    (24, ""),
    (25, ""),
    (26, ""),
    (27, ""),
    (28, ""),
)


class Student(models.Model):
    dynamometry_left = models.PositiveIntegerField(choices=REASON_FOR_SKIPPING, blank=True, null=True,
    verbose_name="Причина пропуска")
    dynamometry_left = models.PositiveIntegerField(choices=REASON_FOR_SKIPPING, blank=True, null=True,
    verbose_name="Месяц пропуска")
    dynamometry_left = models.PositiveIntegerField(choices=DAYS, blank=True, null=True,
    verbose_name="День недели")
    dynamometry_left = models.PositiveIntegerField(choices=SEASON, blank=True, null=True,
    verbose_name="Время года")

    dynamometry_left = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Траты на транспорт")
    dynamometry_left = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Расстояние от дома до места обучения")
    dynamometry_left = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Возраст")
    dynamometry_left = models.BooleanField(
    verbose_name="Дисциплинарное взыскание")

    def __str__(self):
        return "student"

    class Meta:
        #ordering = ("surname",)
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
