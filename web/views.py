import json

from django.shortcuts import render
from django.http.response import HttpResponse

from web.models import Subscribe,Promoter,Feature,VideoBlog,Testimonial,MarketingFeature,Product,Blog,Contact
from web.forms import ContactForm


def index(request):
    promoters = Promoter.objects.all()
    features = Feature.objects.all() 
    videoblogs = VideoBlog.objects.all()
    testimonials = Testimonial.objects.all()
    marketingfeatures = MarketingFeature.objects.all()
    products = Product.objects.all()
    blogs = Blog.objects.all()

    form = ContactForm()

    context = {
        "promoters" : promoters,
        "features" : features,
        "videoblogs" : videoblogs,
        "testimonials" : testimonials,
        "marketingfeatures" : marketingfeatures,
        "products" : products,
        "blogs" : blogs,
        "form" : form
       
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


def contact(request):
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    company = request.POST.get("company")
    company_size = request.POST.get("company_size")
    industry = request.POST.get("industry")
    job_role = request.POST.get("job_role")
    country = request.POST.get("country")
    user_agreement = request.POST.get("user_agreement")
    if not user_agreement:
        user_agreement = False
    elif user_agreement == "on":
        user_agreement = True

    if not Contact.objects.filter(email=email).exists():
        Contact.objects.create(
            email = email,
            first_name = first_name,
            last_name = last_name,
            company = company,
            company_size = company_size,
            industry = industry,
            job_role = job_role,
            country = country,
            user_agreement = user_agreement

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