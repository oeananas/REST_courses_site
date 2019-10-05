from django.db.models import F
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Course
from .models import Lesson
from .models import Teacher
from .serializers import CourseSerializer
from .serializers import LessonSerializer
from .serializers import TeacherSerializer


class MyTemplateHTMLRenderer(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        response = renderer_context['response']
        if response.exception:
            data['status_code'] = response.status_code
        return {'data': data}


class MainPageView(TemplateView):
    template_name = 'courses/index.html'


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    renderer_classes = [MyTemplateHTMLRenderer]
    template_name = 'courses/course.html'


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().select_related('teacher', 'course') \
        .annotate(teacher_name=F('teacher__name'), course_title=F('course__title'))
    serializer_class = LessonSerializer
    renderer_classes = [MyTemplateHTMLRenderer]
    template_name = 'courses/lesson.html'

    def course_list(self, request, *args, **kwargs):
        queryset = Lesson.objects.filter(course_id=kwargs['course_pk'])\
            .select_related('teacher')\
            .annotate(teacher_name=F('teacher__name'))\
            .order_by('start_dt')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def course_list(self, request, *args, **kwargs):
        queryset = Course.objects.get(pk=kwargs['course_pk']).teachers

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
