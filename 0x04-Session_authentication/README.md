# 0x04. Session authentication

# Background Context
    In this project, you will implement a Session Authentication.
    You are not allowed to install any other module.

    In the industry, you should not implement your own Session authentication
    system and use a module or framework that doing it for you
    (like in Python-Flask: Flask-HTTPAuth). Here, for the learning purpose, we
    will walk through each step of this mechanism to understand it by doing.
## Learing Objectives
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## Tasks

0. Et moi et moi et moi!
- Copy 0x03-Basic_authentication project in this new folder.
    - Update @app.before_request in [api/v1/app.py](https://github.com/Esoteric918/holbertonschool-web_back_end/blob/main/0x04-Session_authentication/api/v1/app.py):
        - Assign the result of auth.current_user(request) to request.current_user
    - Update method for the route GET /api/v1/users/<user_id> in [api/v1/views/users.py](https://github.com/Esoteric918/holbertonschool-web_back_end/blob/main/0x04-Session_authentication/api/v1/views/users.py):
        - If <user_id> is equal to me and request.current_user is None: abort(404)
        - If <user_id> is equal to me and request.current_user is not None: return the authenticated User in a JSON response (like a normal case of GET /api/v1/users/<user_id> where <user_id> is a valid User ID)
        - Otherwise, keep the same behavior

- Test with
    in the first terminal
     ```API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app```

In a second terminal:

    ``` curl "http://0.0.0.0:5000/api/v1/status"
        {"status": "OK"}

        curl "http://0.0.0.0:5000/api/v1/users"
        {"status": "OK"}

        curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
        [
            {
                "created_at": "2017-09-25 01:55:17",
                "email": "bob@hbtn.io",
                "first_name": null,
                "id": "9375973a-68c7-46aa-b135-29f79e837495",
                "last_name": null,
                "updated_at": "2017-09-25 01:55:17"
            }
        ]

        curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
        {
          "created_at": "2017-09-25 01:55:17",
          "email": "bob@hbtn.io",
          "first_name": null,
          "id": "9375973a-68c7-46aa-b135-29f79e837495",
          "last_name": null,
          "updated_at": "2017-09-25 01:55:17"
        }
    ```

1. Empty session
- Create class SessionAuth to inherit Auth in api.v1.auth.session_auth
    - Update [api/v1/app.py](https://github.com/Esoteric918/holbertonschool-web_back_end/blob/main/0x04-Session_authentication/api/v1/app.py) for instance of AUTH_TYPE is = to session_auth
        - import SessionAuth from [api.v1.auth.session_auth](https://github.com/Esoteric918/holbertonschool-web_back_end/blob/main/0x04-Session_authentication/api/v1/auth/session_auth.py)
        - create an instance of SessionAuth and assign it to the variable auth
Otherwise, keep the previous mechanism.

- Test With
    in the first terminal:
    ``` API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app ```

    in a second terminal:
    ```
        curl "http://0.0.0.0:5000/api/v1/status"
        {
        "status": "OK"
        }

        curl "http://0.0.0.0:5000/api/v1/status/"
        {
        "status": "OK"
        }
         curl "http://0.0.0.0:5000/api/v1/users"
        {
        "error": "Unauthorized"
        }
        curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
        {
        "error": "Forbidden"
        }
    ```

2. Create a session
- Update SessionAuth class:
    - class attribute user_id_by_session_id initialized by an empty dictionary
    - new method def create_session(self, user_id: str = None) -> str:
        - Return None if user_id is None
        - Return None if user_id is not a string
        Otherwise:
            - Generate a Session ID using uuid module and uuid4() like id in Base
            - Use this Session ID as key of the dictionary user_id_by_session_id - the value for this key must be user_id
            - Return the Session ID
        - The same user_id can have multiple Session ID - indeed, the user_id is the value in the dictionary user_id_by_session_id

Test with
    in treminal
    ```
        API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_1.py
    ```
Results:
    ```
        <class 'dict'>: {}
        None => None: {}
        89 => None: {}
        abcde => 61997a1b-3f8a-4b0f-87f6-19d5cafee63f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde'}
        fghij => 69e45c25-ec89-4563-86ab-bc192dcc3b4f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
        abcde => 02079cb4-6847-48aa-924e-0514d82a43f4: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '02079cb4-6847-48aa-924e-0514d82a43f4': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
    ```

3.User ID for Session ID
Update SessionAuth class:

- Create an instance method def user_id_for_session_id(self, session_id: str = None) -> str: that returns a User ID based on a Session ID:

    - Return None if session_id is None
    - Return None if session_id is not a string
    - Return the value (the User ID) for the key session_id in the dictionary user_id_by_session_id.
    - You must use .get() built-in for accessing in a dictionary a value based on key

Test With
    In treminal
        ```
             API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_2.py
        ```
    Results:
    ```abcde => 8647f981-f503-4638-af23-7bb4a9e4b53f: {'8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
    fghij => a159ee3f-214e-4e91-9546-ca3ce873e975: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
    ---
    None => None
    89 => None
    doesntexist => None
    ---
    8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
    a159ee3f-214e-4e91-9546-ca3ce873e975 => fghij
    ---
    abcde => 5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde', '5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee': 'abcde'}
    5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee => abcde
    8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
    ```

