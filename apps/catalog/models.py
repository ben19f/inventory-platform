from django.db import models

class Item(models.Model):
    # Primary Key id создаётся автоматически, если не указывать
    # id = models.AutoField(primary_key=True)  # опционально

    tenant_id = models.IntegerField(null=True, blank=True, help_text="ID клиента/музея")
    category_id = models.IntegerField(null=True, blank=True, help_text="ID категории предмета")

    title = models.CharField(max_length=255, help_text="Название предмета")
    comment = models.TextField(blank=True, null=True, help_text="Текстовый комментарий")

    attributes = models.JSONField(default=dict, blank=True, help_text="Гибкая структура данных")
    inventory_number = models.CharField(max_length=50, blank=True, null=True, help_text="Инвентарный номер предмета")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.inventory_number})"
