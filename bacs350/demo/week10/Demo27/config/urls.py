from django.urls import path, include


urlpatterns = [
    
    path('', include('accounts.urls')), 
    path('', include('blog.urls')),
    path('workshop/', include('workshop.urls') ),
    
]
