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
