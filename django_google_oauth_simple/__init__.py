from django.conf import settings

default_settings = {
    'LOGIN_URL': 'login',
    'LOGOUT_URL': 'logout',
    'SOCIAL_AUTH_PIPELINE': (
        'social_core.pipeline.social_auth.social_details',
        'social_core.pipeline.social_auth.social_uid',
        'social_core.pipeline.social_auth.auth_allowed',
        'social_core.pipeline.social_auth.social_user',
        'social_core.pipeline.user.get_username',
        'social_core.pipeline.social_auth.associate_by_email',
        'social_core.pipeline.user.create_user',
        'social_core.pipeline.social_auth.associate_user',
        'social_core.pipeline.social_auth.load_extra_data',
        'social_core.pipeline.user.user_details',
    ),
}

additional_settings = {
    'INSTALLED_APPS': [
        'social_django',
    ],
    'MIDDLEWARE': [
        'social_django.middleware.SocialAuthExceptionMiddleware',
    ],
    'AUTHENTICATION_BACKENDS': [
        'social_core.backends.google.GoogleOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    ],

}


class Settings(object):
    def __init__(self, defaults, additional_defaults):
        for k, v in defaults.items():
            if hasattr(settings, k):
                if getattr(settings, k) is None and k != 'LOGOUT_REDIRECT_URL':
                    raise ValueError(f"Configuração {k} não pode ser None. Configure-a corretamente.")
            else:
                setattr(settings, k, v)

        # Adiciona as configurações adicionais
        for key, values in additional_defaults.items():
            if hasattr(settings, key):
                getattr(settings, key).extend(values)
            else:
                setattr(settings, key, values)

settings_obj = Settings(default_settings, additional_settings)