from django.db import models

class BragDocument(models.Model):
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
