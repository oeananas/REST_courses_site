from rest_framework import serializers

from .models import Course
from .models import Teacher
from .models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = 'id'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = 'id'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = 'id'
