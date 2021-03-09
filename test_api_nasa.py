import pytest
from constants import Constants
from PIL import Image
import requests
import sys

def test_api_status_ok(api_client):
    res = api_client.get()
    assert res.ok


@pytest.mark.parametrize('date', [Constants.YESTERDAY, Constants.TODAY, '1995-06-16'])
def test_api_valid_date(api_client, date):
    res = api_client.get(
        params={'date': date}
    )
    assert res.json()['date'] == date


@pytest.mark.parametrize('date',
                         [Constants.RANDOM_DATE_FUTURE, Constants.TOMORROW, '1995-06-15', Constants.RANDOM_DATE_PAST])
def test_api_invalid_date(api_client, date):
    res = api_client.get(
        params={'date': date}
    )
    assert res.status_code == 400


@pytest.mark.parametrize('start_date, end_date', [(Constants.YESTERDAY, Constants.TODAY), \
                                                  (Constants.TODAY, Constants.TODAY), (Constants.RANDOM_DATE_VALID_1, \
                                                                                       Constants.RANDOM_DATE_VALID_2),
                                                  ('1995-06-16', Constants.RANDOM_DATE_VALID_1)])
def test_api_valid_start_date_and_valid_end_date(api_client, start_date, end_date):
    res = api_client.get(
        params={'start_date': start_date,
                'end_date': end_date
                }
    )
    assert res.json()[0]['date'] == start_date and res.json()[-1]['date'] == end_date


@pytest.mark.parametrize('start_date, end_date', [(Constants.TODAY, Constants.TOMORROW), \
                                                  (Constants.RANDOM_DATE_FUTURE, Constants.RANDOM_DATE_FUTURE_2), \
                                                  (Constants.RANDOM_DATE_PAST, Constants.RANDOM_DATE_PAST_2)])
def test_api_invalid_start_date_and_invalid_end_date(api_client, start_date, end_date):
    res = api_client.get(
        params={'start_date': start_date,
                'end_date': end_date
                }
    )
    assert res.status_code == 400


def test_api_valid_count_array(api_client):
    x = Constants.RANDOM_NUMBER
    res = api_client.get(
        params={'count': x,
                }
    )
    assert (len(res.json())) == x


@pytest.mark.parametrize('count', [Constants.RANDOM_NUMBER_INVALID, Constants.RANDOM_NUMBER_INVALID_NEG])
def test_api_invalid_count_array(api_client, count):
    res = api_client.get(
        params={'count': count,
                }
    )
    assert res.json()['msg'] == 'Count must be positive and cannot exceed 100' and \
           res.status_code == 400


def test_api_valid_type(api_client):
    res = api_client.get()
    assert res.json()['media_type'] in ('image', 'video')

def test_api_image_opens(api_client):
    res = api_client.get()
    url = res.json()['url']
    try:
        resp = requests.get(url, stream=True).raw
    except requests.exceptions.RequestException as e:
        sys.exit(1)

    try:
        img = Image.open(resp)
    except IOError:
        print("Unable to open image")
        sys.exit(1)

    img.save('picture_of_the_day.jpg', 'jpeg')


def test_api_image_url_hdurl_are_the_same(api_client):
    res = api_client.get()
    url = res.json()['url'].split('/')
    hdurl = res.json()['hdurl'].split('/')
    assert url[5] == hdurl[5]
