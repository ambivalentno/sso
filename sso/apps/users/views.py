from django.contrib.auth.models import User
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView, ListView
)

from .models import *

from pure_pagination.mixins import PaginationMixin
#from enhanced_cbv.views import ListFilteredView
#from django_genericfilters.views import FilteredListView


class UserDetailView(DetailView):
    """User detail view"""
    model = User
    slug_field = "slug"
    template_name = "user-detail.html"


class UserUpdateView(UpdateView):
    """User update view"""
    model = User
    slug_field = "slug"
    template_name = "user-update.html"


class UserCreateView(CreateView):
    """User create view"""
    model = User
    template_name = "user-create.html"
