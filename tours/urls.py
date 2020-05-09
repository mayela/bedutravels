from rest_framework import routers
from graphene_django.views import GraphQLView

from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import TourViewSet, UserViewSet, ZonaViewSet, index
from .schema import schema

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tours', TourViewSet)
router.register(r'zonas', ZonaViewSet)

urlpatterns = [
    path('', index, name='index'),
    path("login/", auth_views.LoginView.as_view(template_name="tours/login.html"), name="login"),
    path('api/', include(router.urls)),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]
