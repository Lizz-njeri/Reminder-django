# views.py

from django.shortcuts import render, redirect
from .models import Reminder
from .forms import ReminderForm
import africastalking
from django.views.generic import DeleteView
from django.urls import reverse_lazy


def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            # Save the reminder to the database
            reminder = form.save()
            # Send an SMS reminder
            send_sms(reminder)
            return redirect('reminder_view')
    else:
        form = ReminderForm()
    return render(request, 'reminders/index.html', {'form': form})

def reminder_view(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders/index.html', {'reminders': reminders})

def send_sms(reminder):
    africastalking_username = 'username'
    africastalking_api_key = 'api_key'

    africastalking.initialize(africastalking_username, africastalking_api_key)

    sms = africastalking.SMS

    message = f"Don't forget: {reminder.title} on {reminder.date} at {reminder.time}"

    try:
        response = sms.send(message, [reminder.phone_number])
        print(response)
    except Exception as e:
        print(f"SMS sending failed: {e}")

class ReminderDeleteView(DeleteView):
    model = Reminder
    template_name = 'reminders/reminder_confirm_delete.html'
    success_url = reverse_lazy('reminder_view')
