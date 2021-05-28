from django.urls import path, include
from . import views

app_name = 'ssapp'

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path('dashboard', views.Dashboard.as_view(), name='dashboard'),
    path('curriculum', views.UserCurriculum.as_view(), name='curriculum'),
    path('course', views.UserEnrollCourse.as_view(), name='course'),
    path('ssapp/<str:pk>/profile', views.DetailProfile.as_view(), name='profile'),
    path('signup', views.Signup.as_view(), name='signup'),
#    path('curriculum/unenroll', views.unenroll_course_from_curriculum, name="unenroll_course"),

    path('ssapp/admin/dashboard', views.AdminDashboard.as_view(), name="admin_dashboard"),
    path('ssapp/admin/course', views.AdminCourse.as_view(), name="admin_course"),
    path('ssapp/admin/<str:pk>/course', views.AdminDetailCourse.as_view(), name="admin_class"),
    path("ssapp/admin/curriculum", views.AdminCurriculum.as_view(), name="admin_curriculum"),
    path("ssapp/admin/<int:pk>/curriculum", views.AdminDetailCurriculum.as_view(), name="admin_detail_curriculum"),
    path("ssapp/admin/<int:curr_id>/curriculum/generate_ge_courses", views.auto_add_ge_courses, name='add_ge_courses'),
    path("ssapp/admin/<int:curr_id>/curriculum/<str:course_id>/drop", views.drop_course_from_curriculum, name='drop_course_from_curriculum'),


]
