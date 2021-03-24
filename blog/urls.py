
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from posts.views import PostList, IndexPage


router = SimpleRouter()
router.register('api/posts',PostList)

urlpatterns = [
    path('',IndexPage.as_view()),
    path('admin/', admin.site.urls),
    path('api/api-auth/',include('rest_framework.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/rest-auth/',include('rest_auth.urls')),

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)