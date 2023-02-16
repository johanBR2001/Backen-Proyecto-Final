from django.urls import path


from. import views

urlpatterns = [
    path("loginCliente", views.loginCliente),
    path("loginRestaurante", views.loginRestaurante),
    path("obtenerRestaurantes", views.obtenerRestaurantes),
    path("Realizado", views.Realizado)
    ]
