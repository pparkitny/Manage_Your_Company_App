import pytest
import uuid
from django.contrib.auth.models import User


def client():
  client = Client()
  return client


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def create_user(django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.mark.django_db
def test_dashboard_view1(client, create_user, test_password):  # sprawdzamy czy po zalogowaniu mamy dostęp do pulpitu
   user = create_user()
   url = '/dashboard/'
   client.login(
       username=user.username, password=test_password
   )
   response = client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db
def test_dashboard_view2(client):  # sprawdzamy czy mamy dostęp nie logując się
   url = '/dashboard/'
   response = client.get(url)

   assert response.status_code == 302
