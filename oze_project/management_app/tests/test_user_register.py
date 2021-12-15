import pytest
from django.contrib.auth.models import User


def client():
  client = Client()
  return client


@pytest.mark.django_db
def test_user_register1(client):  # sprawdzamy czy można zarejestrować nowego użytkownika na stronie /register/
  client.post('/register/', {'first_name' : 'Maćko', 'last_name' : 'Polo', 'login' : 'user',
                                        'password1' : '12345' , 'password2' : '12345', 'email': '2@2.pl'})

  assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_register2(client):  # sprawdzamy czy można zarejestrować nowego użytkownika na stronie /register/
  client.post('/register/', {'first_name' : 'Adaś', 'last_name' : 'Słoik', 'login' : 'adas121',
                                        'password1' : 'qwerty' , 'password2' : 'qwerty', 'email': 'adas@wo.pl'})

  assert User.objects.count() == 1
