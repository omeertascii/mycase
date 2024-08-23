from django.utils.translation import gettext as _
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from discord.permissions import CallbackPermission
from rest_framework.status import HTTP_402_PAYMENT_REQUIRED
from discord.serializers import (
    AuthorizationUrlSerializer,
    DefaultExceptionSerializer,
)
from discord.models import Membership

class DiscordCallbackViewset(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, CallbackPermission]

    @extend_schema(request=None, responses={200: AuthorizationUrlSerializer, 400: DefaultExceptionSerializer})
    @action(detail=False, methods=["GET"], url_path=r"(?P<org_pk>.+)/get-url", url_name="get-url")
    def get_auth_url(self, request, *args, **kwargs):
        membership = Membership.objects.get(user=kwargs["organization"].owner)  # organization from permission class
        if not membership.can_create_channel():
            return DefaultExceptionSerializer.response(
                detail=_("The membership plan has reached its limits. Unable to add new channel."),
                status=HTTP_402_PAYMENT_REQUIRED,
            )