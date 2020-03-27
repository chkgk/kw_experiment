from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
    mturk_hit_settings=dict(
        keywords='bonus, study, research, decision making',
        title='Short Decision-Making Task',
        description='Make a total of six decisions taking less then 10 minutes.',
        frame_height=700,
        template='global/mturk_template.html',
        minutes_allotted_per_assignment=20,
        expiration_hours=2 * 24,
        qualification_requirements=[
            {
                'QualificationTypeId': '00000000000000000071',
                'Comparator': 'EqualTo',
                'LocaleValues':  [{'Country': "US"}]
            },
            {
                'QualificationTypeId': '3DUIEQIYL66N062LWCCQO5MIE7TY24',
                'Comparator': 'DoesNotExist'
            }
        ],
        grant_qualification_id='3DUIEQIYL66N062LWCCQO5MIE7TY24', # to prevent retakes
    )
)

SESSION_CONFIGS = [
    dict(
        name='kwtask_original',
        display_name="Krupka Weber Task / Original",
        num_demo_participants=2,
        app_sequence=['kwtask'],
        participation_fee=0.50,
        treatment="original"
    ),
    dict(
        name='kwtask_always',
        display_name="Krupka Weber Task / Always",
        num_demo_participants=2,
        app_sequence=['kwtask'],
        participation_fee=0.50,
        treatment="always remind"
    ),
    dict(
        name='kwtask_never',
        display_name="Krupka Weber Task / Never",
        num_demo_participants=2,
        app_sequence=['kwtask'],
        participation_fee=0.50,
        treatment="never remind"
    ),
    dict(
        name='kwtask_inventives',
        display_name="Krupka Weber Task / No Incentives",
        num_demo_participants=2,
        app_sequence=['kwtask'],
        participation_fee=0.50,
        treatment="no incentives"
    )
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'jq6f)a2r1ql&pdq=ac2!*vcxawb$thayb03q3z@6f!!c31g1_o'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

ROOT_URLCONF = 'kwtask.urls'

# for recaptcha
RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUBLIC_KEY', 'none')
RECAPTCHA_PRIVATE_KEY = environ.get('RECAPTCHA_PRIVATE_KEY', 'none')

EXTENSION_APPS = [
    'captcha',
]