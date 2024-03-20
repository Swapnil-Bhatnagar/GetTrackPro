from django.urls import path
from . import views

urlpatterns = [
    # User Registration and Authentication
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/representative/', views.register_representative, name='register_representative'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.view_profile, name='view_profile'),

    # Service Requests
    path('create-service-request/', views.create_service_request, name='create_service_request'),
    path('user-service-requests/', views.view_user_service_requests, name='view_user_service_requests'),
    path('service-request/<int:request_id>/', views.view_service_request_details, name='view_service_request_details'),

    # Representative
    path('all-service-requests/', views.view_all_service_requests, name='view_all_service_requests'),
    path('update_service_request/<int:request_id>/', views.update_service_request, name='update_service_request'),
    path('update_resolved_at/<int:request_id>/', views.update_resolved_at, name='update_resolved_at'),
]