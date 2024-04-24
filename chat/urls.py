# chat/urls.py
from django.urls import path
# from .views import ChatPageView
from .views import predict_product


urlpatterns = [
    # path("", ChatPageView.as_view(), name="chat"),
    path("", predict_product, name='predict_product'),

]