from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Index, name='index'),
    path('blog_detail/<int:pk>' ,views.Blog_detail, name='blog_details'),
    path('save_bookmark/<int:pk>', views.save_bookmark, name='save_bookamark'),
    path('collections',views.collection, name='collection'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('remove_bookmark/<int:pk>/', views.remove_bookmark, name='remove_bookmark'),
    path('logout/', views.Logout, name='logout'),
    path('userblog',views.Userblog, name='userblog'),
    path('comments',views.Comments, name='comments'),

]


# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    