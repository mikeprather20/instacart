from flask import Blueprint, redirect, render_template, request, url_for, flash

from flask_login import login_required, current_user

from app.models import User, Product, db, shop

shop = Blueprint('shop', __name__, template_folder='shoptemplates')

#1 Route for available product (shopfront)
@shop.route('/shop', methods = ["GET","POST"])
def shopfront():
    product = Product.query.all()
    return render_template('shop.html', product=product)



#2 Route for single product with product info (clicked item in shopfront)
@shop.route('/item', methods = ["GET", "POST"])
def productinfo():
    pass

#5 Route to show all items added to cart and the total price
@shop.route('/cart', methods = ["GET","POST"])
@login_required
def showcart():
    user = User.query.get(current_user.id)
    cart = user.cart.all()
    return render_template('cart.html', cart=cart)


#3 Route to add product to cart with @login_required
@shop.route('/add/<string:name>')
@login_required
def add2cart(name):
    product = Product.query.filter_by(name=name).first()
    current_user.cart.append(product)
    db.session.commit()
    flash('Added to Cart!', 'success')
    return redirect(url_for('shop.shopfront'))




#4 Route to remove single item from cart with @login_required
@shop.route('/remove/<string:name>')
@login_required
def removefromcart(name):
    product = Product.query.filter_by(name=name).first()
    current_user.cart.remove(product)
    db.session.commit()
    flash('Item removed.', 'success')
    return redirect(url_for('shop.showcart'))


#6 Route to remove all items from cart
@shop.route('/removeall')
@login_required
def removeall():
    pass