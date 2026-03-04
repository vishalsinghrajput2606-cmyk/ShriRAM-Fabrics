from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    shop_name = "SHRIRAM FABRICS"
    # Bulk Supply Details
    bulk_info = {
        'capacity': '100 to 10000+ Units',
        'supply_type': 'Direct Factory to Client',
        'delivery': 'All Over India Delivery Available',
        'target': 'Schools, Colleges, Factories & Corporates'
    }
    
    return render_template('index.html', shop=shop_name, bulk=bulk_info)

if __name__ == '__main__':
    app.run(debug=True)