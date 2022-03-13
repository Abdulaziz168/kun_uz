from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path("", views.project_news_index, name="project_news_index"),
                  path("<int:pk>/", views.project_news_detail, name="project_news_detail"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
