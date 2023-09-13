from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver



@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('-------------------------------------')
    print('Logged In Signals Run Intro....')
    ip = request.META.get('REMOTE_ADDER')
    print('Cleint IP', ip)
    request.session['ip'] = ip
    