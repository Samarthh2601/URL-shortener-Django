from django import forms

class UrlForm(forms.Form):
    url = forms.CharField(label='URL')

    def check_url(self, url: str) -> bool:
        if url.startswith('http://') or url.startswith('https://'):
            return True
        return False