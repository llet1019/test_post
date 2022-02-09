from django.urls import path
from . import views


urlpatterns = [
    path('board', views.BoardList.as_view()),
    path('board/<int:board_id>', views.PostList.as_view()),
    path('post/<int:post_id>', views.PostDetail.as_view()),

]