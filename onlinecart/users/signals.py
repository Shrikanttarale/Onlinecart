from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
from .models import UserLogs
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from products.models import Wishlist


@receiver(user_logged_in)
def user_logged_in_signal(sender,request,user,**kwargs):
    print("User is logged in")
    userlogs_object, created=UserLogs.objects.get_or_create(
        userlogs_user=user,
        userlogs_action='user_logged_in',
    )

@receiver(user_logged_out)
def user_logged_out_signal(sender,request,user,**kwargs):
    print("User is logged out")
    userlogs_object, created=UserLogs.objects.get_or_create(
        userlogs_user=user,
        userlogs_action='user_logged_out',
    )

#Signal to add audit when whishlist item got added
@receiver(post_save,sender=Wishlist)
def save_user_logs(sender,**kwargs):
    instance=kwargs["instance"] #<Wishlist:potatoes>
    print("sender",sender.wishlist_user)
    userlogs_object,created=UserLogs.objects.get_or_create(
        userlogs_user=instance.wishlist_user,
        userlogs_action='wishlist_item_added'
    )


#Signal to add audit when whishlist item got deleted
@receiver(post_delete,sender=Wishlist)
def save_user_logs(sender,**kwargs):
    instance=kwargs["instance"] #<Wishlist:potatoes>
    print("sender",sender.wishlist_user)
    userlogs_object,created=UserLogs.objects.get_or_create(
        userlogs_user=instance.wishlist_user,
        userlogs_action='wishlist_item_deleted'
    )