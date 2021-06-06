from django.urls import path, re_path

from .services.User.UserService import (
    #list
    UserProfile,
    Register,
    Login,
)

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    #list
    re_path(
        r'^user-id/(?P<id>\d+)/$',
        UserProfile.as_view()
    ),
    #register
    path(
        'register',
        Register.as_view(),
    ),
    #login
    path(
        'login',
        Login.as_view(),
    ),
]