from django.db.models import base
from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
#from .views import PostList, PostDetail, UserList, UserDetail
from .views import UserViewSet, PostViewSet

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('', PostList.as_view()),
#     path('<int:pk>', PostDetail.as_view()),
# ]


# using routers
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
