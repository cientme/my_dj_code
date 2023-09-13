from time import process_time
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('-----------------------------------')
    print('Logged In Signals... Run Intro')
    print('Sender', sender)
    print('Request', request)
    print('User', user)
    print(f"Kwargs: {kwargs}")

# user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print('-----------------------------------')
    print('Logged Out Signals... Run Outro')
    print('Sender', sender)
    print('Request', request)
    print('User:', user)
    print(f"Kwargs: {kwargs}")

# user_logged_out.connect(log_out, sender=User)

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print('-----------------------------------')
    print('Login Failed Signals... Run Outro')
    print('Sender', sender)
    print('Credentials:', credentials)
    print('Request', request)
    print(f"Kwargs: {kwargs}")

# user_login_failed.connect(login_failed, sender=User)

@receiver(pre_save, sender=User)
def at_bignning_save(sender, instance, **kwargs):
    print('-----------------------------------')
    print('Pre Save Signals...')
    print('Sender', sender)
    print('Instance:', instance)
    print(f"Kwargs: {kwargs}")

# pre_save.connect(at_bignning_save, sender=User)

@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print('-----------------------------------')
        print('Post Save Signals...')
        print('New Record...')
        print('Sender', sender)
        print('Instance:', instance)
        print('Created:', created)
        print(f"Kwargs: {kwargs}")
    else:
        print('-----------------------------------')
        print('Post Save Signals...')
        print('Updated...')
        print('Sender', sender)
        print('Instance:', instance)
        print('Created:', created)
        print(f"Kwargs: {kwargs}")

# post_save.connect(at_ending_save, sender=User)


@receiver(pre_delete, sender=User)
def at_bignning_delete(sender, instance, **kwargs):
    print('-----------------------------------')
    print('Pre Delete Signals...')
    print('Sender', sender)
    print('Instance:', instance)
    print(f"Kwargs: {kwargs}")

# pre_save.connect(at_bignning_delete, sender=User)

@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print('-----------------------------------')
    print('Post Delete Signals...')
    print('Sender', sender)
    print('Instance:', instance)
    print(f"Kwargs: {kwargs}")

# post_save.connect(at_ending_delete, sender=User)

@receiver(pre_init, sender=User)
def at_bignning_init(sender, *args, **kwargs):
    print('-----------------------------------')
    print('Pre Init Signals...')
    print('Sender', sender)
    print(f"args: {args}")
    print(f"Kwargs: {kwargs}")

# pre_save.connect(at_bignning_init, sender=User)

@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print('-----------------------------------')
    print('Post Init Signals...')
    print('Sender', sender)
    print(f"Kwargs: {kwargs}")
    print(f"args: {args}")

# post_save.connect(at_ending_init, sender=User)

@receiver(request_started)
def at_bignning_request(sender, environ, **kwargs):
    print('-----------------------------------')
    print('At Bignning Request...')
    print('Sender', sender)
    print('Environ', environ)
    print(f"Kwargs: {kwargs}")

# request_started.connect(at_bignning_request)

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print('-----------------------------------')
    print('At Ending Request...')
    print('Sender', sender)
    print(f"Kwargs: {kwargs}")

# request_finished.connect(at_ending_request)

@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print('-----------------------------------')
    print('At Request excetion...')
    print('Sender', sender)
    print('Request', request)
    print(f"Kwargs: {kwargs}")

# got_request_exception.connect(at_req_exception)

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('-----------------------------------')
    print('Before Install App...')
    print('Sender', sender)
    print('AppConfig', app_config)
    print('Verbosity', verbosity)
    print('Interactive', interactive)
    print('Using', using)
    print('Plan', plan)
    print('Apps', apps)
    print(f"Kwargs: {kwargs}")

# pre_migrate.connect(before_install_app)

@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('-----------------------------------')
    print('At End Migrate Flush...')
    print('Sender', sender)
    print('AppConfig', app_config)
    print('Verbosity', verbosity)
    print('Interactive', interactive)
    print('Using', using)
    print('Plan', plan)
    print('Apps', apps)
    print(f"Kwargs: {kwargs}")

# post_migrate.connect(at_end_migrate_flush)

@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print('-----------------------------------')
    print('Initial Connection to the DataBase...')
    print('Sender', sender)
    print('Connection', connection)
    print(f"Kwargs: {kwargs}")

# connection_created.connect(conn_db)