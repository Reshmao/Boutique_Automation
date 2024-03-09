"""boutique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .import views

urlpatterns = [
    path('',views.index),
    path('login',views.logins),
    path('user_register',views.user_register),
    path('acceptcustomer_username/<id>',views.acceptcustomer_username),
    path('forgot_password',views.forgot_password),
    path('set_password/<id>/<eid>/<emails>',views.set_password),



 # =====================ADMIN==============================================================================================
    path('adminhome',views.adminhome),
    path('admin_view_user',views.admin_view_user),
    path('admin_manage_category',views.admin_manage_category),
    path('delete_category/<id>',views.delete_category),
    path('update_category/<id>',views.update_category),


    path('admin_manage_sizechart/<id>',views.admin_manage_sizechart),
    path('delete_sizechart/<did>/<id>',views.delete_sizechart),
    path('size_active/<did>/<id>',views.size_active),
    path('size_deactive/<did>/<id>',views.size_deactive),

    path('admin_view_bk',views.admin_view_bk),
    path('admin_view_booking_details/<id>',views.admin_view_booking_details),
    path('admin_view_payment/<id>',views.admin_view_payment),
    path('admin_dispatch/<id>',views.admin_dispatch),    


    path('admin_customized_design',views.admin_customized_design), 
    path('admin_add_amount/<id>',views.admin_add_amount), 
    path('admin_view_cpayment/<id>',views.admin_view_cpayment),
    path('admin_cdispatch/<id>',views.admin_cdispatch),    

    path('admin_accept/<id>',views.admin_accept),    
    path('admin_reject/<id>',views.admin_reject),    


    path('admin_manage_design',views.admin_manage_design),
    path('delete_design/<id>',views.delete_design),
    path('update_design/<id>',views.update_design),

    path('admin_manage_purchase',views.admin_manage_purchase),
    path('delete_purchase/<id>',views.delete_purchase),
    path('update_purchase/<id>',views.update_purchase),

    path('admin_view_msg',views.admin_view_msg),
    path('admin_view_feedback',views.admin_view_feedback),

    path('admin_send_reply/<id>',views.admin_send_reply),

    
 # =====================user==============================================================================================
    path('user_view_profile',views.user_view_profile),
    path('user_home',views.user_home),
    path('user_send_msg',views.user_send_msg),
    path('user_view_design',views.user_view_design),

    path('customer_add_cart/<id>/<design>/<amount>/<image>/<dqty>',views.customer_add_cart),

    path('user_add_cdesgin',views.user_add_cdesgin),



    path('user_view_booking',views.user_view_booking),
    path('user_view_booking_details/<id>',views.user_view_booking_details),
    path('customer_make_payment/<id>/<total>',views.customer_make_payment),
    path('user_payment_completes/<id>',views.user_payment_completes),
    path('rpay',views.rpay,name='rpay'),





    path('customer_make_cpayment/<id>/<total>',views.customer_make_cpayment),
    path('user_payment_complete/<id>',views.user_payment_complete),



    path('user_add_feedback',views.user_add_feedback),


    path('user_view_reference/<id>',views.user_view_reference),



    path('customer_add_wlist/<id>',views.customer_add_wlist),
    path('customer_view_wlist',views.customer_view_wlist),
    path('customer_remove_wlist/<id>',views.customer_remove_wlist),

    path('user_view_cancel/<id>',views.user_view_cancel),




]
