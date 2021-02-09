from django.urls import path, include

urlpatterns = [
    path('api/', include('main_app.rest_urls')),
    path('', include('main_app.utility_urls'))
]
