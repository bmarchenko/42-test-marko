from django.forms.widgets import DateInput


class JSDataPickerWidget(DateInput):
    def __init__(self, attrs={'class': 'datepicker'}, format=None):
        super(JSDataPickerWidget, self).__init__(attrs)

    class Media:
        css = {'all': ('http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.3/themes/smoothness/jquery-ui.css',)}
        js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js',
              'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.13/jquery-ui.min.js',
              'basicapp/js/datepicker.js')
