from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.seller_list),
    path('seller/', views.seller_list, name = 'seller_list'),
    path('seller/<int:id>', views.seller_detail, name = 'seller_detail'),
    path('seller/new', views.seller_create, name = 'seller_create'),
    path('seller/<int:id>/edit', views.seller_update, name = 'seller_update'),
    path('seller/<int:id>/delete', views.seller_delete, name = 'seller_delete'),

    path('house/', views.house_list, name = 'house_list'),
    path('house/<int:id>', views.house_detail, name = 'house_detail'),
    path('house/new', views.house_create, name = 'house_create'),
    path('house/<int:id>/edit', views.house_update, name = 'house_edit'),
    path('house/<int:id>/delete', views.house_delete, name = 'house_delete'),
    path('upload/', views.upload_pic, name = 'upload_pic'),

    path('buyer/', views.buyer_list, name = 'buyer_list'),
    path('buyer/<int:id>', views.buyer_detail, name = 'buyer_detail'),
    path('buyer/new', views.buyer_create, name = 'buyer_create'),
    path('buyer/<int:id>/edit', views.buyer_update, name = 'buyer_edit'),
    path('buyer/<int:id>/delete', views.buyer_delete, name = 'buyer_delete'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path,include
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('camping.urls')),
#     path('search/', include('search.urls')),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)