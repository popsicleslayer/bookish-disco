"""
URL mappins for Recipe App
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
# Auto-generating endpoints for methods that are created

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]