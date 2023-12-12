from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import Home

urlpatterns = [
    path('home/', Home.as_view()),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('products/', include('api.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
