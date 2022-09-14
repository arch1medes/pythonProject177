import requests

# fixtures

# Only directors * task is tested here, genres were done via Postman as I'm too lazy I guess

DIRECTOR_POST_DATA = {
    "name": "Вася Внедренный"
}

# UID not used in test below, kept for possible use in the future
DIRECTOR_PUT_UID = 21

DIRECTOR_PUT_DATA = {
    "name": "Вася Измененный"
}

# UID not used in test below, kept for possible use in the future
DIRECTOR_DELETE_UID = 21


class Directors:
    URL = 'http://127.0.0.1:5000/directors/'

    @staticmethod
    def post():
        response = requests.post(Directors.URL, json=DIRECTOR_POST_DATA)
        print(response)
        if response.status_code == 201:
            return response.json()
        else:
            return response.text

    @staticmethod
    def put(uid: int):
        response = requests.put(f'{Directors.URL}{str(uid)}/', json=DIRECTOR_PUT_DATA)
        print(response)
        if response.status_code == 204:
            return ''
        else:
            return response.text

    @staticmethod
    def delete(uid: int):
        response = requests.delete(f'{Directors.URL}{str(uid)}/')
        print(response)
        if response.status_code == 204:
            return ''
        else:
            return response.text

    @staticmethod
    def get_one(uid: int):
        response = requests.get(f'{Directors.URL}{str(uid)}/')
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    @staticmethod
    def get_all():
        response = requests.get(Directors.URL)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text


def test_directors():
    print('Testing directors...')

    print(Directors.post())
    b = Directors.get_one(DIRECTOR_PUT_UID)
    print(b)
    if b['name'] == DIRECTOR_POST_DATA['name']:
        print('Post single director: Ok!\n')
    else:
        print('Post single director: ERROR!')
        exit()

    print(Directors.put(DIRECTOR_PUT_UID))
    b = Directors.get_one(DIRECTOR_PUT_UID)
    print(b)
    if b['name'] == DIRECTOR_PUT_DATA['name']:
        print('Put single director: Ok!\n')
    else:
        print('Put single director: ERROR!')
        exit()

    print(Directors.delete(DIRECTOR_DELETE_UID))
    all_users = Directors.get_all()
    if all_users[-1]['id'] == DIRECTOR_DELETE_UID - 1:
        print('Delete single user: Ok!\n')
    else:
        print('Delete single user: ERROR!')
        exit()


def main():
    test_directors()


if __name__ == '__main__':
    main()
