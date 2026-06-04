from django.db import models

PRODUCT_CHOICES = [
    ('wiremesh', 'Crimped Wiremesh Screen'),
    ('perforated', 'Punching Perforated Plate'),
    ('both', 'Both Products'),
    ('other', 'Other / Not Sure'),
]

class Enquiry(models.Model):
    name         = models.CharField(max_length=150, verbose_name="Full Name")
    company      = models.CharField(max_length=200, blank=True, verbose_name="Company Name")
    phone        = models.CharField(max_length=20, verbose_name="Phone / WhatsApp")
    email        = models.EmailField(verbose_name="Email Address")
    product      = models.CharField(max_length=20, choices=PRODUCT_CHOICES, verbose_name="Product Required")
    message      = models.TextField(verbose_name="Message / Specifications")
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read      = models.BooleanField(default=False, verbose_name="Read")

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} — {self.get_product_display()} ({self.submitted_at.strftime('%d %b %Y')})"



class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    order_no      = models.PositiveIntegerField()
    order_date    = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=200)
    location      = models.CharField(max_length=200, blank=True)
    rate          = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_nos     = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_weight  = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_price   = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    price_per_nos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    line_items    = models.JSONField(default=list)
    notes         = models.TextField(blank=True)
    status        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-order_no']

    def __str__(self):
        return f"#{self.order_no} — {self.customer_name}"   