
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from appAPI import views as api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    
    
    path('classroom/', api_views.ClassroomList.as_view(), name="classroom-list-API"), 


    path('classroom/<int:classroom_id>/', api_views.ClassroomDetails.as_view(), name="classroom-detail-API"),
    path('classroom/<int:classroom_id>/update/', api_views.UpdateClassroom.as_view(), name="classroom-update-API"),
    path('classroom/<int:classroom_id>/cancel/', api_views.CancelClassroom.as_view(), name="classroom-cancel"),

    path('classroom/create/', api_views.CreateClassroom.as_view(), name="classroom-create-API"),


    path('api/token/', TokenObtainPairView.as_view(), name='login'),

    ]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
