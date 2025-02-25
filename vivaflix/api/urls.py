from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, WatchlistViewSet, RatingViewSet, signup, login_view
from django.urls import path
from .views import RegisterView, MyTokenObtainPairView
from .views import upload_image
from . import views



router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'watchlist', WatchlistViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('upload/', upload_image, name='upload_image'),
]