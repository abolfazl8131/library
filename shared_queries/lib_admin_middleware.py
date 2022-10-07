from management.models import LibraryAdmin

def find_library_admin(id):

    try:
        obj = LibraryAdmin.objects.get(id=id)
        return obj
    except Exception as e:
        return e
