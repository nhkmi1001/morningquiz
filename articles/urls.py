from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='ArticleList'),
    path('<int:article_id>/', views.ArticleDetail.as_view(), name='ArticleDetail'),
    
]
