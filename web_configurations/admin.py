from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import IndexConfiguration, GeneralConfiguration, LaEmpresaConfiguration, CacheConfiguration,CasosExitoConfiguration

admin.site.register(GeneralConfiguration, SingletonModelAdmin)
admin.site.register(IndexConfiguration, SingletonModelAdmin)
admin.site.register(LaEmpresaConfiguration, SingletonModelAdmin)
admin.site.register(CacheConfiguration, SingletonModelAdmin)
admin.site.register(CasosExitoConfiguration, SingletonModelAdmin)
