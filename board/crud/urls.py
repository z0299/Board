from django.urls import path
from . import views

app_name = 'crud'
# 여러개의 app을 만들때 동일한 url이름이 있는 경우 template사용시 엇갈리지 않게하기 위해 사용
urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('update/<int:post_id>/', views.update, name='update'),
]