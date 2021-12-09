from django.conf.urls import url
from .views import AdvertisementAPIView, AdvertisementDetails

urlpatterns = [
    url(r'^api/advertisement$', AdvertisementAPIView.as_view()),
    url(r'^api/advertisement/(?P<indent>[0-9]+)$', AdvertisementDetails.as_view()),
]
