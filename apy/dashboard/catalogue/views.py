import oscar.apps.dashboard.catalogue.views as views
from oscar.apps.dashboard.catalogue.views import *

class ProductCreateRedirectView(views.ProductCreateRedirectView):
    permanent = False
    productclass_form_class = ProductClassSelectForm
    
    def get_product_create_url(self, product_class):
        """ Allow site to provide custom URL """
        kwargs = {'product_class_slug': product_class.slug}
        return reverse('dashboard:catalogue-product-create', kwargs=kwargs)

    def get_invalid_product_class_url(self):
        messages.error(self.request, _("Please choose a product type"))
        return reverse('dashboard:catalogue-product-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        multi_image = self.request.GET.get('multi_image')
        context['multi_image'] = multi_image
        return context

    def get_redirect_url(self, **kwargs):
        form = self.productclass_form_class(self.request.GET)  #creating instance of form class with arguments from request
        if form.is_valid():
            product_class = form.cleaned_data['product_class']  #cleaned_data return dictionary from form
            return self.get_product_create_url(product_class)

        else:
            return self.get_invalid_product_class_url()