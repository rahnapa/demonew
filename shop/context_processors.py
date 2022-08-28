from . models import Categery
def menu_links(request):
    links=Categery.objects.all()
    return dict(links=links)