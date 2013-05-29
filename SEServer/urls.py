from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('cms.views',
    # Examples:
    url(r'^SEServer/login$', 'login', name='login'),
    url(r'^SEServer/register', 'register', name='register'),
    url(r'^SEServer/profile', 'profile', name='profile'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
