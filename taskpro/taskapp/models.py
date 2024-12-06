from django.db import models

class Todo(models.Model):
    PRIORITY_CHOICES = (
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    )
    PROGRESS_CHOICES = (
        ('Pending','Pending'),
        ('Ongoing','Ongoing'),
        ('Completed','Completed'),
    )
    Title = models.CharField(max_length=50)
    Description=models.TextField()
    Priority=models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='High'
    )
    Status=models.CharField(
        max_length=50,
        choices=PROGRESS_CHOICES,
        default='Pending',
    )
    Creation_Date=models.DateField(auto_now=True)
    # Deadline=models.DateField()

    def __str__(self):
        return self.Title

