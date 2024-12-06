from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import Contact

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        Contact.objects.create(name=name, phone=phone, email=email, address=address)
        return redirect('home')
    return render (request, 'add_contact.html')


def edit_contact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.address = request.POST['address']
        contact.save()
        return redirect('home')
    return render(request, 'edit_contact.html', {'contact': contact})

def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('home')

