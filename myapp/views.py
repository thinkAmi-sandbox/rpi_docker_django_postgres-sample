from django.shortcuts import render
from django.views.generic import DetailView
from myapp.models import Foo


class FooView(DetailView):
    model = Foo