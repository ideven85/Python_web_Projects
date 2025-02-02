from django.db import models

# Create your models here.
CATEGORY_CHOICES = (("EC", "Electronics"), ("CG", "Clothing"), ("AC", "Accessories"))


class Category(models.Model):
    category = models.CharField(max_length=120)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("category",)


class Item(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    brand = models.CharField(max_length=120, default="Laptop")
    category = models.ManyToManyField(Category, related_name="Item_Category")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)

    def discount(self):
        pass

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("price", "brand")


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images", name="item_image")
    thumbnail = models.ImageField(upload_to="thumbnails", null=True)


class ItemTag(models.Model):
    items = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="item_subcategory"
    )
    sub_category = models.CharField(max_length=120, default="Laptop")

    name = models.CharField(max_length=120, unique=True)
    slug = models.CharField(max_length=120)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    pass
