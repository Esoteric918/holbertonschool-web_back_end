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
    - Update @app.before_request in api/v1/app.py:
        - Assign the result of auth.current_user(request) to request.current_user
    - Update method for the route GET /api/v1/users/<user_id> in api/v1/views/users.py:
        - If <user_id> is equal to me and request.current_user is None: abort(404)
        - If <user_id> is equal to me and request.current_user is not None: return the authenticated User in a JSON response (like a normal case of GET /api/v1/users/<user_id> where <user_id> is a valid User ID)
        - Otherwise, keep the same behavior

- Test with
    in the first terminal
     ```API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app```

##### In a second terminal:

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
    - Update api/v1/app.py for instance of AUTH_TYPE is = to session_auth
        - import SessionAuth from api.v1.auth.session_auth
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
