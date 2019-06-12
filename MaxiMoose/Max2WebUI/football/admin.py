from django.contrib import admin

from .models import Team
from .models import Match

admin.site.register(Team)
admin.site.register(Match)