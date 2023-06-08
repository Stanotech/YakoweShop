import oscar.apps.dashboard.catalogue.apps as apps
from django.urls import include, path

class CatalogueDashboardConfig(apps.CatalogueDashboardConfig):
    name = 'apy.dashboard.catalogue'
    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path(
            'products/create/<slug:product_class_slug>/<str:multi_image>/',
            self.product_createupdate_view.as_view(),
            name='catalogue-product-create'),
        ]
        return self.post_process_urls(urls)
    
class ProductCreateUpdateView(apps.ProductCreateUpdateView):
    