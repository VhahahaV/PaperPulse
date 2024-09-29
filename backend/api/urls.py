from django.urls import path, include

urlpatterns = [
    path('user/', include('api.user.urls')),
    path('paper/', include('api.paper.urls')),
    path('analysis/', include('api.analysis.urls')),
    path('scheduler/', include('api.scheduler.urls')),
    path('notification/', include('api.notification.urls')),
    path('websocket/', include('api.websocket.urls')),
]