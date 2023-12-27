from .models import Settings
from django.core.cache import cache



def get_settings(request):

    # check data in cache 
    try:
        settings_data = cache.get('settings_data')
        print('new cache')
    except Exception:
        print('new data')
        settings_data = Settings.objects.last()
        cache.set('settings_data',settings_data,60*60*24*30)
    
    return {'settings_data':settings_data}