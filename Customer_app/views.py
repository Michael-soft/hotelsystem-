



from django. shortcuts import render


def Customer(request): 
    return render(request,"Customer/index.html")

def Contact(request):
    return render(request,"Customer/Contact.html")