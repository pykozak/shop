from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import api_views

urlpatterns = patterns('',
    url(
        regex=r'^products/(?P<category_id>\w+)/$',
        view=api_views.ProductAPIView.as_view(),
        name='product_list'
    ),
    url(
        regex=r'^product/(?P<id>\w+)/$',
        view=api_views.ProductDetailAPIView.as_view(),
        name='product_detail'
    ),
    url(
        regex=r'^categories/$',
        view=api_views.CategoryAPIView.as_view(),
        name='category_list'
    ),
)

urlpatterns = format_suffix_patterns(urlpatterns)