from flask import Blueprint, redirect, render_template, request, url_for, flash

from flask_login import login_required, current_user

from app.models import User, Product, db, shop

shop = Blueprint('shop', __name__, template_folder='shoptemplates')

#1 Route for available product (shopfront)
@shop.route('/shop', methods = ["GET"])
def shopfront():
    pass

#2 Route for single product with product info (clicked item in shopfront)
@shop.route('/item', methods = ["GET"])
def productinfo():
    pass

#3 Route to add product to cart with @login_required
@shop.route('/add', methods = ["POST"])
@login_required
def add2cart():
    pass

#4 Route to show all items added to cart and the total price
@shop.route('/cart', methods = ["GET"])
@login_required
def showcart():
    pass

#5 Route to remove all items from cart
@shop.route('/remove', methods = ["GET","POST"])
@login_required
def removeall():
    pass
