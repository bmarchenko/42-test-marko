from django import forms


class CalendarWidget(forms.DateInput):
    class Media:
        css = {
            'all': ('css/jquery.ui.theme.css', 'css/jquery.ui.datepicker.css')
        }
        js = ('js/jquery-1.5.1.js', 'js/jquery.form.js',
                'js/jquery-ui-1.8.13.custom.min.js', 'js/widget-calendar.js')
