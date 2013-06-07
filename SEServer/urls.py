from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('cms.views',
    # Examples:
    url(r'^login$', 'login', name='login'),
    url(r'^register$', 'register', name='register'),
    url(r'^profile$', 'profile', name='profile'),
    url(r'^add_tags$', 'add_tags'),
    url(r'^$', 'home', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('cms.user_views',

    url(r'^user/profile$', 'profile', name='user_profile'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('cms.activity_views',

    url(r'^activity/all$', 'all', name='user_profile'),
    url(r'^activity/add_tags$', 'add_tags'),
    url(r'^activity/create$', 'create'),
)