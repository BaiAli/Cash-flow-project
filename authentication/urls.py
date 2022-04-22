from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('edit', views.edit, name='edit'),
    path('profile', views.profile, name='profile'),
    path('features', views.features, name='features'),
    path('contacts', views.contacts, name='contacts'),
    path('why', views.why, name='why_cash_flow'),
    path('addbankincomes',views.addNewBankCard, name = 'bankcard'),
    path('addbankcardname', views.addBankName,  name='bankname'),
    re_path(r'^accounts/$', views.AccountListView.as_view(), name='account'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)