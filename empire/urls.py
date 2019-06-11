from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url

from rest_framework import routers
from .views import UserLoginViewSet , ShopDetailsViewSet , FeedBackDetailsViewSet , CustomView

router = routers.DefaultRouter()
router.register(r'showDetails', ShopDetailsViewSet)
router.register(r'loginUser', UserLoginViewSet)
router.register(r'feedback', FeedBackDetailsViewSet)

urlpatterns = [
     path('', views.index, name='index'),
     url(r'customview', CustomView.as_view()),
     path('cool',views.questions_view),
] 

urlpatterns += router.urls

# if settings.DEBUG:
urlpatterns += static('/empire/static/empire', document_root=settings.STATIC_ROOT) 
# else :
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 