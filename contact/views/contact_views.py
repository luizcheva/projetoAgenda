from django.shortcuts import get_object_or_404, render

from contact.models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by("-id")[:10]

    print(contacts.query)

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context,
    )


def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True,
    )

    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': contact_name,
    }

    return render(
        request,
        'contact/contact.html',
        context,
    )
