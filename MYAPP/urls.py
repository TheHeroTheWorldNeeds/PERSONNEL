from django.conf.urls import url
from MYAPP import views
from django.urls import path

urlpatterns = [
    url(r'^api/accounts$', views.accounts_list),
    url(r'^api/accounts/(?P<pk>[0-9]+)$', views.accounts_detail),

    url(r'^api/departments$', views.departments_list),
    path('api/departments/<str:pk>', views.departments_detail),

    url(r'^api/positions$', views.positions_list),
    path('api/positions/<str:pk>', views.positions_detail),

    url(r'^api/salaries$', views.salaries_list),
    url(r'^api/salaries/(?P<pk>[0-9]+)$', views.salaries_detail),

    url(r'^api/staffs$', views.staffs_list),
    url(r'^api/staffs/(?P<pk>[0-9]+)$', views.staffs_detail),
]
