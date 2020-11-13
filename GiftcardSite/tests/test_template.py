from django.test import TestCase





from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'GiftcardSite/index.html'

    def get_context_data(self, **kwargs):
        kwargs['environment'] = 'Production'
        return super().get_context_data(**kwargs)
