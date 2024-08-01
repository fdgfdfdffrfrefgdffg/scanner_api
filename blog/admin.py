from django.contrib import admin

# Register your models here.
from chiqish.models import Chiqish
admin.site.register(Chiqish)

from ega.models import Ega
admin.site.register(Ega)

from kirishlar.models import Kirish
admin.site.register(Kirish)

from maktab.models import Maktab
admin.site.register(Maktab)

from maktabadmin.models import Admin
admin.site.register(Admin)

from oquvchi.models import Oquvchi
admin.site.register(Oquvchi)    

from telegroups.models import Telegroup
admin.site.register(Telegroup)