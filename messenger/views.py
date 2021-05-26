from django.shortcuts import render, redirect
from .models import Channel, Message
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Главная страница
def main(request):
  if not request.user.is_authenticated:
    return redirect('login')
  channels = Channel.objects.all()
  return render(request, 'main.html', {'channels': channels})


def channel(request, title):
  channel = Channel.objects.get(title=title)
  messages = Message.objects.filter(channel=channel.title).order_by('pub_date')
  return render(request, 'channel.html', {'messages': messages, 'channel': channel})

# Создание сообщения
def new_message(request):
  message = Message(
    text=request.POST.get('text'),
    author=request.user.username,
    channel=request.POST.get('channel'),
  )
  message.save()
  return redirect('channel', title=request.POST.get('channel'))


# Регистрация
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'