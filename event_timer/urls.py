from django.urls import path

from .views import index_view, update_view, create_view, delete_view, timer_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('create', create_view, name='create_view'),
    path('<int:event_pk>/update', update_view, name='update_view'),
    path('<int:event_pk>/delete', delete_view, name='delete_view'),
    path('<int:event_pk>', timer_view, name='timer_view'),
]
