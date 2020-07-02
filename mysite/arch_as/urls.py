from django.urls import path

from . import views

app_name = 'arch_as'
urlpatterns = [
        path('', views.index, name='index'),
        path('as/<int:as_id>/', views.as_detail, name='as_detail'),
        path('as/<int:as_id>/add_int', views.add_int, name="add_int"),
        path('interaction/<int:int_id>/remove', views.remove_int, name="remove_int"),
        path('interaction/<int:int_id>/edit', views.edit_int, name="edit_int"),
        path('upload_json/', views.upload_json, name='upload_json'),
        path('archas_base/', views.arachas_base, name='arachas_base'),
        path('archas_as_view/', views.as_view, name='as_view'),
        path('archas_category_view/', views.category_view, name='category_view'),
]

