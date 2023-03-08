#python shopping cart program

class Cart:
    def __init__(self):
        self.items={}
        self.price={'mobile': 10000, 'laptop': 60000, 'tablet': 45000}
        
    def add_item(self, product, quantity):
        self.items[product]=quantity
    
    def remove_item(self, product):
        del self.items[product]
        
    def update_item(self, product, quantity):
        self.items[product]= quantity
    
    def get_items(self):
        only_product=[]
        for item in self.items.keys():
            only_product.append(item)
        return only_product
    
    def total_price(self):
        total=0
        for item, quantity in self.items.items():
            total+=quantity*self.price[item]
        return total
    
obj=Cart()

obj.add_item('laptop', 1)
obj.add_item('mobile', 2)
obj.add_item('tablet',1)
print(obj.items)

obj.remove_item('mobile')
print(obj.items)

obj.update_item('laptop', 2)
print(obj.items)

print(obj.get_items())

print(obj.total_price())