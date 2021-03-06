from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'personalblog'
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.ContactMe,name='contact'),
    path("innovations/",views.inovate,name='innovations'),
    path("programming/",views.programming,name='programming'),
    path('inspiration/',views.inspirations,name='inspiration'),
    path('trending-post/<str:pk>/',views.PostDetail,name='trending-post'),
    path('posts-Details/<str:pk>',views.PostOnly,name='post-Details')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)