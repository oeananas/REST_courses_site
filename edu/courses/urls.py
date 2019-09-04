from django.urls import path

from . import views

urlpatterns = [
    path('', views.CourseViewSet.as_view({'get': 'list',
                                          'post': 'create'})),
    path('<int:pk>/', views.CourseViewSet.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'})),
    path('<int:course_pk>/lessons/', views.LessonViewSet.as_view({'get': 'list',
                                                                  'post': 'create'})),
    path('lessons/<int:pk>/', views.LessonViewSet.as_view({'get': 'retrieve',
                                                           'put': 'update',
                                                           'patch': 'partial_update',
                                                           'delete': 'destroy'})),
    path('<int:course_pk>/teachers/', views.TeacherViewSet.as_view({'get': 'list',
                                                                    'post': 'create'})),
    path('teachers/<int:pk>/', views.TeacherViewSet.as_view({'get': 'retrieve',
                                                             'put': 'update',
                                                             'patch': 'partial_update',
                                                             'delete': 'destroy'})),
]
