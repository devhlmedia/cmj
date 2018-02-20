
from braces.views import FormMessagesMixin
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from cmj.core.models import Notificacao
from cmj.ouvidoria.forms import DenunciaForm
from cmj.ouvidoria.models import Solicitacao


class DenunciaAnonimaFormView(FormMessagesMixin, CreateView):
    form_valid_message, form_invalid_message = (
        _('Sua denúncia anônima foi encaminha.'),
        _('Houve um erro no envio de sua mensagem.'))
    model = Solicitacao
    form_class = DenunciaForm
    template_name = 'ouvidoria/denuncia_form.html'

    def get_context_data(self, **kwargs):

        context = CreateView.get_context_data(self, **kwargs)
        context['title'] = _('Denúncia Anônima')
        return context

    def get_success_url(self):
        return reverse('cmj.ouvidoria:denuncia_form')

    def get_initial(self):
        initial = CreateView.get_initial(self)
        initial.update({'logged_user':
                        bool(self.request.user.is_authenticated)})
        return initial

    def get(self, request, *args, **kwargs):
        response = CreateView.get(self, request, *args, **kwargs)
        if self.request.user.is_authenticated:
            logout(request)

        return response


class SolicitacaoDetailView(PermissionRequiredMixin, DetailView):
    model = Solicitacao
    template_name = 'ouvidoria/solicitacao_detail.html'
    permission_required = 'ouvidoria.detail_solicitacao'

    def has_permission(self):
        self.object = self.get_object()

        if self.object.owner == self.request.user:
            return True
        elif PermissionRequiredMixin.has_permission(self):
            return self.object.areatrabalho.operadores.filter(
                pk=self.request.user.pk).exists()
        else:
            return False

    def get(self, request, *args, **kwargs):

        if not self.object.owner:
            self.template_name = 'ouvidoria/denuncia_anonima_detail.html'
        return DetailView.get(self, request, *args, **kwargs)