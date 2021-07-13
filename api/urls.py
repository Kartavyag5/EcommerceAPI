from django.urls import path
from .views import *

urlpatterns = [
    path('',ListCategory.as_view(), name='API-Home'),
    path('categories/', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    
    path('products/', ListProduct.as_view(), name='products'),
    path('products/<int:pk>', DetailProduct.as_view(), name='singleproduct'),

    path('users', ListUser.as_view(), name='users'),
    path('users/<int:pk>', DetailUser.as_view(), name='singleuser'),
    path('users/registration',RegistrationAPIView.as_view(),name='registration'),

#------new Cart---------------------
    path('carts/', CartAPIView.as_view(), name='carts'),    
    path('carts/<int:pk>/', CartDetailsView.as_view(), name='cart_Details'),    

#-------------orders---------------------
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderDetailsView.as_view(), name='orderDetails'),
    path('billing_profile',BillingProfileAPIView.as_view(), name='billing_profiles'),
    
    #path('test/',test,name='test'),

#----------------Razorpay urls------------------------------
 # Payment APIs
    path('payment/', payment, name = 'payment'),
   
]
