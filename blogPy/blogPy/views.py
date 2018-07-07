from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseRedirect(reverse("test"))
    #     return super().get(request, *args, **kwargs)
