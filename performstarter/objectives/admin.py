from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Skill)
admin.site.register(Team)
admin.site.register(Tool)
admin.site.register(TeamSkill)
admin.site.register(TeamTool)
admin.site.register(Objective)
admin.site.register(DefinitionOfGood)
admin.site.register(ObjectiveSkill)
admin.site.register(ObjectiveTool)
