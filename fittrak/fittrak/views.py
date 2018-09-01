from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request, template_name="index.html"):
    """
    Renders the index page which is the fallback for all routes.

    This allows the client-side app to take over and serves as a thin wrapper
    injecting the required context.
    """

    return render(
        request, template_name=template_name, context={"DEBUG": settings.DEBUG}
    )
