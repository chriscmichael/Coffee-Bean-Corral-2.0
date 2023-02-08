from django.urls import path

from cups.views import (
    CupListView,
    CupDetailView,
    CupCreateView,
)

urlpatterns = [
    path("list/", CupListView.as_view(), name="list_cups"),
    path("<int:pk>/", CupDetailView.as_view(), name="show_cup"),
    path("create/", CupCreateView.as_view(), name="create_cup"),
]
