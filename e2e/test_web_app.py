import pytest

from flask import session


def test_register(client):
    # Check that we retrieve the register page.
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    # Check that we can register a user successfully, supplying a valid username and password.
    response = client.post(
        '/authentication/register',
        data={'username': 'gmichael', 'password': 'CarelessWhisper1984'}
    )
    assert response.headers['Location'] == 'http://localhost/authentication/login'


@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('', '', b'Your username is required'),
        ('cj', '', b'Your username is too short'),
        ('test', '', b'Your password is required'),
        ('test', 'test', b'Your password must be at least 8 characters, and contain an upper case letter, '
                         b'a lower case letter and a digit'),
        ('fmercury', 'Test#6^0', b'Your username is already taken - please supply another'),
))
def test_register_with_invalid_input(client, username, password, message):
    # Check that attempting to register with invalid combinations of username and password generate appropriate error
    # messages.
    response = client.post(
        '/authentication/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    # Check that we can retrieve the login page.
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200

    # Check that a successful login generates a redirect to the homepage.
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    # Check that a session has been created for the logged-in user.
    with client:
        client.get('/')
        assert session['username'] == 'thorke'


def test_logout(client, auth):
    # Login a user.
    auth.login()

    with client:
        # Check that logging out clears the user's session.
        auth.logout()
        assert 'user_id' not in session


def test_index(client):
    # Check that we can retrieve the home page.
    response = client.get('/')
    assert response.status_code == 200
    assert b'The Movie Channel.123' in response.data


def test_login_required_to_comment(client):
    response = client.post('/comment')
    assert response.headers['Location'] == 'http://localhost/authentication/login'


def test_comment(client, auth):
    # Login a user.
    auth.login()

    # Check that we can retrieve the comment page.
    response = client.get('/comment?movie=2')

    response = client.post(
        '/comment',
        data={'ratting': '1', 'comment': 'Who needs quarantine?', 'movie_id': 2}
    )
    assert response.headers['Location'] != None


@pytest.mark.parametrize(('comment', 'messages'), (
        ('Who thinks Trump is a fuckwit?', (b'Your comment must not contain profanity')),
        ('Hey', (b'Your comment is too short')),
        ('ass', (b'Your comment is too short', b'Your comment must not contain profanity')),
))
def test_comment_with_invalid_input(client, auth, comment, messages):
    # Login a user.
    auth.login()

    # Attempt to comment on an movie.
    response = client.post(
        '/comment',
        data={'comment': comment, 'movie_id': 2}
    )
    print(f'\n\n\n{messages}\n\n\n{response.data}')
    # Check that supplying invalid comment text generates appropriate error messages.
    for message in messages:
        assert message in response.data


def test_movies_without_date(client):
    # Check that we can retrieve the movies page.
    response = client.get('/movies_by_date')
    assert response.status_code == 200

    # Check that without providing a date query parameter the page includes the first movie.
    assert b'2014' in response.data
    assert b'guardians of the galaxy' in response.data


def test_movies_with_date(client):
    # Check that we can retrieve the movies page.
    response = client.get('/movies_by_date?date=2014')
    assert response.status_code == 200

    # Check that all movies on the requested date are included on the page.
    assert b'2014' in response.data
    assert b'A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.' in response.data


def test_movies_with_comment(client):
    # Check that we can retrieve the movies page.
    response = client.get('/movies_by_date?date=2014&view_comments_for=1')
    assert response.status_code == 200

    # Check that all comments for specified movie are included on the page.
    assert b'This film is good!' in response.data
    assert b'Yes! I like it!' in response.data


def test_movies_with_genre(client):
    # Check that we can retrieve the movies page.
    response = client.get('/movies_by_genre?genre=action')
    assert response.status_code == 200

    # Check that all movies tagged with 'action' are included on the page.
    assert b'Action Movies' in response.data
    assert b'guardians of the galaxy' in response.data
    assert b'A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.' in response.data

