from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset
from django import forms
from django.forms.models import ModelForm, ModelMultipleChoiceField
from django.utils.translation import ugettext_lazy as _
from sapl.crispy_layout_mixin import to_row, SaplFormLayout
from sapl.parlamentares.models import Parlamentar

from cmj.sigad import models
from cmj.sigad.models import Classe, Documento


class UpLoadImportFileForm(forms.Form):
    import_file = forms.FileField(
        required=True,
        label=_('Arquivo formato ODF para Importanção')
    )

    def __init__(self, *args, **kwargs):
        super(UpLoadImportFileForm, self).__init__(*args, **kwargs)
        self.fields['import_file'].widget.attrs.update(
            {'multiple': 'multiple'})

error_messages = {
    'required': _('Este campo é obrigatório'),
    'invalid': _('Formato inválido.')
}


class ClasseForm(ModelForm):

    visibilidade = forms.ChoiceField(
        label=Classe._meta.get_field('visibilidade').verbose_name,
        choices=Documento.VISIBILIDADE_STATUS)
    perfil = forms.ChoiceField(
        label=Classe._meta.get_field('perfil').verbose_name,
        choices=models.PERFIL_CLASSE)
    descricao = forms.CharField(
        label=Classe._meta.get_field('descricao').verbose_name,
        widget=forms.Textarea,
        required=False)

    parent = forms.ModelChoiceField(
        queryset=Classe.objects.all(),
        widget=forms.HiddenInput(),
        required=False)

    class Meta:
        model = Classe
        fields = [
            'codigo',
            'titulo',
            'visibilidade',
            'perfil',
            'descricao',
            'parent',
            'template_doc_padrao',
            'template_classe',
            'parlamentar'
        ]

    def __init__(self, *args, **kwargs):

        row1 = to_row([
            ('codigo', 2),
            ('titulo', 6),
            ('parlamentar', 4),
        ])

        row2 = to_row([
            ('perfil', 3),
            ('visibilidade', 3),
            ('template_classe', 3),
            ('template_doc_padrao', 3),
        ])
        row3 = to_row([
            ('descricao', 12),
        ])

        self.helper = FormHelper()
        self.helper.layout = SaplFormLayout(
            Fieldset(_('Identificação Básica'),
                     row1, row2, row3))

        super(ClasseForm, self).__init__(*args, **kwargs)


class DocumentoForm(ModelForm):

    parlamentares = ModelMultipleChoiceField(
        queryset=Parlamentar.objects.all(), required=False,
        label=Parlamentar._meta.verbose_name_plural,
        widget=forms.SelectMultiple(attrs={'size': '10'})
    )

    class Meta:
        model = Documento
        fields = ['titulo',
                  'template_doc',
                  'descricao',
                  'visibilidade',
                  'parlamentares'
                  ]

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.layout = SaplFormLayout(
            to_row([
                ('titulo', 6), ('template_doc', 3), ('visibilidade', 3),
            ]),
            to_row([
                ('descricao', 8),
                ('parlamentares', 4)
            ]),
        )

        super(DocumentoForm, self).__init__(*args, **kwargs)

        self.fields['parlamentares'].choices = [
            ('0', '--------------')] + list(
            self.fields['parlamentares'].choices)