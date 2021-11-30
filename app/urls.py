from django.urls import path, include


app_name = 'app'

urlpatterns = [
    path('', include('app.auth.urls', namespace='auth')),
]
