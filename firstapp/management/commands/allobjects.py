from django.core.management.base import NoArgsCommand, CommandError
import sys

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        from django.db.models import Model
    
        for model in Model.__subclasses__():
            print model.__name__, model.objects.count()
            print >> sys.stderr,  "error: %s %d" % (model.__name__, model.objects.count())
            #print model.objects.count()
