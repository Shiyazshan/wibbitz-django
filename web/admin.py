from django.contrib import admin
from web.models import Subscribe,Promoter,Feature,VideoBlog,Testimonial,MarketingFeature,Product,Blog


admin.site.register(Subscribe)

class PromoterAdmin(admin.ModelAdmin):
    list_display = ["id", "image"]

admin.site.register(Promoter,PromoterAdmin) 

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id","image","icon","icon_background","title","description","testimonial_description","testimonial_author","author_designation","testimonial_logo"]

admin.site.register(Feature,FeatureAdmin)

class VideoBlogAdmin(admin.ModelAdmin):
    list_display = ["id", "image","title","logo"]

admin.site.register(VideoBlog,VideoBlogAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id","image","logo","description","name","designation","company_name"]

admin.site.register(Testimonial,TestimonialAdmin)

class MarketingFeatureAdmin(admin.ModelAdmin):
    list_display = ["id","image","title","description"]

admin.site.register(MarketingFeature,MarketingFeatureAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","logo","title","description","image"]

admin.site.register(Product,ProductAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display =["id","image","title","content_type"]

admin.site.register(Blog,BlogAdmin)