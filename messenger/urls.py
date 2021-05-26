from django.urls import path

from .views import main, new_message, SignUpView, channel

urlpatterns = [
  path('', main),
  path('new/', new_message),
  path('signup/', SignUpView.as_view()),
  path('channel/<str:title>/', channel, name='channel'),
]