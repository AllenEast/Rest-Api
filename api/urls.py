from django.urls import path
#from .views import UserViewSet, PostViewSet
from .views import UserView, UserDetail, ClientView, ClientDetail, PostView, PostDetail
from rest_framework.routers import SimpleRouter

#router = SimpleRouter()
#router.register('users', UserViewSet, basename='users')
#router.register('', PostViewSet, basename='posts')

#urlpatterns = router.urls


urlpatterns = [
    path('post/', PostView.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),

    path('users/', UserView.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),



    path('clients/', ClientView.as_view()),
    path('client/<int:pk>/', ClientDetail.as_view()),
]
