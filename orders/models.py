from django.db import models
from products.models import Product

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=50, verbose_name="اسم العائلة")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    address = models.CharField(max_length=250, verbose_name="العنوان")
    city = models.CharField(max_length=100, verbose_name="المدينة")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    paid = models.BooleanField(default=False, verbose_name="تم الدفع")

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'الطلب رقم {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity