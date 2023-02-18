import pyodbc


class DBHelper:

    driver_name = "{SQL Server}"
    server_name = "SERVER\SQLEXPRESS;"
    database_name = "SH2017_SM"

    # customer table
    customer_id_field_name = "CustomerID"
    customer_table = "dbo.Customer"
    phone_number_field_name = ""
    customer_name_field_name = ""

    # bill table
    bill_table = "dbo.CustomerBill"
    balance_amount_field_name = "BalanceAmount"
    invoice_field_name = ""
    transaction_date_field_name = ""
    total_amount = ""
    limit_thresold = 5

    #product_table
    product_name_field_name = ""
    product_price_field_name = ""
    product_table = ""

    c_id_phone_no_name = {}

    #variables = customer_id_field_name, phone_number_field_name,customer_name_field_name customer_table
    get_cid_and_phone_numbers_and_name = "SELECT {}, {}, {} FROM {}"

    # get_customer_id_query
    # variables - customer_id_field_name, customer_table , customer_id_field_name, phoneno
    get_customer_id = "SELECT {} FROM {} where {} like '%{}%'"

    # get_pending_amount
    # variables balance_amount_field_name,  bill_table, customer_id_field_name, customer_id, customer_id_field_name, customer_id_field_name
    get_pending_amount = "SELECT CAST(SUM({}) AS INTEGER) FROM {} where {} = {} GROUP BY {} HAVING CAST(SUM({}) AS INTEGER) > 0"

    # get_last_five_transactions
    # variables transaction_date_field_name, invoice_field_name, total_amount, balance_amount_field_name|, bill_table, customer_id_field_name, customer_id, transaction_date_field_name, limit_thresold
    get_last_five_transactions = "SELECT {}, {}, {}, {} FROM {} WHERE {} = {} ORDER BY {} LIMIT {}"

    # get_last_five_unpaid_transactions
    # variables transaction_date_field_name, invoice_field_name, total_amount, balance_amount_field_name| , bill_table, customer_id_field_name, customer_id, balance_amount_field_name, transaction_date_field_name, limit thresold
    get_last_five_unpaid_transactions_query = "SELECT {}, {}, {}, {} FROM {} WHERE {} = {} AND CAST({}) > 0 ORDER BY {} LIMIT {}"

    #variables = product_name_field_name, product_price_field_name, product_table
    get_product_details_query = "SELECT {}, {} FROM {}"

    def __init__(self):
        pass

    def find_all_customer_ids_and_phone_numbers(self):
        conn = pyodbc.connect('Driver={};'
                              'Server={};'
                              'Database={};'
                              'Trusted_Connection=yes;'.format(self.driver_name, self.server_name, self.database_name))
        cursor = conn.cursor()
        cursor.execute(self.get_cid_and_phone_numbers_and_name.format(self.customer_id_field_name,self.phone_number_field_name, self.customer_name_field_name, self.customer_table))
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            #CHECK TYPES OF dictionaries AND HANDLE NONE, HANDLE MULTIPLE PHONE NUMBERS, HANDLE NATION CODE
            c_id = row[0]
            p_no = row[1]
            if row[0] not in self.c_id_phone_no_name:
                phone_and_name = row[1]
                phone_and_name.append(row[2])
                self.c_id_phone_no_name[c_id] = p_no
        conn.close()
        return self.c_id_phone_no_name

    def get_last_five_unpaid_transactions(self,c_id):
        conn = pyodbc.connect('Driver={};'
                              'Server={};'
                              'Database={};'
                              'Trusted_Connection=yes;'.format(self.driver_name, self.server_name, self.database_name))
        cursor = conn.cursor()
        cursor.execute(self.get_last_five_unpaid_transactions_query).format(self.transaction_date_field_name, self.invoice_field_name, self.total_amount, self.balance_amount_field_name , self.bill_table, self.customer_id_field_name, c_id, self.balance_amount_field_name, self.transaction_date_field_name, self.limit_thresold)
        unpaid_transactions = []
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            unpaid_transactions.append(row[0] + ',' + row[1] + ',' + row[2], + ',' + row[3])
        #form_formatted_string and return, use better data structure
        conn.close()
        return unpaid_transactions


    def get_product_details(self):
        conn = pyodbc.connect('Driver={};'
                              'Server={};'
                              'Database={};'
                              'Trusted_Connection=yes;'.format(self.driver_name, self.server_name, self.database_name))
        cursor = conn.cursor()
        cursor.execute(self.get_product_details_query.format(self.product_name_field_name, self.product_price_field_name, self.product_table))
        product_details = []
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            product_details.append(row[0] + ',' + row[1] + ',' + row[2], + ',' + row[3])
        conn.close()
        #Form formatted message here itself and return , Handle none values
        return product_details

