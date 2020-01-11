from django.db import models
import uuid # Required for unique id


class Mouse(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Unique ID for this particular id.',
        editable=False)
    #store numbers up to approximately one billion with a resolution of 10 decimal places
    currency = models.DecimalField(
        max_digits=19,
        decimal_places=10)


    def __str__(self):
        return self.uid


class Relationship(models.Model):
    superior = models.ForeignKey(
        'Mouse',
        on_delete=models.CASCADE,
        related_name='superior_relationship_set'
    )

    subordinate = models.ForeignKey(
        'Mouse',
        on_delete=models.CASCADE,
        related_name='subordinate_relationship_set'
    )

    def __str__(self):
        return self.id

class Transaction(models.Model):
    from_mouse = models.ForeignKey(
        'Mouse',
        on_delete=models.CASCADE,
        related_name='from_mouse_transaction_set'
    )

    to_mouse = models.ForeignKey(
        'Mouse',
        on_delete=models.CASCADE,
        related_name='to_mouse_transaction_set'
    )
    #store numbers up to approximately one billion with a resolution of 10 decimal places
    amount = models.DecimalField(
        max_digits=19,
        decimal_places=10)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class Notification(models.Model):
    creator = models.ForeignKey(
        'Mouse',
        on_delete=models.CASCADE,
        related_name='creator_notification_set'
    )

    receiver = models.ForeignKey(
        'Mouse',
        on_delete=models.CASCADE,
        related_name='receiver_notification_set'
    )

    context = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
