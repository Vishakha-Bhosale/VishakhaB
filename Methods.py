import requests
import json
headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'authorization': "Bearer 2uIcSpFAlNluC5FMiBYU7aMipLdFMg9NCJ-K_0nfPBU"
}

#getting all contacts
def get_contact():
    response = requests.get(
        "https://api.sandbox.split.cash/contacts", headers=headers)
    print(response.status_code)
    print(response.text)


# getting a single customer details from id
def get_single_contact():
    print("\nIndividual Customer\n")
    url = "https://api.sandbox.split.cash/contacts/2e115cc1-1566-41d4-ad66-56814e1c55b6"
    response = requests.get(url, headers=headers)
    print(response.text)


""" 
#getting your bank account id
print("\nMy Bank ID\n")
response = requests.get("https://api.sandbox.split.cash/bank_accounts", headers = headers)
print(response.text) 
 """
# list all payments

def list_payments():
    url = "https://api.sandbox.split.cash/payments"
    response = requests.get(url, headers=headers)
    print(response.status_code)
    #resp_dict = json.loads(response.text)
    # for i in resp_dict:
    #     print("\n",i,"\n",resp_dict[i])

#get a single payment
def get_a_particular_payment():
    url = "https://api.sandbox.split.cash/payments/PB.3uub"
    response = requests.get(url, headers = headers)
    print(response.text)

# making a payment

def making_a_payment():
    print("\nMaking a payment to a contact\n")
    payload = {
        'description': 'making_api_payment',
        'matures_at': '2021-01-21T00:00:00Z',
        'payouts': [
            {
                'amount': 300,
                'description': 'making_api_payment',
                'recipient_contact_id': '2e115cc1-1566-41d4-ad66-56814e1c55b6'
            }]
    }
    url = "https://api.sandbox.split.cash/payments"
    response = requests.post(url, json.dumps(payload), headers=headers)
    print(response.status_code)


# creating a contact
def create_contact():
    payload = {
        'name': 'creating a contactwithapi',
        'email': 'createcontactviaapi@gmail.com',
        'branch_code': '011101',
        'account_number': '003333333'
    }
    url = "https://api.sandbox.split.cash/contacts/anyone"
    response = requests.post(url, json.dumps(payload), headers=headers)
    print(response.status_code)


# propose unassigned agreement
def unassigned_agreements():
    payload = {
        'expiry_in_seconds': '900',
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

#list all unassigned agreements
def list_all_unassigned_agreements():
    url = "https://api.sandbox.split.cash/unassigned_agreements"
    response =  requests.get(url, headers = headers)
    resp_dict = json.loads(response.text)
    for i in resp_dict:
        print("\n",i,":" ,"\n",resp_dict[i])

#return one unassigned agreeement
def single_unassigned_agreement():
    url = "https://api.sandbox.split.cash/unassigned_agreement/A.je3"
    response = requests.get(url, headers = headers)
    print(response.text)

#get a payment request
def get_a_payment_request():
    url = "https://api.sandbox.split.cash/payment_request/PR.w20"
    response = requests.get(url, headers = headers)
    print(response.status_code)

#direct debiting/ payment request 
def direct_debit():
    payload = {
        'description': '21.01 api_payment_request',
        'matures_at': '2021-01-21T02:10:56.000Z',
        'amount': '300',
        'authoriser_contact_id': 'c4e6d5b7-a6a0-4b68-b481-0caaac0d3875',  # one making payment
        'your_bank_account_id': '8cd332a0-8cf3-479b-9e80-c17a22bf63ad'
    }
    url = "https://api.sandbox.split.cash/payment_requests"
    response = requests.post(url, json.dumps(payload), headers=headers)
    print("If successful, the response code should be = 200", response.status_code)

#list paymentrequest
def list_payment_request():
    url = "https://api.sandbox.split.cash/payment_request/outgoing"
    response = requests.get(url, headers = headers)
    print(response.text)


