from django.urls import path


from products_app.views import \
    index, cart, checkout, cart_save, \
    delete, update, login,SignUp

urlpatterns = [path('', index, name='index'),
               path('cart/', cart, name='cart'),
               path('cart-save/', cart_save, name='cart_save'),
               path('checkout/', checkout, name='checkout'),
               path('delete/', delete, name='delete'),
               path('update/', update, name="update"),
               path('login/',login, name='login'),
               path('signup/', SignUp.as_view(), name='signup'),
]


