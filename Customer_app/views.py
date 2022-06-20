



from django. shortcuts import render


def Customer(request): 
    return render(request,"Customer_app/index.html")

def Contact(request):
    return render(request,"Customer_app/Contact.html")