"""
URL configuration for {{ cookiecutter.project_name }} project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from allauth.socialaccount.providers.openid_connect.views import login, callback


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hijack/", include("hijack.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("pwa.urls")),
    # path("api/", include("rest_framework.urls")),
    path("api/", include("apps.api.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("auth/", include("allauth.urls")),  # allauth urls
    # path("auth/oidc/<str:provider_id>/login/", login, name="openid_connect_login"),
    # path(
    #     "auth/oidc/<str:provider_id>/login/callback/",
    #     callback,
    #     name="openid_connect_callback",
    # ),
    path("", include("apps.transactions.urls")),
    path("", include("apps.common.urls")),
    path("", include("apps.users.urls")),
    path("", include("apps.accounts.urls")),
    path("", include("apps.net_worth.urls")),
    path("", include("apps.monthly_overview.urls")),
    path("", include("apps.yearly_overview.urls")),
    path("", include("apps.currencies.urls")),
    path("", include("apps.rules.urls")),
    path("", include("apps.calendar_view.urls")),
    path("", include("apps.dca.urls")),
    path("", include("apps.mini_tools.urls")),
    path("", include("apps.import_app.urls")),
    path("", include("apps.export_app.urls")),
    path("", include("apps.insights.urls")),
]
