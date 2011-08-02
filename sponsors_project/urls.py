from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template

from sponsors.models import Sponsor

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r"impact/", direct_to_template, {"template": "impact/index.html",}, name="impact"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('sponsors.views',
    url(regex=r'^$',
        view=ListView.as_view(
            queryset=Sponsor.objects.order_by('-pub_date'),
            context_object_name='latest_sponsor_list',
            template_name='sponsors/sponsor_list.html'),
        name='sponsor_list',
    ),
    url(regex=r'^(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(
            model=Sponsor,
            template_name='sponsors/sponsor_detail.html'),
        name='sponsor_detail',
    ),
)