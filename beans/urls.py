from django.urls import path


from beans.views import (
    BeanListView,
    BeanDetailView,
    BeanCreateView,
)

urlpatterns = [
    path("list/", BeanListView.as_view(), name="list_beans"),
    path("<int:pk>/", BeanDetailView.as_view(), name="show_bean"),
    path("create/", BeanCreateView.as_view(), name="create_bean"),
]
