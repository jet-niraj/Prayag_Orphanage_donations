"""
URL configuration for dms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from . import views
from donation.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
     path('admin/', admin.site.urls),
     path('all_login/',views.all_login, name='all_login'), 
     path('index/',views.index, name='index'),
     path('donor_login/',views.donor_login, name='donor_login'),
     path('volunteer_login/',views.volunteer_login, name='volunteer_login'),
     path('admin_login/', views.admin_login, name='admin_login'),
     path('donor_reg/', views.donor_reg, name='donor_reg'),
     path('donor_home/', views.donor_home, name='donor_home'),
     path('admin_home/', views.admin_home, name='admin_home'),
     path('logout/', views.Logout, name='logout'),
     path('donate_now/', views.donate_now, name='donate_now'),
     path('donation_history/', views.donation_history, name='donation_history'),
     path('pending_donation/', views.pending_donation, name='pending_donation'),
     path('accepted_donation/', views.accepted_donation, name='accepted_donation'),
     path('view_donationdetail/<int:pid>', views.view_donationdetail, name='view_donationdetail'),
     path('edit_area/<int:pid>', views.edit_area, name='edit_area'),
     path('delete_area/<int:pid>', views.delete_area, name='delete_area'),
     path('add_area/', views.add_area, name='add_area'),
     path('manage_area/', views.manage_area, name='manage_area'),
     path('manage_donor/', views.manage_donor, name='manage_donor'),
     path('view_donordetail/<int:pid>', views.view_donordetail, name='view_donordetail'),
     path('delete_donor/<int:pid>', views.delete_donor, name='delete_donor'),
     path('volunteer_reg/',views.volunteer_reg, name='volunteer_reg'),
     path('volunteer_home/',views.volunteer_home, name='volunteer_home'),
     path('new_volunteer/',views.new_volunteer, name='new_volunteer'),
     path('accepted_volunteer/',views.accepted_volunteer, name='accepted_volunteer'),
     path('rejected_volunteer/',views.rejected_volunteer, name='rejected_volunteer'),
     path('all_volunteer/',views.all_volunteer, name='all_volunteer'),
     path('collection_req/',views.collection_req, name='collection_req'),
     path('view_volunteerdetail/<int:pid>', views.view_volunteerdetail, name='view_volunteerdetail'),
     path('delete_volunteer/<int:pid>', views.delete_volunteer, name='delete_volunteer'),
     path('accepted_donationdetail/<int:pid>', views.accepted_donationdetail, name='accepted_donationdetail'),
     path('donationcollection_detail/<int:pid>', views.donationcollection_detail, name='donationcollection_detail'),
     path('donationrec_volunteer/',views.donationrec_volunteer, name='donationrec_volunteer'),
     path('donationrec_detail/<int:pid>',views.donationrec_detail, name='donationrec_detail'),
     path('donationnotrec_volunteer/',views.donationnotrec_volunteer, name='donationnotrec_volunteer'),
     path('donationdelivered_volunteer/',views.donationdelivered_volunteer, name='donationdelivered_volunteer'),
     path('profile_volunteer/',views.profile_volunteer, name='profile_volunteer'),
     path('password_volunteer/',views.password_volunteer, name='password_volunteer'),



     



   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
