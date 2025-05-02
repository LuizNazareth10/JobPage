from django.db import models

# Create your models here.
class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_salary_visible = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_logo = models.ImageField(upload_to='media/company_logos/', blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    is_remote = models.BooleanField(default=False)
    
    EXPERIENCE_LEVELS = [
    ('Internship', 'Internship'),
    ('Junior', 'Junior'),
    ('Mid-level', 'Mid-level'),
    ('Senior', 'Senior'),
    ('Lead', 'Lead'),
    ('Executive', 'Executive'),
    ]
    
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVELS, blank=True, null=True)

    CONTRACT_TYPES = [
        ('Full-time', 'Full-time'),
        ('Contractor', 'Contractor'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
        ('Temporary', 'Temporary'),
        ('Volunteer', 'Volunteer'),
        ('Other', 'Other'),
    ]
    
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPES, blank=True, null=True)
    
    CATEGORY_CHOICES = [
        ('IT', 'IT'),
        ('Marketing', 'Marketing'),
        ('Finance', 'Finance'),
        ('HR', 'HR'),
        ('Sales', 'Sales'),
        ('Customer Service', 'Customer Service'),
        ('Operations', 'Operations'),
        ('Legal', 'Legal'),
        ('Engineering', 'Engineering'),
        ('Design', 'Design'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Construction', 'Construction'),
        ('Manufacturing', 'Manufacturing'),
        ('Hospitality', 'Hospitality'),
        ('Transportation', 'Transportation'),
        ('Real Estate', 'Real Estate'),
        ('Telecommunications', 'Telecommunications'),
        ('Media', 'Media'),
        ('Entertainment', 'Entertainment'),
        ('Retail', 'Retail'),
        ('Non-profit', 'Non-profit'),
        ('Government', 'Government'),
        ('Agriculture', 'Agriculture'),
        ('Energy', 'Energy'),
        ('Pharmaceutical', 'Pharmaceutical'),
        ('Automotive', 'Automotive'),
        ('Aerospace', 'Aerospace'),
        ('Biotechnology', 'Biotechnology'),
        ('Chemicals', 'Chemicals'),
        ('Textiles', 'Textiles'),
        ('Food and Beverage', 'Food and Beverage'),
        ('Sports', 'Sports'),
        ('Fashion', 'Fashion'),
        ('Art and Culture', 'Art and Culture'),
        ('Travel and Tourism', 'Travel and Tourism'),
        ('Security', 'Security'),
        ('Insurance', 'Insurance'),
        ('Other', 'Other'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    
    benefits = models.TextField(blank=True, null=True)
    
    expires_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    application_link = models.URLField(blank=True, null=True)
    email_to_apply = models.EmailField(blank=True, null=True)
    phone_to_apply = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f'{self.title} - {self.company_name}'