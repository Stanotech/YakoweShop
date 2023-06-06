import oscar.apps.dashboard.catalogue.apps as apps
from django.urls import include, path

class CatalogueDashboardConfig(apps.CatalogueDashboardConfig):
    name = 'apy.dashboard.catalogue'
    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('products/createmulti/', self.product_create_redirect_view.as_view(), name='catalogue-products-create'),
        ]
        return self.post_process_urls(urls)
    
    