from .models import Settings



def get_settings(request):
    data = Settings.objects.last()
    return {'settings_data':data}