from django.apps import AppConfig


class TmartCartAndFavoriteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tmart_Cart_and_Favorite'

    def ready(self):
        import tmart_Cart_and_Favorite.signals