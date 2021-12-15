import pytest


def client():
  client = Client()
  return client


@pytest.mark.django_db
def test_main_site_view1(client):  # sprawdzamy czy możemy wejść na stronę główną
  response = client.get('//')
  assert response.status_code == 200

