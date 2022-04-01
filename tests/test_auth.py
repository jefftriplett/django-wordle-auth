import pytest
import datetime


@pytest.fixture
def password():
    return "snout"


@pytest.fixture
def older_password():
    return "mimic"


@pytest.fixture
def bad_password():
    return "moist"


@pytest.fixture
def testing_user(django_user_model, password):
    return django_user_model.objects.create_user(username="username")


def test_valid_password(db, tp, time_machine, testing_user, password):
    time_machine.move_to(datetime.datetime(2022, 4, 1, 23, 00))
    response = tp.client.login(username=testing_user.username, password=password)
    assert response is True


def test_valid_older_password(db, tp, time_machine, testing_user, older_password):
    time_machine.move_to(datetime.datetime(2021, 8, 6, 23, 00))
    response = tp.client.login(username=testing_user.username, password=older_password)
    assert response is True


def test_bad_password(db, tp, time_machine, testing_user, bad_password):
    time_machine.move_to(datetime.datetime(2022, 4, 1, 23, 00))
    response = tp.client.login(username=testing_user.username, password=bad_password)
    assert response is False


def test_out_of_range(db, tp, time_machine, testing_user, password):
    time_machine.move_to(datetime.datetime(2021, 4, 1, 23, 00))
    response = tp.client.login(username=testing_user.username, password=password)
    assert response is False
