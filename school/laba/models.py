from django.db import models


class StudentClass(models.Model):
    level = models.IntegerField("Номер класса")
    main_cabinet = models.IntegerField("Номер кабинета")
    school_number = models.IntegerField("Номер школы")

    def __str__(self):
        return f"Класс - {self.level}"


class Student(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=100)
    height = models.IntegerField("Рост, в см")
    weight = models.IntegerField("Вес, в кг")
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    

