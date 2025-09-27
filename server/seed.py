from app import app, db, Customer, Item, Review

with app.app_context():
    # Clear existing data
    Review.query.delete()
    Customer.query.delete()
    Item.query.delete()
    db.session.commit()

    # Create Customers
    customer1 = Customer(name="Tal Yuri")
    customer2 = Customer(name="Mia Chen")
    customer3 = Customer(name="Alex Kim")

    # Create Items
    item1 = Item(name="Laptop Backpack", price=49.99)
    item2 = Item(name="Insulated Coffee Mug", price=9.99)
    item3 = Item(name="Wireless Mouse", price=25.50)

    # Add all to session
    db.session.add_all([customer1, customer2, customer3, item1, item2, item3])
    db.session.commit()

    # Create Reviews
    review1 = Review(comment="Great backpack!", customer=customer1, item=item1)
    review2 = Review(comment="Keeps coffee hot", customer=customer1, item=item2)
    review3 = Review(comment="Very smooth mouse", customer=customer2, item=item3)
    review4 = Review(comment="Not durable", customer=customer3, item=item1)

    # Add reviews to session
    db.session.add_all([review1, review2, review3, review4])
    db.session.commit()

    print("Database seeded successfully!")
