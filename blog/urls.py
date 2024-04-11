from django.urls import path
from .views import index_view, blog_view, blog_single_view, about_view, contact_view

urlpatterns = [
    path('', index_view),
    path('blog/', blog_view),
    path('blog/<int:pk>/', blog_single_view),
    path('about/', about_view),
    path('contact/', contact_view)
]
