import json
import os

from django.conf import settings
from django.shortcuts import render
from django.views import View
from .models import UserPreference
from django.contrib import messages

from expenses.models import Expense
import requests


# Create your views here.
class PreferencesView(View):
    currency_data = []

    def load_json_data(self):
        file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

            for k, v in json_data.items():
                self.currency_data.append({'name': k, 'value': v})

    def get(self, request):

        self.load_json_data()
        return render(request, 'preferences/index.html', context={'currency_data': self.currency_data})

    def post(self, request):
        # Input from the form
        new_currency = request.POST['currency']

        # User Check
        exists = UserPreference.objects.filter(user=request.user).exists()
        if exists:
            user_preferences = UserPreference.objects.get(user=request.user)

            # Old Currency Code
            old_currency = user_preferences.currency[:3]

            # Request To API
            response = requests.get(
                f'https://free.currconv.com/api/v7/convert?q={old_currency}_{new_currency[:3]}&compact=ultra&apiKey=c565e159db89deadcca6')

            # The conversion rate is returned
            # response.json returns the json format or a dict - in python
            # The key will be 'old_currency'_'new_currency' eg: USD_AUD which translates to USD to AUD

            conversion_rate = response.json()[f'{old_currency}_{new_currency[:3]}']

            # Getting all expences of a particular user
            users_expenses = Expense.objects.filter(owner=request.user)

            # Changing every expense to the desired format
            for expense in users_expenses:
                convert = Expense.objects.get(pk=expense.id)
                converted_amount = convert.amount * conversion_rate
                if conversion_rate < 1:
                    if converted_amount < 10:
                        convert.amount = converted_amount
                    elif 10 < converted_amount < 100:
                        convert.amount = round(converted_amount, -1)
                    elif converted_amount > 100:
                        convert.amount = round(converted_amount, -2)
                else:
                    convert.amount = round(converted_amount)
                convert.save()

            user_preferences.currency = new_currency
            user_preferences.save()
        else:
            UserPreference.objects.create(user=request.user, currency=new_currency)
        messages.success(request, 'Changes Saved')
        return render(request, 'preferences/index.html', context={'currency_data': self.currency_data})

