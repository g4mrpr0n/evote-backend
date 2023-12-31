from django.urls import path
from userhistory import views

urlpatterns = [
    path('', views.UserHistoryList.as_view()),
    path('vote/status-test', views.delete_user_vote),
    path('vote/<int:person_id>', views.get_user_vote_status),
]