from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist

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

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)# consulta en función del producto y del carrito
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save() # save the change in db
    else:
        cart_item.delete()
    
    return redirect("cart")

def cart(request, total=0, quantity=0, cart_items=None):
    try: 
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
        for cart_item in cart_items: # know final price of all the cart
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100 # tax of 2%
        grand_total = total + tax
        
    except ObjectDoesNotExist:
        pass

    # what will send to the html template
    context = {
        "total": total,
        "quantity": quantity,
        "cart_items": cart_items,
        "tax": tax,
        "grand_total": grand_total,
    }

    return render(request, "store/cart.html", context)