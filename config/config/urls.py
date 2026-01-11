from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookmarks.views import BookmarkViewSet

router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet, basename='bookmark')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
