## Instructions

1. Install using pip:

    ```
    $ pip install git+https://github.com/marcelogumercinocosta/django-google-oauth-simple.git

2. Add `django_google_oauth` to `INSTALLED_APPS` in `settings.py`:

    ```python
    INSTALLED_APPS = (
        ...
        'django_goo_oauth_simple',
    )

3. Add google OAuth base url to your project's `urls.py`:

    ```python
    urlpatterns = [
        ...
        path("google/", include("django_google_oauth_simple.urls")),
        ...
    ]
    ```

4. Specify your google credentials and OAuth Scope in `settings.py`:

    ```python
    LOGOUT_REDIRECT_URL = 'home'
    LOGIN_REDIRECT_URL = "home"
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('google_CLIENT_ID')
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('google_CLIENT_SECRET')
    ```


## Example

Add a link to google OAuth in one of your templates:

```
<a href='{% url 'google_oauth' %}'>Get googleed</a>
