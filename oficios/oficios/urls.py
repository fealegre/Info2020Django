from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.conf import settings

#URL PRINCIPAL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Home'),
    path('Usuarios/',include('apps.Usuarios.urls')),
    path('Trabajadores/',include('apps.Trabajadores.urls')),
    path('Stalkers/',include('apps.Stalkers.urls')),
    path('Comentarios/',include('apps.Comentarios.urls')),
    path('Zonas/',include('apps.Zonas.urls')),
    path('Calificaciones/',include('apps.Calificaciones.urls')),
    path('Login', auth.LoginView.as_view(template_name='Usuarios/Login.html'), name='login'),
    path('Logout', auth.LogoutView.as_view(template_name='Usuarios/Logout.html'), name='logout'),

    path('password', auth.PasswordChangeView.as_view(template_name='Usuarios/password.html'), name='password_change'),
    path('passwordDone', auth.PasswordChangeDoneView.as_view(template_name='Usuarios/passwordDone.html'), name='password_change_done'),
    path('reset_password/',
        auth.PasswordResetView.as_view(template_name="Usuarios/password_reset.html"), 
        name="reset_password"),

    path('reset_password_sent/',
        auth.PasswordResetDoneView.as_view(template_name="Usuarios/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth.PasswordResetConfirmView.as_view(template_name="Usuarios/password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/',
        auth.PasswordResetCompleteView.as_view(template_name="Usuarios/password_reset_done.html"), 
        name="password_reset_complete"),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
