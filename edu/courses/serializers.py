from rest_framework import serializers

from .models import Course
from .models import Teacher
from .models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    teacher_name = serializers.CharField(required=False)
    course_title = serializers.CharField(required=False)
    start_dt = serializers.DateTimeField(format="%d.%m.%Y %H:%M")

    class Meta:
        model = Lesson
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
