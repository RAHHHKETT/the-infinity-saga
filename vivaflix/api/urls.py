from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, WatchlistViewSet, RatingViewSet, signup, login_view, upload_video, VideoListView, RegisterView, MyTokenObtainPairView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'watchlist', WatchlistViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('upload/', upload_video, name='upload_video'),
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('videos/', VideoListView.as_view(), name='video_list'),
]
