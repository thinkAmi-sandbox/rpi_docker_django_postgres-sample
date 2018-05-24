from django.urls import path
from myapp.views import FooView

urlpatterns = [
    path('<int:pk>/', FooView.as_view()),
]