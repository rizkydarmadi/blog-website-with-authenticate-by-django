from django.forms import ModelForm

from .models import artikel

class artikelForm(ModelForm):
    """Form definition for artikel."""

    class Meta:
        """Meta definition for artikelform."""

        model = artikel
        fields = ('judul','isi','kategori')
