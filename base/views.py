from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe

stripe.api_key = "sk_test_51HFYxlA4CqyyLqmjEjgR9B7Qp6dA0yFN1eMejjRzOVgoxlRxUhiDAOeStD7bmMDAtXKDHXGQw9mZc0dV1tiRyFKg001mQh1LG4"


def index(request):
    return render(request, 'base/index.html')


def charge(request):
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        print('Data:', request.POST)
        customer = stripe.Customer.create(
            # using two types of getting form data from field
            email=request.POST['email'],
            name=request.POST.get('nickname'),
            source=request.POST.get('stripeToken')  # Source that going to be charged actually the credit card
            # stripeToken was the value that returned on post credit card check in console
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description='Donations'
        )
    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'base/success.html', {'amount': amount})
