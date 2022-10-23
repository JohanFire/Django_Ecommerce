from django.shortcuts import redirect, render

from .models import Cart, CartItem
from store.models import Product

# Create your views here.

# private function = _before_function
def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()

    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        # cart_id= actual session of user in browser
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try: 
        # cartitem is the info of the product that user will buy
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1 # increase quantity if you select same product multiple times
        cart_item.save()
    except CartItem.DoesNotExist: # if it's first time addind the product to the cart
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
        
    return redirect("cart")

def cart(request):
    return render(request, "store/cart.html")