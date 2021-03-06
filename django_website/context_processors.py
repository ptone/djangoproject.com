from django.conf import settings
from django.core.cache import cache

from django_website.docs.models import DocumentRelease

def recent_release(request):
    recent_release = cache.get('recent_release')
    if not recent_release:
        recent_release = DocumentRelease.objects.default().version
        cache.set(
            DocumentRelease.DEFAULT_CACHE_KEY,
            recent_release,
            settings.CACHE_MIDDLEWARE_SECONDS,
        )
    return {'RECENT_RELEASE': recent_release}
