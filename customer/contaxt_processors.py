from .models import Person

def my_proser(request):
    last_person = Person.objects.last()
    if last_person:
        name = last_person.name

    else:
        name = 'no person  found'  
    return {
        'contack_us': '+8801937796586',
        'last_person':name

    }
    