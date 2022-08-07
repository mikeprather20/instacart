from flask import Blueprint, redirect, render_template, request, url_for, flash

from flask_login import login_required, current_user

from app.models import User, Product, shop, db

shop = Blueprint('shop', __name__, template_folder='shoptemplates')

