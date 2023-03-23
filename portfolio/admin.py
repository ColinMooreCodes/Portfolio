from django.contrib import admin

from .models import User, BlogPost, BlogTag, GalleryPost, GalleryTag, HeroSection, ShopLink, SocialMedia

# Register your models here.

admin.site.register(User)
admin.site.register(BlogPost)
admin.site.register(BlogTag)
admin.site.register(GalleryPost)
admin.site.register(GalleryTag)
admin.site.register(HeroSection)
admin.site.register(ShopLink)
admin.site.register(SocialMedia)
