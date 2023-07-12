from django.db import models
from open_problems.models.contacts_users import Contact
from open_problems.models.open_problems import OpenProblems
from open_problems.models.references import Reference

class SubmissionManager(models.Manager): 
    def return_active(self): 
        self.filter(is_active = True)
    def return_inactive(self): 
        self.filter(is_active=False)

class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    full_text = models.TextField(null=True)
    open_problem = models.ForeignKey(OpenProblems, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING, blank=True, null=True)
    submitted_references = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False) #When submission is reviewed we set this to true to display on the web page.
    # Are contacts required to submit ??
    
    def __str__(self) -> str:
        return f"{self.submission_id}: {self.full_text}"

    
class SubmissionReferences(models.Model): 
    submission_id = models.ForeignKey(Submission, on_delete=models.CASCADE)
    reference_id = models.ForeignKey(Reference, on_delete=models.CASCADE)




