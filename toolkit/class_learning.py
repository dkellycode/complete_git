class ProductID:
    def __init__(self, id, acct, desc):
        self.id = id
        self.acct = acct
        self.desc = desc

product_ids = [
    ProductID(9421903673244, 227010725, 'd3 RST - Rigid Strapping Tape'),
    ProductID(9421903673220, 225110726, 'd3 K6.0 Kinesiology Tape'),
    ProductID(9421905741828, 225510725, 'd3 X6.0 Waterproof Kinesiology Tape'),
    ProductID(9421903673206, 223010725, 'd3 Cohesive Bandage'),
    ProductID(9421034850477, 224110725, 'd3 Light EAB Spandex Bandage'),
    ProductID(9421905131841, 221010725, 'd3 Athletic Tape'),
    ProductID(9421034854208, 284110725, 'd3 Instant ice Pack x4')
]

for product in product_ids:
    print(f"ID: {product.id}, Account: {product.acct}, Description: {product.desc}")


# Access the first product
first_product = product_ids[0]
print(f"First product: ID: {first_product.id}, Account: {first_product.acct}, Description: {first_product.desc}")

# Access the third product
third_product = product_ids[2]
print(f"Third product: ID: {third_product.id}, Account: {third_product.acct}, Description: {third_product.desc}")

class Cars:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is running.")

italian = Cars('Ferrari', 'testarossa', 1987, 'red')
german = Cars('BMW', 318, 1987, 'blue')
french = Cars('Peugeot', 205, 1987, 'green')


italian.start_engine()
