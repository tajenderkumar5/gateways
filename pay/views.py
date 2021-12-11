from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import stripe
import razorpay
from django.conf import settings
from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY  

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
auth=("rzp_test_qJYq5tt1a08hAk", "PWm5gGdgVtDFJPxaVYvEnjsY"))
        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
    
    return render(request, 'index.html')

@csrf_exempt
def success(request):
    return render(request, "sucess.html")
