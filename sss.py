from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import functions, types
from db import DBHelper
import random, string

db = DBHelper()

# using now() to get current time


#siva's
name = "buv"

api_id = ""

api_hash = ""

company_string = ""
random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
client = TelegramClient(name, api_id, api_hash)
#TELEGRAM API ALONE GIVES CONTACT NUMBER WITHOUT NATION CODE

async def main():
    dialogs = await client.get_dialogs()

    customer_id_phone_no_mappings = {1:["+917010942886","Siva Anandh"]}
    #customer_id_phone_no_mappings = db.find_all_customer_ids_and_phone_numbers()
    #today_product_details = db.get_product_details()
    for customer_id in customer_id_phone_no_mappings:
        #unpaid_transactions = db.get_last_five_unpaid_transactions(customer_id)

        current_customer_id = customer_id
        current_phone_number = customer_id_phone_no_mappings[current_customer_id][0] #formatted one
        first_name = customer_id_phone_no_mappings[current_customer_id][1] + company_string + random_str
        get_contact_result = await client(functions.contacts.GetContactsRequest(hash=0))
        """for u in get_contact_result.users:
            if u.first_name and u.phone:
                print(u.first_name+":"+u.phone)
            elif u.first_name:
                print(u.first_name)
            else:
                print(u.phone)"""
        flag = 0
        for each_user in get_contact_result.users:
            if each_user.phone == current_phone_number[1:]:
                flag = 1
                break
        if flag == 0:
            contact = InputPhoneContact(client_id=0, phone=current_phone_number, first_name=first_name + company_string + random_str, last_name="")
            result = await client(ImportContactsRequest([contact]))
        entity = await client.get_entity(current_phone_number)
        await client.send_message(entity, unpaid_transactions)
        await client.send_message(entity, today_product_details)

with client:
    client.loop.run_until_complete()