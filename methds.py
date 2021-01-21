def getcontact():
    response = requests.get(
        "https://api.sandbox.split.cash/contacts", headers=headers)
    print(response.status_code)
    print(response.text)
getcontact()

#getting a single customer details from id
def getsinglecontact():
    print("\nIndividual Customer\n")
    url = "https://api.sandbox.split.cash/contacts/2e115cc1-1566-41d4-ad66-56814e1c55b6"
    response = requests.get(url, headers = headers)
    print(response.text)
getsinglecontact()

""" #getting your bank account id
print("\nMy Bank ID\n")
response = requests.get("https://api.sandbox.split.cash/bank_accounts", headers = headers)
print(response.text) """

#making a payment
def makingapayment():
    print("\nMaking a payment to a contact\n")
    payload = {
        'description': 'making_api_payment',
        'matures_at': '2021-01-21T00:00:00Z',
        'payouts' : [
            {
                'amount':300, 
                'description':'making_api_payment',
                'recipient_contact_id':'2e115cc1-1566-41d4-ad66-56814e1c55b6'
            }]
    }
    url = "https://api.sandbox.split.cash/payments"
    response = requests.post(url, json.dumps(payload), headers = headers)
    print(response.status_code) 
makingapayment()

#creating a contact
def createcontact():
    payload = {
        'name': 'creating a contactwithapi',
        'email':'createcontactviaapi@gmail.com',
        'branch_code':'011101',
        'account_number':'003333333'
    }
    url = "https://api.sandbox.split.cash/contacts/anyone"
    response = requests.post(url,json.dumps(payload),headers = headers)
    print(response.status_code)
createcontact()

# propose unassigned agreement
def unassigned_agreements():
    payload = {
        'expiry_in_seconds':'900',
        'terms': 
            {'per_payout': 
                {
                    'min_amount': 'null',
                    'max_amount': '1000',
                },
                'per_frequency': 
                    {
                    'days': '7',
                    'max_amount': '10000'
                }
                }
             
    }
    url = "https://api.sandbox.split.cash/unassigned_agreements"
    response = requests.post(url, json.dumps(payload), headers=headers)
    print(response.text)
unassigned_agreements()
def directdebit():
    payload = {
        'description': '21.01 api_payment_request',
        'matures_at': '2021-01-21T02:10:56.000Z',
        'amount': '300',
        # one who is going to make a payment
        'authoriser_contact_id': 'c4e6d5b7-a6a0-4b68-b481-0caaac0d3875',
        'your_bank_account_id': '8cd332a0-8cf3-479b-9e80-c17a22bf63ad'
        }
    url = "https://api.sandbox.split.cash/payment_requests"
    response = requests.post(url, json.dumps(payload), headers=headers)
    print(response.status_code)
directdebit()

