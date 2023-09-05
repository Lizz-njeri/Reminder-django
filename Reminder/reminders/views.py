from django.shortcuts import render, get_object_or_404, redirect
from .models import Reminder
from .forms import ReminderForm

import africastalking

# Initialize Africa's Talking API
username = "your_username"
api_key = "your_api_key"
africastalking.initialize(username, api_key)
def send_sms(phone_number, message):
    sms = africastalking.SMS
    response = sms.send(message, [phone_number])
    return response



def reminder_list(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders/reminder_list.html', {'reminders': reminders})

def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            # Implement SMS notification here
            send_sms('+2547.....', 'Your reminder has been placed')
            return redirect('reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'reminders/reminder_form.html', {'form': form})

def edit_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            # Implement SMS notification here
            return redirect('reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'reminders/reminder_form.html', {'form': form})

def delete_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminder_list')
    return render(request, 'reminders/reminder_confirm_delete.html', {'reminder': reminder})

