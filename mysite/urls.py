"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from jobs.views import my_jobs,result

from personal.views import (
	home_screen_view,
    first_page_view,
)

from scholarship_blog.views import scholarship_blog_view

from account.views import (
    employee_registration_view,
    company_registration_view,
    logout_view,
    login_view,
    employee_account_view,
    company_account_view,
	must_authenticate_view,
    register_option_view,
    employee_redirect_view,
    company_redirect_view,
)

urlpatterns = [
    path('',first_page_view,name="first_page"),
    path('jobs/', home_screen_view, name="home"),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', 'blog')),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
	path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('must_authenticate_as_employee/', employee_redirect_view, name="employee_redirect"),
    path('must_authenticate_as_company/', company_redirect_view, name="company_redirect"),

    path('register/employee', employee_registration_view, name="register_employee"),
    path('register/company', company_registration_view, name="register_company"),

    path('register/company_update', company_account_view, name="update_company_account"),
    path('register/employee_update', employee_account_view, name="update_employee_account"),

    path('register_option/',register_option_view,name="register_option"),
    
    path('home/',my_jobs,name="jobs"),
    path('home/results/',result,name="job_results"),

    path('scholarship_data/',scholarship_blog_view,name='scholarship_blog'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
