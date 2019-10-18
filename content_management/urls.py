from django.urls import path
from .views import UserPanel, CreatePostView


urlpatterns = [
    path('panel/', UserPanel.as_view(), name="panel"),
    path('user_management/', CreatePostView.as_view(), name="create"),
]
