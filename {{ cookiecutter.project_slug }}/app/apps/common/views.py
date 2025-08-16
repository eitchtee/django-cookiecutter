from dateutil.relativedelta import relativedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.utils.translation import gettext_lazy as _

from cachalot.api import invalidate

from apps.common.decorators.htmx import only_htmx
from apps.transactions.models import Transaction
from apps.common.decorators.user import htmx_login_required


@only_htmx
@htmx_login_required
@require_http_methods(["GET"])
def toasts(request):
    return render(request, "common/fragments/toasts.html")


@only_htmx
@login_required
@require_http_methods(["GET"])
def invalidate_cache(request):
    invalidate()

    messages.success(request, _("Cache cleared successfully"))

    return HttpResponse(
        status=204,
        headers={
            "HX-Trigger": "updated",
        },
    )
