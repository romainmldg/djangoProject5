from django.contrib import admin

# Register your models here.
from .models import Utilisateur
admin.site.register(Utilisateur)

from .models import Frigo
admin.site.register(Frigo)

from .models import Photo_plat
admin.site.register(Photo_plat)

from .models import Recette
admin.site.register(Recette)

from .models import Avis
admin.site.register(Avis)

from .models import Service
admin.site.register(Service)

from .models import Ingredients
admin.site.register(Ingredients)





