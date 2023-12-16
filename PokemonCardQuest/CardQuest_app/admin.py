from django.contrib import admin
from .models import PokemonCard, Trainer, Collection
# Register your models here.
admin.site.register(PokemonCard)
admin.site.register(Trainer)
admin.site.register(Collection)


class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "hp", "card_type", "attack", "description", "weakness", "card_number", "release_date", "evolution_stage", "abilities", "created_at", "updated_at")
    search_fields = ("name",)

class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "email", "birthdate", "created_at", "updated_at", )
    search_fields = ("name",)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ("trainer", "card", "collection_date", "created_at", "updated_at", )
    search_fields = ("name",)