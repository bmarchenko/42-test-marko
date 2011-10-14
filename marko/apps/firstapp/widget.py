from django import forms

class CalendarWidget(forms.DateInput):
    class Media:
        css = {
            'all': ('/media/css/jquery.ui.theme.css', 'css/jquery.ui.datepicker.css')
        }
        js = ('/media/js/jquery-1.5.1.js', '/media/js/jquery.form.js',
        '/media/js/jquery-ui-1.8.13.custom.min.js', '/media/js/calendar.js')
