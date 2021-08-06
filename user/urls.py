from django.urls import path, re_path

from .services.User.UserService import (
    #list
    UserProfile,
    Register,
    Login,
    FindUsername,
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
    # find user by username with api gateway
    path(
        'find-user',
        FindUsername.as_view(),
    ),
]