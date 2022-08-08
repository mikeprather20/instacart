from cgi import print_exception
from flask import Blueprint, redirect, render_template, request, url_for, flash

from flask_login import login_required, current_user

from app.models import User, Product, db, shop

shop = Blueprint('shop', __name__, template_folder='shoptemplates')

#1 Route for available product (shopfront)
@shop.route('/shop', methods = ["GET","POST"])
def shopfront():
    product = Product.query.all()
    return render_template('shop.html', product=product)


#3 Route to show all items added to cart and the total count
@shop.route('/cart', methods = ["GET","POST"])
@login_required
def showcart():
    user = User.query.get(current_user.id)
    cart = user.cart.all()
    total = len(cart)
    return render_template('cart.html', cart=cart, user=user, total = total)


#5 Route to add product to cart with @login_required
@shop.route('/add/<string:name>')
@login_required
def add2cart(name):
    product = Product.query.filter_by(name=name).first()
    current_user.cart.append(product)
    db.session.commit()
    flash('Added to Cart!', 'success')
    return redirect(url_for('shop.shopfront'))




#6 Route to remove single item from cart with @login_required
@shop.route('/remove/<string:name>')
@login_required
def removefromcart(name):
    product = Product.query.filter_by( name=name).first()
    current_user.cart.remove(product)
    db.session.commit()
    flash('Item removed.', 'success')
    return redirect(url_for('shop.showcart'))


#7 Route to remove all items from cart
@shop.route('/removeall')
@login_required
def removeall():
    product = Product.query.all()
    for p in product:
        if p in current_user.cart:
            current_user.cart.remove(p)
            db.session.commit()
    flash('All Items Removed!', 'success')
    return redirect(url_for('shop.showcart'))