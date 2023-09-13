from django.urls import path

from account.views import (
    account_view,
    update_account_view,
)

app_name = "account"
urlpatterns = [
    path('<user_id>/',  account_view, name='view'),
    path('<user_id>/update',  update_account_view, name='update'),
]
