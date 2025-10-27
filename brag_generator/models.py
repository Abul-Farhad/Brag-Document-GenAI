from django.db import models
from django.conf import settings

class BragDocument(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255)
    month = models.CharField(max_length=50)
    generated_at = models.DateTimeField(auto_now_add=True)
    
    work_accomplishments = models.JSONField()
    learning = models.JSONField()
    utilized_skills = models.JSONField()
    
    class Meta:
        ordering = ['-generated_at']
    
    def __str__(self):
        return f"{self.employee_name} - {self.month}"
