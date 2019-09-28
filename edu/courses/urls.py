from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('courses/', views.CourseViewSet.as_view({'get': 'list',
                                                  'post': 'create'}), name='courses'),
    path('courses/<int:pk>/', views.CourseViewSet.as_view({'get': 'retrieve',
                                                           'put': 'update',
                                                           'patch': 'partial_update',
                                                           'delete': 'destroy'}), name='course'),
    path('lessons/', views.LessonViewSet.as_view({'get': 'list',
                                                  'post': 'create'}), name='lessons'),
    path('<int:course_pk>/lessons/', views.LessonViewSet.as_view({'get': 'course_list',
                                                                  'post': 'create'}), name='course_lessons'),
    path('lessons/<int:pk>/', views.LessonViewSet.as_view({'get': 'retrieve',
                                                           'put': 'update',
                                                           'patch': 'partial_update',
                                                           'delete': 'destroy'}), name='lesson'),
    path('teachers/', views.TeacherViewSet.as_view({'get': 'list',
                                                    'post': 'create'}), name='teachers'),
    path('<int:course_pk>/teachers/', views.TeacherViewSet.as_view({'get': 'course_list',
                                                                    'post': 'create'}), name='course_teachers'),
    path('teachers/<int:pk>/', views.TeacherViewSet.as_view({'get': 'retrieve',
                                                             'put': 'update',
                                                             'patch': 'partial_update',
                                                             'delete': 'destroy'}), name='teacher'),
]
