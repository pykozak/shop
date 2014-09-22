from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import api_views

urlpatterns = patterns('',
    url(
        regex=r'^products/(?P<category_id>\w+)/$',
        view=api_views.ProductAPIView.as_view(),
        name='product_list'
    ),
)

urlpatterns = format_suffix_patterns(urlpatterns)