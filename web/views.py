import json

from django.shortcuts import render
from django.http.response import HttpResponse

from web.models import Subscribe,Promoter,Feature,VideoBlog,Testimonial,MarketingFeature,Product,Blog


def index(request):
    promoters = Promoter.objects.all()
    features = Feature.objects.all() 
    videoblogs = VideoBlog.objects.all()
    testimonials = Testimonial.objects.all()
    marketingfeatures = MarketingFeature.objects.all()
    products = Product.objects.all()
    blogs = Blog.objects.all()

    context = {
        "promoters" : promoters,
        "features" : features,
        "videoblogs" : videoblogs,
        "testimonials" : testimonials,
        "marketingfeatures" : marketingfeatures,
        "products" : products,
        "blogs" : blogs
       
    }
    return render(request, "index.html",context = context)

def subscribe(request):
    email = request.POST.get("email")

    if not Subscribe.objects.filter(email=email).exists():

        Subscribe.objects.create(
            email = email
        )

        response_data = {
            "status" :"success",
            "message" : "You subscribed to our newsletter successfully",
            "title" : "Successfully Registered"
        }
    else:
        response_data = {
            "status" :"warning",
            "message" : "You are already a member. No need to register again",
            "title" : "You are already subscribed."
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")