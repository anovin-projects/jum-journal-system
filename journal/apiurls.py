from .api import ManuscriptViewSet, AuthorViewSet, SectionsViewSet, VolumeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('manuscripts', ManuscriptViewSet, 'manuscripts')
router.register('authors', AuthorViewSet, 'Authors')
router.register('sections', SectionsViewSet, 'Sections')
router.register('volumes', VolumeViewSet, 'Volumes')


urlpatterns = router.urls
