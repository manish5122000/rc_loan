from customer.forms import Personal_Information_Form
from django.urls import path
from django.contrib.auth import views as auth_views
from customer import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Authentication 
    path('customer-registration/', views.CustomerRegistration, name='customerregistration'),

    #personal Information
    path('personal-information/',views.Personal_Info.as_view(), name='personalinformation'),

    #Dashboard
    path('Dashboard/', views.dashboard, name='dashboard'),

    #Document
    path('documents-upload/', views.Docs, name='docs'),

    #apply Loan
    path('apply-for-loan/', views.loan_apply, name='loan'),

    #admin page
    path('admin-page/',views.Personal_Info.as_view(), name='adminpg'),

    #get user detail by admin
    path('user-detail/<int:id>', views.get_user_detail, name='userdetail'),

    #loan status
    path('loan-status/', views.Admin_view, name='l_status'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)