"""
URL configuration for SchoolFees project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_admin),
    path('', views.login_admin),
    path('logout/', views.logout_admin),
    path('students/', views.student_list),
    path('students/add/', views.add_student),
    path('students/delete/<int:id>/', views.delete_student),
    path('students/update/<int:id>/', views.update_student),
    path('dashboard', views.dashboard),
    path('fee-categories/', views.fee_category_list),
    path('fee-categories/add/', views.add_fee_category),
    path('fee-categories/update/<int:id>/', views.update_fee_category),
    path('fee-categories/delete/<int:id>/', views.delete_fee_category),
    path('fees/assign/', views.assign_fees),
    path('fees/student/<int:id>/', views.payment_status),
    path('fees/update/<int:id>/', views.update_payment_status),

]
