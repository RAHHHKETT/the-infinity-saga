from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, WatchlistViewSet, RatingViewSet, signup, LoginView, upload_video, VideoListView, RegisterView, MyTokenObtainPairView, CollectionViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'watchlist', WatchlistViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('upload/', upload_video, name='upload_video'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('videos/', VideoListView.as_view(), name='video_list'),
]
