from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.TopView.as_view(), name = 'top'),
    path('index/', views.IndexView.as_view(), name = 'index'),
    path('article/<int:pk>/', views.ArticleDetail.as_view(), name = 'detail'),
    #path('category/<int:pk>/', views.CategoryView.as_view(), name = 'category'),
    path('category/<str:category>', views.CategoryView.as_view(), name = 'category'),
]