from rest_framework import routers

# blog app called viewsets are
from .viewsets import BlogViewSet, BlogCategoryViewSet, BlogCommentViewSet, BlogTagViewSet

router = routers.SimpleRouter()
router.register('blog', BlogViewSet, basename='blog')
router.register('blog-category', BlogCategoryViewSet, basename='blog-category')
router.register('blog-comment', BlogCommentViewSet, basename='blog=comment')
router.register('blog-tag', BlogTagViewSet, basename='blog-tag')

urlpatterns = router.urls
