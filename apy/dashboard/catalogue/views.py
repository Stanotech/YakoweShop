import oscar.apps.dashboard.catalogue.views as views
from oscar.apps.dashboard.catalogue.views import *

class ProductCreateRedirectView(views.ProductCreateRedirectView):
    
    permanent = False
    productclass_form_class = ProductClassSelectForm

    def get_product_create_url(self, product_class, multi_image=None):
        """ Allow site to provide custom URL """
        kwargs = {'product_class_slug': product_class.slug}
        if multi_image is not None:
            kwargs['multi_image'] = multi_image
        return reverse('dashboard:catalogue-product-create', kwargs=kwargs)

    def get_invalid_product_class_url(self):
        messages.error(self.request, ("Please choose a product type"))
        return reverse('dashboard:catalogue-product-list')

    def get_redirect_url(self, **kwargs):
        form = self.productclass_form_class(self.request.POST) #creating instance of form class with arguments from request
        if form.is_valid():
            product_class = form.cleaned_data['product_class'] #cleaned_data return dictionary from form
            multi_image = self.request.POST.get('multi_image')
            print(self.request.POST)
            print(multi_image)
            return self.get_product_create_url(product_class, multi_image)

        else:
            return self.get_invalid_product_class_url()
        
class ProductCreateUpdateView(views.ProductCreateUpdateView):

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['product_class'] = self.product_class
        ctx['parent'] = self.parent
        ctx['title'] = self.get_page_title()
        ctx['multi_image'] = self.kwargs.get('multi_image')

        for ctx_name, formset_class in self.formsets.items():
            if ctx_name not in ctx:
                ctx[ctx_name] = formset_class(self.product_class,
                                              self.request.user,
                                              instance=self.object)
                
        return ctx