from django.urls import path

from . import views

urlpatterns = [
    path(
        "toasts/",
        views.toasts,
        name="toasts",
    ),
    path(
        "cache/invalidate/",
        views.invalidate_cache,
        name="invalidate_cache",
    ),
]
