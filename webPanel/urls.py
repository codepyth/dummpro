"""webPanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.views import LogoutView
from main import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.utils.html import format_html
from main.models import Registration
pending_count = Registration.objects.filter(status='PENDING').count()
rejected_count = Registration.objects.filter(status='REJECTED').count()
approved_count = Registration.objects.filter(status='APPROVED').count()
applied_for_edit = Registration.objects.filter(applied_for_edit=True).count()
members_with_dependents = Registration.objects.filter(living_with_dependents=True).count()
members_whom_visa_will_expire_in_30_days = Registration.objects.filter(visa_gonna_expire_in_30_days=True).count()
members_whom_passport_will_expire_in_30_days = Registration.objects.filter(passport_gonna_expire_in_30_days=True).count()
members_whom_visa_already_expired = Registration.objects.filter(visa_expired=True).count()
members_whom_passport_already_expired = Registration.objects.filter(passport_expiry=True).count()


admin.site.site_header = "PKWR Administration"
admin.site.site_title = "PKWR Administration"
admin.site.index_title = format_html('''
    <div class="row">
        <div class="col-md-4">
            <div class="card text-white bg-warning">
                <div class="card-body">
                    <h5 class="card-title">Pending Members</h5>
                    <p class="card-text">{}</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-white bg-success">
                <div class="card-body">
                    <h5 class="card-title">Approved Members</h5>
                    <p class="card-text">{}</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-white bg-danger">
                <div class="card-body">
                    <h5 class="card-title">Rejected Members</h5>
                    <p class="card-text">{}</p>
                </div>
            </div>
        </div>
    </div>

    <div class="row mt-3">
        <div class="col-md-4">
            <div class="card text-white bg-info">
                <div class="card-body">
                    <h5 class="card-title">Applied for Edit</h5>
                    <p class="card-text">{}</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-white bg-primary">
                <div class="card-body">
                    <h5 class="card-title">Members with Dependents</h5>
                    <p class="card-text">{}</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-white bg-secondary">
                <div class="card-body">
                    <h5 class="card-title">Visa Expires in 30 Days</h5>
                    <p class="card-text">{}</p>
                </div>
            </div>
        </div>
    </div>

    <div class="row mt-3">
        <div class="col-md-4">
            <div class="card text-white bg-dark">
                <div class="card-body">
                    <h5 class="card-title">Passport Expires in 30 Days</h5>
                    <p class="card-text">{}</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-white bg-secondary">
                <div class="card-body">
                    <h5 class="card-title">Visa Already Expired</h5>
                    <p class="card-text">{}</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-white bg-dark">
                <div class="card-body">
                    <h5 class="card-title">Passport Already Expired</h5>
                    <p class="card-text">{}</p>
                </div>
            </div>
        </div>
    </div>
''', pending_count, approved_count, rejected_count, applied_for_edit, members_with_dependents,
    members_whom_visa_will_expire_in_30_days, members_whom_passport_will_expire_in_30_days,
    members_whom_visa_already_expired, members_whom_passport_already_expired)

from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginView.as_view(), name='public'),
    path('start/',views.check_view,name='start'),
    path('login/',views.signin, name='login'),
    path('signup/',views.signup, name='signup'),
    path('update_data/',views.update_data, name='update_data'),
    path('step-1/',views.save_registration),
    path('step-2/',views.step2,name='step-2'),
    path('step-3/',views.step3,name='step-3'),
    path('step-4/',views.step4,name='step-4'),
    path('step-5/',views.add_dependent,name='step-5'),
    path('status/',views.status,name='status'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
