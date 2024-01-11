from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # auth
    path("accounts/", include("django.contrib.auth.urls")),
    # local apps
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("accounts/", include("users.urls")),
    path("budget/", include("budget.urls")),
    path("dashboard/", include("dashboard.urls")),
]
