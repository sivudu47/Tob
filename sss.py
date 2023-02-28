from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import functions, types
from db import DBHelper
import random, string
import time
from ratelimit import limits, sleep_and_retry
import logging
logging.basicConfig(filename = 'log.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')




db = DBHelper()

# using now() to get current time


#siva's
name = "arya"

api_id = ""

api_hash = ""

company_string = "MOS"

sleep_time = 0

content_length = 3000

no_of_days = 5

owner_phone_number = "9092363875"

owner_name = "sivudu"

CALLS = 5

RATE_LIMIT = 60


random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
client = TelegramClient(name, api_id, api_hash)
#TELEGRAM API ALONE GIVES CONTACT NUMBER WITHOUT NATION CODE

#async def main():
@sleep_and_retry
@limits(calls=CALLS, period=RATE_LIMIT)
async def main():
    """dialogs = await client.get_dialogs()
    customer_id_phone_no_mappings = db.find_all_customer_ids_and_phone_numbers()#{1: ['9944193999', 'S.SANKARI'], 2: ['', 'MAHALAKSHMI TEA SHOP'], 3: ['', 'GOMATHY TEA  STALL'], 4: ['', 'MURUGAN IDLY SHOP'], 5: ['', 'NAMATHUVAR'], 6: ['9489120804', 'SEETHA LAKSHMI'], 7: ['9962382864', 'Balamurugan'], 8: ['9894143470', 'A.R.karthik'], 9: ['', 'SS.chinadurai '], 10: ['', 'karthick cibi'], 11: ['', 'KARUNAS HOTEL'], 12: ['', 'SUDALAI NARAYANAN'], 13: ['', 'SS.CHINNADURAI'], 14: ['', 'P.SENTHIL KUMAR'], 15: ['', 'TITANIC SHANMUGAM'], 16: ['', 'KS TEA STALL'], 20: ['9994496601', 'VADAKAM AKKA '], 21: ['', 'boss'], 22: ['9442054356', 'P.SENTHIL KUMAR'], 23: ['', 'VIKAS'], 24: ['', 'SB HOMES'], 25: ['', 'VARADHARAJAN AUDITOR'], 26: ['', 'RAJAGOPAL '], 27: ['9487868207', 'Sri Rengan '], 28: ['9487868207', 'Sri Rengan'], 29: ['8778064043', 'P.Dinesh'], 30: ['', 'Kathar Store'], 31: ['', 'A3J Mess'], 32: ['', 'TMB அக்கா '], 33: ['', 'R.KRISHNA NADAR'], 34: ['', 'dfgsdg']}
    customer_bill_details = {}#{1: [29689006, {'A72/300120': ['Jan 30 2020  7:16PM', 60, 60], 'B14/310120': ['Jan 31 2020  1:21PM', 112, 112], 'B28/190223': ['Feb 19 2023 12:04AM', 492, 492], 'B29/190223': ['Feb 19 2023 12:06AM', 328, 328], 'B30/190223': ['Feb 19 2023 12:09AM', 2688014, 2688014], 'B31/190223': ['Feb 19 2023 12:27AM', 27000000, 27000000]}]}
    #{}  # key - cid values - list [1- Unpaid amount, 2- Bill details with bill id as key
    today_product_details = db.get_product_details()
    # remove in original system"""
    customer_bill_details = {1: [29689006, {'A72/300120': ['Jan 30 2020  7:16PM', 60, 60, 1121], 'B14/310120': ['Jan 31 2020  1:21PM', 112, 112, 1120], 'B28/190223': ['Feb 19 2023 12:04AM', 492, 492, 5], 'B29/190223': ['Feb 19 2023 12:06AM', 328, 328, 5], 'B30/190223': ['Feb 19 2023 12:09AM', 2688014, 2688014, 5], 'B31/190223': ['Feb 19 2023 12:27AM', 27000000, 27000000, 5]}], 6: [0, {}], 7: [0, {}], 8: [0, {}], 20: [3090, {'A365/190220': ['Feb 19 2020  1:20PM', 2995, 2995, 1101], 'A642/240220': ['Feb 24 2020 12:29PM', 95, 95, 1096]}], 22: [0, {}], 27: [0, {}], 28: [0, {}], 29: [0, {}]}
    customer_id_phone_no_mappings = {1: ['9994242534', 'Sandy'], 2: ['', 'MAHALAKSHMI TEA SHOP'], 3: ['', 'GOMATHY TEA  STALL'], 4: ['', 'MURUGAN IDLY SHOP'], 5: ['', 'NAMATHUVAR'], 6: ['8056766011', 'Sindhuja'], 7: ['9962382864', 'Balamurugan'], 8: ['9894143470', 'A.R.karthik'], 9: ['', 'SS.chinadurai '], 10: ['', 'karthick cibi'], 11: ['', 'KARUNAS HOTEL'], 12: ['', 'SUDALAI NARAYANAN'], 13: ['', 'SS.CHINNADURAI'], 14: ['', 'P.SENTHIL KUMAR'], 15: ['', 'TITANIC SHANMUGAM'], 16: ['', 'KS TEA STALL'], 20: ['7010147410', 'VADAKAM AKKA '], 21: ['', 'boss'], 22: ['9442054356', 'P.SENTHIL KUMAR'], 23: ['', 'VIKAS'], 24: ['', 'SB HOMES'], 25: ['', 'VARADHARAJAN AUDITOR'], 26: ['', 'RAJAGOPAL '], 27: ['9003552999', 'Sri Rengan '], 28: ['9003552999', 'Sri Rengan'], 29: ['8778064043', 'P.Dinesh'], 30: ['', 'Kathar Store'], 31: ['', 'A3J Mess'], 32: ['', 'TMB அக்கா '], 33: ['', 'R.KRISHNA NADAR'], 34: ['', 'dfgsdg']}
    today_product_details = {}
    """for customer_id in customer_id_phone_no_mappings:
        if customer_id_phone_no_mappings[customer_id][0] == '':
            continue
        current_customer_details = []
        current_customer_unpaid_balance = db.get_unpaid_amount(customer_id)
        current_customer_bill_dict = db.get_unpaid_transactions(customer_id, no_of_days)
        current_customer_details.append(current_customer_unpaid_balance)
        current_customer_details.append(current_customer_bill_dict)
        customer_bill_details[customer_id] = current_customer_details"""
    #for owner message
    get_contact_result = await client(functions.contacts.GetContactsRequest(hash=0))

    # Invalid no - empty no, less than 10 digits or greater than 13 digits
    # owner_no_fix
    if not (owner_phone_number.startswith("+91")) and len(owner_phone_number) == 10:
        owner_number = "+91" + owner_phone_number
    elif not (owner_phone_number.startswith("+")) and len(owner_phone_number) == 12:
        owner_number = "+" + owner_phone_number
    else:
        owner_number = owner_phone_number
    flag = 0
    for each_user in get_contact_result.users:
        if each_user.phone == owner_number[1:]:
            flag = 1
            break
    if flag == 0:
        contact = InputPhoneContact(client_id=0, phone=owner_number,
                                    first_name=owner_name + '_' + company_string, last_name="")
        result = await client(ImportContactsRequest([contact]))
    owner_number_exception = False
    try:
        entity = await client.get_entity(owner_number)
    except:
        already_exists = False
        with open("no_telegram.txt", "r") as myfile:
            if owner_number in myfile.read():
                already_exists = True
        with open("no_telegram.txt", "a") as myfile:
            if not already_exists:
                details = "Name: {}, Phone: {}\n".format(owner_name, owner_number)
                myfile.write(details)
        owner_number_exception = True
    msg_content = "ஹலோ ! {} நாட்களுக்கு மேல் நிலுவையில் உள்ள பரிவர்த்தனைகள்\n".format(no_of_days)
    for customer_id in customer_id_phone_no_mappings:
        if owner_number_exception:
            continue
        bill_exists = False
        current_phone_number = customer_id_phone_no_mappings[customer_id][0]
        if current_phone_number == '' or len(current_phone_number) < 10 or len(current_phone_number) > 13:
            continue
        if customer_id in customer_bill_details and  customer_bill_details[customer_id][0] <= 0:
            continue
        msg_content += "\nவாடிக்கையாளர் அடையாள எண்: {}\nவாடிக்கையாளர் பெயர்: {}\nவாடிக்கையாளர் தொடர்பு எண்: {}\n\n".format(customer_id,customer_id_phone_no_mappings[customer_id][1], customer_id_phone_no_mappings[customer_id][0])
        if customer_id_phone_no_mappings[customer_id][0] == '':
            continue
        if customer_id in customer_bill_details:
            unpaid_balance = customer_bill_details[customer_id][0]
            msg_content += "உங்கள் மொத்த செலுத்தப்படாத தொகை : {} Rupees\n\n".format(str(unpaid_balance))
            msg_content += "{} நாட்களுக்கு மேல் நிலுவையில் உள்ள பரிவர்த்தனைகள் :\n\n".format(no_of_days,str(unpaid_balance))
            current_customer_bill_details = customer_bill_details[customer_id][1]
            for bill_ids, each_bill in enumerate(current_customer_bill_details):
                bill_exists = True
                invoice_no = each_bill
                transaction_date = current_customer_bill_details[each_bill][0]
                total_amount = current_customer_bill_details[each_bill][1]
                balance_amount = current_customer_bill_details[each_bill][2]
                datediff = current_customer_bill_details[each_bill][3]
                if len(msg_content) > content_length:
                    time.sleep(sleep_time)
                    await client.send_message(entity, msg_content)
                    msg_content = ""
                msg_content += "பில் எண்:{}\nநீங்கள் இந்த பரிவர்த்தனையை செய்து {} நாட்கள் ஆகிவிட்டன\nபரிவர்த்தனை எண்: {}\nபரிவர்த்தனை தேதி: {}\nமொத்த தொகை : {}\nமீதமுள்ள தொகை: {}\n\n".format(bill_ids +1,datediff, invoice_no, transaction_date, total_amount, balance_amount)
            msg_content += "-----------------------------------------------------------------------\n\n"
    if len(msg_content) > 1:
        time.sleep(sleep_time)
        await client.send_message(entity, msg_content)

    msg_content = "இன்றைய விலையைக் கண்டறியவும்\n\n"
    product_exists = False
    for item, product in enumerate(today_product_details):
        product_exists = True
        if len(msg_content) > content_length:
            time.sleep(sleep_time)
            await client.send_message(entity, msg_content)
            break
            msg_content = ""
        p_name = today_product_details[product][0]
        p_price = today_product_details[product][1]
        p_id = product
        msg_content += "வரிசை எண்: {}\nதயாரிப்பு அடையாள எண்: {}\nதயாரிப்பின் பெயர்: {}\nவிலை: {}\n\n".format(item + 1,
                                                                                                             p_id,
                                                                                                             p_name,
                                                                                                             p_price)
    if product_exists:
        time.sleep(sleep_time)
        await client.send_message(entity, msg_content)
    logging.debug(
        'Owner Message Completed')
    #for individual messages
    for customer_id in customer_id_phone_no_mappings:
        bill_exists = False
        #Invalid no - empty no, less than 10 digits or greater than 13 digits
        current_phone_number = customer_id_phone_no_mappings[customer_id][0]
        current_name = customer_id_phone_no_mappings[customer_id][1]
        if current_phone_number == '' or len(current_phone_number) < 10 or len(current_phone_number) > 13:
            continue
        if not(current_phone_number.startswith("+91")) and len(current_phone_number) == 10:
            current_phone_number = "+91" + current_phone_number
        elif not(current_phone_number.startswith("+")) and len(current_phone_number) == 12:
            current_phone_number = "+" + current_phone_number
        msg_content = "ஹலோ ! உங்கள் பரிவர்த்தனை விவரங்கள்\n\nவாடிக்கையாளர் அடையாள எண்: {}\n\nவாடிக்கையாளர் பெயர்: {}\n\nவாடிக்கையாளர் தொடர்பு எண்: {}\n\n".format(
            customer_id, customer_id_phone_no_mappings[customer_id][1], customer_id_phone_no_mappings[customer_id][0])
        if customer_id_phone_no_mappings[customer_id][0] == '':
            continue
        if customer_id in customer_bill_details:
            unpaid_balance = customer_bill_details[customer_id][0]
            msg_content += "உங்கள் மொத்த செலுத்தப்படாத தொகை : {} Rupees\n\n".format(str(unpaid_balance))
            msg_content += "{} நாட்களுக்கு மேல் நிலுவையில் உள்ள உங்களது பரிவர்த்தனைகள் :\n\n".format(str(no_of_days))
            current_customer_bill_details = customer_bill_details[customer_id][1]
            for bill_id, each_bill in enumerate(current_customer_bill_details):
                if len(msg_content) > content_length:
                    time.sleep(sleep_time)
                    await client.send_message(entity, msg_content)
                    msg_content = ""
                bill_exists = True
                invoice_no = each_bill
                transaction_date = current_customer_bill_details[each_bill][0]
                total_amount = current_customer_bill_details[each_bill][1]
                balance_amount = current_customer_bill_details[each_bill][2]
                datediff = current_customer_bill_details[each_bill][3]
                msg_content += "பில் எண்:{}\nநீங்கள் இந்த பரிவர்த்தனையை செய்து {} நாட்கள் ஆகிவிட்டன\nபரிவர்த்தனை எண்: {}\nபரிவர்த்தனை தேதி: {}\nமொத்த தொகை : {}\nமீதமுள்ள தொகை: {}\n\n".format(bill_id +1,datediff, invoice_no, transaction_date, total_amount, balance_amount)
        get_contact_result = await client(functions.contacts.GetContactsRequest(hash=0))
        flag = 0
        for each_user in get_contact_result.users:
            if each_user.phone == current_phone_number[1:]:
                flag = 1
                break
        if flag == 0:
            contact = InputPhoneContact(client_id=0, phone=current_phone_number,
                                        first_name=current_name + company_string, last_name="")
            result = await client(ImportContactsRequest([contact]))
        current_phone_number_exception = False
        try:
            entity = await client.get_entity(current_phone_number)
        except:
            already_exists = False
            with open("no_telegram.txt", "r") as myfile:
                if current_phone_number in myfile.read():
                    already_exists = True
            with open("no_telegram.txt", "a") as myfile:
                if not already_exists:
                    details = "Name: {}, Phone: {}, CustomerId: {}\n".format(current_name, current_phone_number, customer_id)
                    myfile.write(details)
            current_phone_number_exception = True
        if current_phone_number_exception:
            continue
        if bill_exists:
            time.sleep(sleep_time)
            await client.send_message(entity, msg_content)
        msg_content = "இன்றைய விலையைக் கண்டறியவும்\n\n"
        product_exists = False
        for item,product in enumerate(today_product_details):
            product_exists = True
            if len(msg_content) > content_length:
                time.sleep(sleep_time)
                await client.send_message(entity, msg_content)
                break
                msg_content = ""
            p_name = today_product_details[product][0]
            p_price = today_product_details[product][1]
            p_id = product
            msg_content += "வரிசை எண்: {}\nதயாரிப்பு அடையாள எண்: {}\nதயாரிப்பின் பெயர்: {}\nவிலை: {}\n\n".format(item+1, p_id, p_name, p_price)
        if product_exists:
            time.sleep(sleep_time)
            await client.send_message(entity, msg_content)
        logging.debug('Individual Message completed for {} , {} , {}'.format(customer_id, current_phone_number, current_name))


    """"#for debugging purpose
    print("*******************************************************************")
    for customer in customer_bill_details:
        print(customer, customer_bill_details[customer])
    print("*******************************************************************")
    today_product_details = db.get_product_details()
    #unpaid_transactions = db.get_unpaid_transactions(customer_id)
    #dialogs = await client.get_dialogs()

    #customer_id_phone_no_mappings = {1:["+917010942886","Siva Anandh"]}
    customer_id_phone_no_mappings = db.find_all_customer_ids_and_phone_numbers()
    #today_product_details = db.get_product_details()
    for customer_id in customer_id_phone_no_mappings:
        if customer_id_phone_no_mappings[0] == '':
            continue
        #unpaid_transactions = db.get_last_five_unpaid_transactions(customer_id)

        current_customer_id = customer_id
        current_phone_number = customer_id_phone_no_mappings[current_customer_id][0] #formatted one
        first_name = customer_id_phone_no_mappings[current_customer_id][1] + company_string + random_str
        get_contact_result = await client(functions.contacts.GetContactsRequest(hash=0))
        for u in get_contact_result.users:
            if u.first_name and u.phone:
                print(u.first_name+":"+u.phone)
            elif u.first_name:
                print(u.first_name)
            else:
                print(u.phone)
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
        await client.send_message(entity, today_product_details)"""



with client:
    client.loop.run_until_complete(main())