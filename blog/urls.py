from django.urls import path

from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('blog', BlogViewSet, basename='blog')
router.register('blog-category', BlogCategoryViewSet, basename='blog-category')
router.register('blog-comment', BlogCommentViewSet, basename='blog=comment')
router.register('blog-tag', BlogTagViewSet, basename='blog-tag')

urlpatterns = router.urls
