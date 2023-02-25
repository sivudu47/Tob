import pyodbc


class DBHelper:

    driver_name = "{SQL Server}"
    server_name = "SERVER\SQLEXPRESS;"
    database_name = "SH2017_SM"

    # customer table
    customer_id_field_name = "CustomerID"
    customer_table = "dbo.Customer"
    phone_number_field_name = "ContactNumber"
    customer_name_field_name = "Name"

    # bill table
    bill_table = "dbo.CustomerBill"
    balance_amount_field_name = "BalanceAmount"
    paid_amount_field_name = "PaidAmount"
    invoice_field_name = "SalesInvoiceNo"
    transaction_date_field_name = "SalesDate"
    total_amount = "BillAmount"
    limit_thresold = 5

    #product_table
    product_name_field_name = "ProductName"
    product_price_field_name = "DealerPrice"
    product_table = "dbo.Product"
    product_id_field_name = "ProductID"

    c_id_phone_no_name = {}
    product_details = {}

    #variables = customer_id_field_name, phone_number_field_name,customer_name_field_name customer_table
    get_cid_and_phone_numbers_and_name = "SELECT {}, {}, {} FROM {}"

    # get_customer_id_query
    # variables - customer_id_field_name, customer_table , customer_id_field_name, phoneno
    get_customer_id = "SELECT {} FROM {} where {} like '%{}%'"

    # get_pending_amount
    # variables balance_amount_field_name,  bill_table, customer_id_field_name, customer_id, customer_id_field_name, balance_amount_field_name
    get_pending_amount = "SELECT CAST(SUM({}) AS INTEGER) FROM {} where {} = {} GROUP BY {} HAVING CAST(SUM({}) AS INTEGER) > 0"

    # get_last_five_transactions
    # variables transaction_date_field_name, invoice_field_name, total_amount, balance_amount_field_name|, bill_table, customer_id_field_name, customer_id, transaction_date_field_name, limit_thresold
    get_last_five_transactions = "SELECT {}, {}, {}, {}, {} FROM {} WHERE {} = {} ORDER BY {} LIMIT {}"

    # get_last_five_unpaid_transactions
    # variables transaction_date_field_name, invoice_field_name, total_amount, balance_amount_field_name ,datediff, bill_table, customer_id_field_name, customer_id, balance_amount_field_name, transaction_date_field_name
    get_last_five_unpaid_transactions_query = "SELECT CAST({} AS VARCHAR), {}, CAST({} AS INTEGER), CAST({} AS INTEGER),  abs(DATEDIFF(day,GETDATE(), {}))  FROM {} WHERE {} = {} AND CAST({} AS INTEGER) > 0 AND  abs(DATEDIFF(day,GETDATE(), {})) >= {} ORDER BY {}"

    #variables = product, product_name_field_name, product_price_field_name, product_table
    get_product_details_query = "SELECT {}, {}, CAST({} AS INTEGER) FROM {}"

    #sample = "SELECT CAST(SalesDate AS VARCHAR), SalesInvoiceNo, CAST(BillAmount AS INTEGER), CAST(BalanceAmount AS INTEGER),  abs(DATEDIFF(day, getdate(), SalesDate))  FROM dbo.CustomerBill WHERE CustomerID = 1 AND CAST(BalanceAmount AS INTEGER) > 0  ORDER BY SalesDate"

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
            c_name = row[2]
            if "," in p_no:
                p_no = p_no.split(',')[0]
            if row[0] not in self.c_id_phone_no_name:
                phone_and_name = []
                phone_and_name.append(p_no)
                phone_and_name.append(c_name)
                self.c_id_phone_no_name[c_id] = phone_and_name
        conn.close()
        #debugging pls remove
        """for i in self.c_id_phone_no_name:
            print(i,self.c_id_phone_no_name[i])"""
        return self.c_id_phone_no_name

    #returns a dict of bill details of a customer with the customer id as key
    def get_unpaid_transactions(self,c_id, no_of_days):
        conn = pyodbc.connect('Driver={};'
                              'Server={};'
                              'Database={};'
                              'Trusted_Connection=yes;'.format(self.driver_name, self.server_name, self.database_name))
        cursor = conn.cursor()
        #debugging
        #print(self.get_last_five_unpaid_transactions_query.format(self.transaction_date_field_name, self.invoice_field_name, self.total_amount, self.balance_amount_field_name, self.transaction_date_field_name, self.bill_table, self.customer_id_field_name, c_id, self.balance_amount_field_name,self.transaction_date_field_name, self.no_of_days, self.transaction_date_field_name))
        cursor.execute(self.get_last_five_unpaid_transactions_query.format(self.transaction_date_field_name, self.invoice_field_name, self.total_amount, self.balance_amount_field_name, self.transaction_date_field_name, self.bill_table, self.customer_id_field_name, c_id, self.balance_amount_field_name,self.transaction_date_field_name, no_of_days, self.transaction_date_field_name))
        unpaid_transactions = {}
        #import pdb;pdb.set_trace()
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            transaction_date = row[0]
            invoice_no = row[1]
            total_amount = row[2]
            balance_amount = row[3]
            datediff = row[4]
            unpaid_transactions[invoice_no] = []
            temp_details_list= []
            temp_details_list.append(transaction_date)
            temp_details_list.append(total_amount)
            temp_details_list.append(balance_amount)
            temp_details_list.append(datediff)

            unpaid_transactions[invoice_no] = temp_details_list        #form_formatted_string and return, use better data structure
        conn.close()
        return unpaid_transactions

        # returns the unpaid amount as INT
    def get_unpaid_amount(self, c_id):
        conn = pyodbc.connect('Driver={};'
                              'Server={};'
                              'Database={};'
                              'Trusted_Connection=yes;'.format(self.driver_name, self.server_name,
                                                               self.database_name))
        cursor = conn.cursor()
        #debugging
        #print(self.balance_amount_field_name, self.bill_table, self.customer_id_field_name, c_id, self.customer_id_field_name, self.balance_amount_field_name)
        #print(self.get_pending_amount.format(self.balance_amount_field_name, self.bill_table, self.customer_id_field_name, c_id, self.customer_id_field_name, self.balance_amount_field_name))
        cursor.execute(self.get_pending_amount.format(self.balance_amount_field_name, self.bill_table, self.customer_id_field_name, c_id, self.customer_id_field_name, self.balance_amount_field_name))

        unpaid_amount = 0
        row = cursor.fetchone()
        if row:
            unpaid_amount = row[0]
        # form_formatted_string and return, use better data structure
        conn.close()
        return unpaid_amount


    def get_product_details(self):
        conn = pyodbc.connect('Driver={};'
                              'Server={};'
                              'Database={};'
                              'Trusted_Connection=yes;'.format(self.driver_name, self.server_name, self.database_name))
        cursor = conn.cursor()
        cursor.execute(self.get_product_details_query.format(self.product_id_field_name,self.product_name_field_name, self.product_price_field_name, self.product_table))
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            product_id = row[0]
            product_name = row[1]
            product_value = row[2]
            product_details_list = []
            product_details_list.append(product_name)
            product_details_list.append(product_value)
            self.product_details[product_id] = product_details_list
        conn.close()
        # debugging pls remove
        """for i in self.product_details:
            print(i, self.product_details[i])"""
        #Form formatted message here itself and return , Handle none values
        return self.product_details