from apps.newsletters.form import NewsLetterModelForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class NewsLetterViews(FormView):
    template_name = 'newsletter.html'
    form_class = NewsLetterModelForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)