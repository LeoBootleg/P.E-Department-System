from django.urls import path

from . import views


urlpatterns = [
    path('', views.loginuser, name="login"),
    path('registration', views.register, name="registration"),
    path('student', views.student, name="student"),
    path('admin_home', views.adminHome, name="admin_home"),
    path('admin_borrow', views.adminBorrow, name="admin_borrow"),
    path('admin_return', views.adminReturn, name="admin_return"),
    path('admin_schedule', views.adminSched, name="admin_schedule"),
    path('admin_preorder', views.adminPreorder, name="admin_preorder"),
    path('admin_block', views.adminBlock, name="admin_block"),
    path('admin_inventory', views.adminInventory, name="admin_inventory"),
    path('admin_sales', views.adminSales, name="admin_sales"),
    path('sendmail_sheesh', views.sendmail_sheesh, name='sendmail_sheesh')

    
]
