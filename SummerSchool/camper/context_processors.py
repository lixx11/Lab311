from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        'DEADLINE': settings.DEADLINE,
        'WEBSITE': settings.WEBSITE,
        'RELEASE': settings.RELEASE,
    }
