from django.urls import path, include


app_name = 'app'

urlpatterns = [
    path('', include('app.auth.urls', namespace='auth')),
    path('rumah-sakit', include('app.rumah_sakit.urls', namespace='rumah_sakit')),
]
