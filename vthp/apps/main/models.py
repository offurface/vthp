from django.db import models

REASON_FOR_SKIPPING = (
    (1, "Некоторые инфекционные и паразитарные болезни"),
    (2, "Новообразования"),
    (3, "Болезни крови, кроветворных органов и отдельные нарушения, вовлекающие иммунный механизм"),
    (4, "Болезни эндокринной системы, расстройства питания и нарушения обмена веществ"),
    (5, "Психические расстройства и расстройства поведения"),
    (6, "Болезни нервной системы"),
    (7, "Болезни глаза и его придаточного аппарата"),
    (8, "Болезни уха и сосцевидного отростка"),
    (9, "Болезни системы кровообращения"),
    (10, "Болезни органов дыхания"),
    (11, "Болезни органов пищеварения"),
    (12, "Болезни кожи и подкожной клетчатки"),
    (13, "Болезни костно-мышечной системы и соединительной ткани"),
    (14, "Болезни мочеполовой системы"),
    (15, "Беременность, роды и послеродовой период"),
    (16, "Отдельные состояния, возникающие в перинатальном периоде"),
    (17, "Врожденные аномалии [пороки развития], деформации и хромосомные нарушения"),
    (18, "Симптомы, признаки и отклонения от нормы, выявленные при клинических и лабораторных исследованиях, не классифицированные в других рубриках"),
    (19, "Травмы, отравления и некоторые другие последствия воздействия внешних причин"),
    (20, "Внешние причины заболеваемости и смертности"),
    (21, "Факторы, влияющие на состояние здоровья населения и обращения в учреждения здравоохранения"),
    (22, "Осмотр после лечения"),
    (23, "Медицинская консультаци"),
    (24, "Донорство крови"),
    (25, "Сдача анализов"),
    (26, "Отсутствие без объяснения причины"),
    (27, "Психотерапия "),
    (28, "Посещение стоматолога"),
)
PASS_MONTH = (
    (1, "Январь"),
    (2, "Февраль"),
    (3, "Март"),
    (4, "Апрель"),
    (5, "Май"),
    (6, "Июнь"),
    (7, "Июль"),
    (8, "Август"),
    (9, "Сентябрь"),
    (10, "Октябрь"),
    (11, "Ноябрь"),
    (12, "Декабрь"),
)
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
FIRST_EDUCATION = (
    (1, "Школа"),
    (2, "Высшее"),
    (3, "Аспирантура"),
    (4, "Докторантура"),
)


class File(models.Model):
    title = models.CharField(max_length=150,
    verbose_name="Подпись")

    document = models.FileField(upload_to='documents/',
    verbose_name="Подпись")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

class Student(models.Model):
    number = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Идентификационный номер")

    reason_for_skipping = models.PositiveIntegerField(choices=REASON_FOR_SKIPPING, blank=True, null=True,
    verbose_name="Причина пропуска")

    pass_month = models.PositiveIntegerField(choices=PASS_MONTH, blank=True, null=True,
    verbose_name="Месяц пропуска")

    day_of_the_week = models.PositiveIntegerField(choices=DAYS, blank=True, null=True,
    verbose_name="День недели")

    season = models.PositiveIntegerField(choices=SEASON, blank=True, null=True,
    verbose_name="Время года")

    transportation_costs = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Траты на транспорт")

    distance = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Расстояние от дома до места обучения")

    age = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Возраст")

    disciplinary_action = models.BooleanField(
    verbose_name="Дисциплинарное взыскание")

    first_education = models.PositiveIntegerField(choices=FIRST_EDUCATION, blank=True, null=True,
    verbose_name="Первое образование")

    amount_of_children = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Количество детей")

    drinks = models.BooleanField(
    verbose_name="Выпивает")

    smoking = models.BooleanField(
    verbose_name="Курит")

    number_of_pets = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Количество домашних животных")

    weight = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Вес")

    height = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Рост")

    body_mass_index = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Индекс массы тела")

    missed_academic_hours = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Пропущено академических часов")

    def __str__(self):
        return "student"

    class Meta:
        #ordering = ("surname",)
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
