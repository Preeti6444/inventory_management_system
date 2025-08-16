from flask_restful import Resource, Api
from models import Product, Supplier

def init_api(app):
    api = Api(app)

    class ProductAPI(Resource):
        def get(self):
            products = Product.query.all()
            return [{"id": p.id, "name": p.name, "stock": p.stock, "price": p.price} for p in products]

    class SupplierAPI(Resource):
        def get(self):
            suppliers = Supplier.query.all()
            return [{"id": s.id, "name": s.name, "email": s.email} for s in suppliers]

    class LowStockAPI(Resource):
        def get(self):
            products = Product.query.filter(Product.stock < 5).all()
            return [{"id": p.id, "name": p.name, "stock": p.stock} for p in products]

    api.add_resource(ProductAPI, '/api/products')
    api.add_resource(SupplierAPI, '/api/suppliers')
    api.add_resource(LowStockAPI, '/api/low_stock')