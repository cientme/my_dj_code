from django.dispatch import Signal, receiver


# Creating Signals
notification = Signal()


# Receiver Function
@receiver(notification)
def show_notification(sender, **kwargs):
    print('Sender:', sender)
    print(f"Kwrgas: {kwargs}")
    print("Notification")