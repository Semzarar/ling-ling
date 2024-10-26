from flask import Flask, render_template
app = Flask(__name__)

dish_templates = {
    'home': 'index.html',
    'contact': 'contact.html',
    'hot': 'hot.html',
    'cold': 'cold.html',
    'drinks': 'drinks.html',
    'dessert': 'dessert.html',
    'spec1': 'spec1.html',
    'spec2': 'spec2.html',
    'breakfast': 'breakfast.html',
    'pasta' : 'pasta.html',
    'chicken_curry': 'chicken_curry.html',
    'soup': 'soup.html',
    'potatoes': 'potatoes.html',
    'salad': 'salad.html',
    'sushi': 'sushi.html',
    'burrito': 'burrito.html',
    'sandwich': 'sandwich.html',
    'smoothie': 'smoothie.html',
    'milkshake': 'milkshake.html',
    'tea': 'tea.html',
    'juice': 'juice.html',
    'cupcakes': 'cupcakes.html',
    'brownies': 'brownies.html',
    'cookies': 'cookies.html',
    'fruit_tart': 'fruit_tart.html',
    'eggs': 'eggs.html',
    'waffles': 'waffles.html',
    'pancakes': 'pancakes.html',
    'porridge': 'porridge.html',
    'login': 'login.html'
}

# <page>
@app.route('/<page>')
def render_page(page):
    if page in dish_templates:
        return render_template(dish_templates[page])
    else:
        return 'Page not found!'


if __name__ == '__main__':
    app.run(debug=True)