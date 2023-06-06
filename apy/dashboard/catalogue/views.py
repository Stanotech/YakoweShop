import oscar.apps.dashboard.catalogue.apps as apps
from django.urls import include, path

class ProductCreateRedirectView(apps.ProductCreateRedirectView):
    permanent = False
    productclass_form_class = ProductClassSelectForm

    def get_product_create_url(self, product_class):
        """ Allow site to provide custom URL """
        return reverse('dashboard:catalogue-product-create',
                       kwargs={'product_class_slug': product_class.slug})

    def get_invalid_product_class_url(self):
        messages.error(self.request, _("Please choose a product type"))
        return reverse('dashboard:catalogue-product-list')

    def get_redirect_url(self, **kwargs):
        form = self.productclass_form_class(self.request.GET)
        if form.is_valid():
            product_class = form.cleaned_data['product_class']
            return self.get_product_create_url(product_class)

        else:
            return self.get_invalid_product_class_url()
    
