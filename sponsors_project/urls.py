from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import DetailView, ListView

from sponsors.models import Sponsor

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^sponsors/', include('sponsors.urls')),
)

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