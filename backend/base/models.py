from django.db import models

# Create your models here.


class Menu(models.Model):
    father = models.ForeignKey("base.Menu", blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, verbose_name="Name")
    url = models.CharField(max_length=300, verbose_name="URL", help_text="Set model and app or your custom URL, for example: app.model or extra/content/")
    admin = models.BooleanField(verbose_name="Administrative", default=False)
    support = models.BooleanField(verbose_name="Support", default=False)
    icon = models.CharField(max_length=300, verbose_name="Icon class name", help_text="Set the name for the desired icon based on FlatIcon, for example 'fi-rr-angle-small-right'", default="fi-rr-angle-small-right")
    order = models.IntegerField(verbose_name="Order", default=0)
    active = models.BooleanField(verbose_name="Active", default=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"
