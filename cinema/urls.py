from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    CinemaHallViewSet,
    ActorDetail,
    MovieViewSet,
)

cinema_hall_list = CinemaHallViewSet.as_view({"get": "list", "post": "create"})
cinema_hall_detail = CinemaHallViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema_hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall-detail"
    ),
]

app_name = "cinema"
