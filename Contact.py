import requests 
headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'authorization': "Bearer 2uIcSpFAlNluC5FMiBYU7aMipLdFMg9NCJ-K_0nfPBU"
}

response = requests.get("https://api.sandbox.split.cash/contacts", headers = headers)
print(response.status_code)
print(response.text)

#getting a single customer details from id
print("\nIndividual Customer\n")
response = requests.get("https://api.sandbox.split.cash/contacts/2e115cc1-1566-41d4-ad66-56814e1c55b6", headers = headers)
print(response.text)

#getting your bank account id
print("\nMy Bank ID\n")
response = requests.get("https://api.sandbox.split.cash/bank_accounts", headers = headers)
print(response.text)

#making a payment
print("\nMaking a payment to a contact\n")
payload = "{\"description\":\"The SuperPackage\",\"matures_at\":\"2021-01-19T00:00:00Z\",\"your_bank_account_id\":\"8cd332a0-8cf3-479b-9e80-c17a22bf63ad\",\"payouts\":[{\"amount\":30,\"description\":\"testing payments via code\",\"recipient_contact_id\":\"2e115cc1-1566-41d4-ad66-56814e1c55b6\",\"metadata\":{\"invoice_ref\":\"BILL-0001\",\"invoice_id\":\"c80a9958-e805-47c0-ac2a-c947d7fd778d\",\"custom_key\":\"Custom string\",\"another_custom_key\":\"Maybe a URL\"}},{\"amount\":30,\"description\":\"A scuba dive SDS5464\",\"recipient_contact_id\":\"2e115cc1-1566-41d4-ad66-56814e1c55b6\"}]}"
response = requests.post("https://api.sandbox.split.cash/payments", payload, headers = headers)
print(response.text) 

#create a contact
print("\Creating a Split contact")
payload = "{\"name\":\"contactadded with api\",\"email\":\"withapi@gmail.com\",\"branch_code\":\"123056\",\"account_number\":\"099999999\"}"
response = requests.post("https://api.sandbox.split.cash/contacts/anyone",payload,headers = headers)
print(response.status_code)

#propose an unassigned agreement

print("\n Propose an agreement\n")
payload = "{\"expiry_in_seconds\":6000,\"single_use\":false,\"terms\":{\"per_payout\":{\"min_amount\":null,\"max_amount\":10000},\"per_frequency\":{\"days\":7,\"max_amount\":1000000}}}"
response = requests.post("https://api.sandbox.split.cash/unassigned_agreements", payload, headers = headers)
print(response.text)

#Direct Debit a contact 
print("\nDirect Debit a contact\n")
payload = "{\"description\":\"Direct Debiting a contact via api\",\"matures_at\":\"20121-01-20T02:10:56.000Z\",\"amount\":1000,\"authoriser_contact_id\":\"c4e6d5b7-a6a0-4b68-b481-0caaac0d3875\",\"your_bank_account_id\":\"8cd332a0-8cf3-479b-9e80-c17a22bf63ad\",\"precheck_funds\":false,\"metadata\":{\"custom_key\":\"Custom string\",\"another_custom_key\":\"Maybe a URL\"}}"
response = requests.post("https://api.sandbox.split.cash/payment_requests",payload, headers = headers)
print(response.text)

