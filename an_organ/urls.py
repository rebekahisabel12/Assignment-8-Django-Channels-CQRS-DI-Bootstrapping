from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import AnalyticalMethodViewSet, InstrumentViewSet


from . import views

router = routers.DefaultRouter()
router.register(r"analytical-methods", AnalyticalMethodViewSet)
router.register(r"instruments", InstrumentViewSet)

app_name = "an_organ"

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]

urlpatterns += router.urls

#  self.list_url = reverse("barkyapi:bookmark-list")
#         self.detail_url = reverse(
#             "barkyapi:bookmark-detail", kwargs={"pk": self.bookmark.id}
#         )

# router = routers.DefaultRouter()
# router.register(r"bookmarks", views.BookmarkViewSet)
