from django.urls import path
from django.views.generic import TemplateView

from . import views
from archas.views import *

from django.conf import settings
from django.conf.urls.static import static

app_name = 'archas'
urlpatterns = [
        path('', AutomatedSystemListView.as_view(), name='index'),
        path('asl/', AutomatedSystemListView.as_view(), name='asl'),
        path('as/<slug:slug>', AutomatedSystemDetailView.as_view(), name='as_detail'),
        path('as/<slug:slug>/update', AutomatedSystemUpdate.as_view(), name='as_update'),
        path('as/<slug:id>/ta/update', TargetArchitectureUpdate.as_view(), name='as_ta_update'),
        path('as/<int:automated_system_id>/intlist/update', InteractionsListUpdate.as_view(), name='int_list_update'),
        path('int/<slug:interaction_id>/update', InteractionUpdate.as_view(), name='interaction_update'),
        path('int/<int:automated_system_id>/create', InteractionCreate.as_view(), name='interaction_create'),
        path('int/<slug:interaction_id>/remove', views.interaction_remove, name='interaction_remove'),
        path('confluence/', views.confluence, name='confluence'),



        path('as/<int:as_id>/add_int', views.add_int, name="add_int"),
        # path('interaction/<int:int_id>/remove', views.remove_int, name="remove_int"),
        path('interaction/<int:int_id>/edit', views.edit_int, name="edit_int"),
        path('upload_json/', views.upload_json, name='upload_json'),
        path('archas_base/', views.arachas_base, name='arachas_base'),
        path('archas_as_view/', views.as_view, name='as_view'),
        path('archas_category_view/', views.category_view, name='category_view'),
        path('test_class_view/', AboutView.as_view(template_name="archas/archas_as_view.html")),
        path('test_class_view/', AboutView.as_view(template_name="archas/archas_as_view.html")),
        path('test_listclass_view/', BookListView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

