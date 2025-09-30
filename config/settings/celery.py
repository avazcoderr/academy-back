CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP =True
CELERY_RESULT_EXTENDED = True


from celery.schedules import schedule


# CELERY_BEAT_SCHEDULE = {
#     'create-products-every-3-seconds': {
#         'task': 'apps.products.tasks.create_product',
#         'schedule': 3.0,
#         'args': ()
#     },
#     'create store': {
#         'task': 'apps.tests.tasks.remember_every_2_second',
#         'schedule': 2.0,
#         'args': ()
#     },
# }
#
