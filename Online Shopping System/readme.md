**Table of Contents**

- [System Requirements](#system-requirements)
- [Class diagram](#class-diagram)
- [Activity diagrams](#activity-diagrams)
- [Code](#code)

### System Requirements
- Users should be able to add new products to sell.
- Users should be able to search for products by their name or category.
- Users can search and view all the products, but they will have to become a registered member to buy a product.
- Users should be able to add/remove/modify product items in their shopping cart.
- Users can check out and buy items in the shopping cart.
- Users can rate and add a review for a product.
- The user should be able to specify a shipping address where their order will be delivered.
- Users can cancel an order if it has not shipped.
- Users should get notifications whenever there is a change in the order or shipping status.
- Users should be able to pay through credit cards or electronic bank transfer.
- Users should be able to track their shipment to see the current state of their order.

### Class diagram
------------
```mermaid
%%{init: { "theme": "neutral"} }%%

classDiagram
direction LR 
class ShoppingCart {
  items: list<ltem>
	getltems()
	addltem()
	removetem()	
}

class Item {
    quantity: int
	price: double
	updateQuantity()
}

class Order {
    orderNumber: string
	status: OrderStatus
	orderDate: date
	sendForShipment()
}

class OrderLog {
    creationDate: date
	status: OrderStatus
}

class ProductCategory {
    name: string
    description: string
}

class Product {
    name: string
	description: string
	price: double
	availableltemCount: int
	category: ProductCategory
	getAvailableCount()
}

class Shipment{
	shipmentDate: date
	estimatedArrival: date
	shipmentMethod: string
	addShipmentLog()
}

class Account{
  userName: string
  password: string
  status: AccountStatus
  name: string
  shippingAddress: Address
  email: string
  phone: string
  getShippingAddress()
  addProductReview()
  addProduct()
}

class Shipment{
	shipmentDate: date
	estimatedArrival: date
	shipmentMethod: string
	addShipmentLog()
}

class Member {
	placeOrder()
}

class Admin{
	blockUser()
	addNewProductCategory()
	modityProductCategory()
}

class Guest {
    registerAccount()
}

class Customer {
	getShoppingCart()
}

class ProductReview {
	rating: int
	review: string
	getRating()
}

Customer *-- Order
Customer *-- ShoppingCart
Order "1" --> "*" Item
ShoppingCart "1" --> "*" Item
Product "1" --> "*" Item
Order "1" --> "1..*" Shipment
Order "1" --> "1..*" OrderLog
Product --> ProductCategory : Belongs to
ProductReview --> Product : Abount
Member *-- Account
Admin *-- Account 
Customer --|> Member
Guest --|> Member


    
            

```
