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

## Task

0.
   - Copy 0x03-Basic_authentication project in this new folder.
        - Update @app.before_request in api/v1/app.py:
            - Assign the result of auth.current_user(request) to request.current_user
        - Update method for the route GET /api/v1/users/<user_id> in api/v1/views/users.py:
            - If <user_id> is equal to me and request.current_user is None: abort(404)
            - If <user_id> is equal to me and request.current_user is not None: return the authenticated User in a JSON response (like a normal case of GET /api/v1/users/<user_id> where <user_id> is a valid User ID)
            - Otherwise, keep the same behavior

       - Test with
            -


