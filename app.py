from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json

app = Flask(__name__)
app.secret_key = 'popcorn-secret-key-2024'

PRODUCTS = [
    {
        "id": 1,
        "slug": "siracha-lime",
        "name": "Siracha Lime",
        "price": 2.99,
        "color": "#C63B2F",
        "tag_color": "red",
        "description": "Introducing our mouthwatering Sriracha Lime Popcorn, a delightful blend of zesty flavours that will take your snacking experience to new heights! Made with the finest French corn, this bold flavour combo packs a punch.",
        "long_description": "Our Sriracha Lime is the perfect marriage of fiery heat and citrus zing. Each kernel is coated in our signature sriracha glaze before being dusted with real lime zest, creating a flavour explosion that keeps you coming back for more. Born in France, loved worldwide.",
        "stars": 5,
        "review_count": 124,
        "nutrition": [
            {"label": "Energy", "value": "66kcal", "percent": 3},
            {"label": "Fat", "value": "3.0g", "percent": 4},
            {"label": "Sugars", "value": "0.2g", "percent": 1},
            {"label": "Salt", "value": "0.01g", "percent": 1},
        ],
        "tags": ["spicy", "zesty", "bestseller"],
        "weight": "80g"
    },
    {
        "id": 2,
        "slug": "caramel-salt",
        "name": "Caramel Salt",
        "price": 2.99,
        "color": "#C4742A",
        "tag_color": "orange",
        "description": "The timeless classic reinvented. Our Caramel Salt Popcorn delivers the perfect balance between rich, buttery caramel sweetness and a satisfying savoury finish. Irresistibly good.",
        "long_description": "We take pride in our slow-cooked caramel process, which gives each kernel an even, glossy coat of golden caramel. A touch of Guérande sea salt at the finish creates that addictive sweet-salty balance that makes this our most beloved flavour.",
        "stars": 5,
        "review_count": 211,
        "nutrition": [
            {"label": "Energy", "value": "72kcal", "percent": 4},
            {"label": "Fat", "value": "2.8g", "percent": 4},
            {"label": "Sugars", "value": "4.1g", "percent": 5},
            {"label": "Salt", "value": "0.03g", "percent": 1},
        ],
        "tags": ["sweet", "classic", "fan-favourite"],
        "weight": "80g"
    },
    {
        "id": 3,
        "slug": "truffle-parmesan",
        "name": "Truffle Parmesan",
        "price": 2.99,
        "color": "#1B3A6B",
        "tag_color": "blue",
        "description": "Luxurious and indulgent. Our Truffle Parmesan Popcorn elevates the humble snack into something truly extraordinary. Real truffle oil and aged parmesan come together beautifully.",
        "long_description": "Sourced from the finest Italian truffles and aged Parmigiano-Reggiano, this premium flavour was designed for those who want more from their snack. Each bag delivers a sophisticated umami experience that pairs wonderfully with a glass of wine.",
        "stars": 4,
        "review_count": 87,
        "nutrition": [
            {"label": "Energy", "value": "74kcal", "percent": 4},
            {"label": "Fat", "value": "3.4g", "percent": 5},
            {"label": "Sugars", "value": "0.1g", "percent": 1},
            {"label": "Salt", "value": "0.04g", "percent": 1},
        ],
        "tags": ["luxury", "savoury", "premium"],
        "weight": "80g"
    },
    {
        "id": 4,
        "slug": "sweet-chilli",
        "name": "Sweet Chilli",
        "price": 2.99,
        "color": "#8B2020",
        "tag_color": "red",
        "description": "A crowd-pleasing classic with a French twist. Sweet chilli sauce meets perfectly popped corn for a snack that's both familiar and exciting.",
        "long_description": "Our Sweet Chilli is made using a blend of ripe red peppers and a hint of garlic, giving it that signature tangy-sweet heat. It's the perfect snack for sharing — though you probably won't want to.",
        "stars": 4,
        "review_count": 63,
        "nutrition": [
            {"label": "Energy", "value": "68kcal", "percent": 3},
            {"label": "Fat", "value": "2.9g", "percent": 4},
            {"label": "Sugars", "value": "1.2g", "percent": 1},
            {"label": "Salt", "value": "0.02g", "percent": 1},
        ],
        "tags": ["spicy", "sweet", "sharing"],
        "weight": "80g"
    },
]

def get_cart():
    return session.get('cart', {})

def get_cart_count():
    cart = get_cart()
    return sum(item['qty'] for item in cart.values())

@app.context_processor
def inject_cart_count():
    return {'cart_count': get_cart_count()}

@app.route('/')
def index():
    featured = PRODUCTS[:3]
    return render_template('index.html', products=featured)

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS)

@app.route('/product/<slug>')
def product_detail(slug):
    product = next((p for p in PRODUCTS if p['slug'] == slug), None)
    if not product:
        return redirect(url_for('products'))
    related = [p for p in PRODUCTS if p['slug'] != slug][:3]
    return render_template('product_detail.html', product=product, related=related)

@app.route('/our-story')
def our_story():
    return render_template('our_story.html')

@app.route('/sustainability')
def sustainability():
    return render_template('sustainability.html')

@app.route('/cart')
def cart():
    cart_data = get_cart()
    items = []
    total = 0
    for slug, item in cart_data.items():
        product = next((p for p in PRODUCTS if p['slug'] == slug), None)
        if product:
            subtotal = product['price'] * item['qty']
            items.append({'product': product, 'qty': item['qty'], 'subtotal': subtotal})
            total += subtotal
    return render_template('cart.html', items=items, total=total)

@app.route('/cart/add', methods=['POST'])
def cart_add():
    slug = request.form.get('slug')
    qty = int(request.form.get('qty', 1))
    cart = get_cart()
    if slug in cart:
        cart[slug]['qty'] += qty
    else:
        cart[slug] = {'qty': qty}
    session['cart'] = cart
    return redirect(request.referrer or url_for('cart'))

@app.route('/cart/update', methods=['POST'])
def cart_update():
    slug = request.form.get('slug')
    qty = int(request.form.get('qty', 1))
    cart = get_cart()
    if qty <= 0:
        cart.pop(slug, None)
    else:
        cart[slug] = {'qty': qty}
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart/remove', methods=['POST'])
def cart_remove():
    slug = request.form.get('slug')
    cart = get_cart()
    cart.pop(slug, None)
    session['cart'] = cart
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
