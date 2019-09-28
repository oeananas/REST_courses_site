from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    skill_info = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return f'Teacher {self.name}'


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teachers = models.ManyToManyField(Teacher, related_name='courses')

    objects = models.Manager()

    def __str__(self):
        return f'Course {self.title}'


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, related_name='lessons', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'Lesson {self.title}'
