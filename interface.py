import mysql.connector as c
import random

agent_id = {5, 7, 13, 17, 18, 21, 28, 30, 31, 33, 35, 37, 38, 39, 40}
selected_agent_id = random.choice(list(agent_id))

con = c.connect(
    host=" localhost", user=" root", passwd="password", database="dbms_project"
)
if con.is_connected():
    print("Successfully Connected....\n")
    print("ADMINISTRATOR : ")
else:
    print("Error Connecting....\n")
cursor = con.cursor()

while 1 > 0:
    print("\n\tEnter 0 : Add Property")
    print("\tEnter 1 : Add Employee")
    print("\tEnter 2 : To run queries")
    print("\tEnter 3 : EXIT")

    try:
        choice = input("\nEnter your choice : ")
    except Exception as e:
        print("invalid input!\n")
        continue

    if choice == "0":
        print("enter seller details...")
        name = input("\tEnter name : ")
        email_id = input("\tEnter email_id : ")
        contact = input("\tEnter contact : ")
        seller_query = "INSERT INTO seller(emp_id,name,email_id,contact,address_line_1,address_line_2,address_line_3) VALUES (%s,%s,%s,%s,%s,%s,%s)"

        print("enter property details...")
        date_of_reg = input("\tEnter date_of_reg(yyyy-mm-dd) : ")
        address_line_1 = input("\tEnter address_line_1 : ")
        address_line_2 = input("\tEnter address_line_2 : ")
        address_line_3 = input("\tEnter address_line_3 : ")
        mode = input("\tEnter mode : ")
        renting_price = float(input("\tEnter renting_price : "))
        selling_price = float(input("\tEnter selling_price : "))
        year_of_construction = int(input("\tEnter year_of_construction : "))
        size = input("\tEnter size : ")
        p_type = input("\tEnter p_type : ")

        # entry for seller
        values = (
            selected_agent_id,
            name,
            email_id,
            contact,
            address_line_1,
            address_line_2,
            address_line_3,
        )
        cursor.execute(seller_query, values)
        con.commit()
        seller_id = cursor.lastrowid

        # entry for property
        query = "INSERT INTO property (seller_id,date_of_reg,address_line_1,address_line_2,address_line_3,mode,renting_price,selling_price,year_of_construction,size,p_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            seller_id,
            date_of_reg,
            address_line_1,
            address_line_2,
            address_line_3,
            mode,
            renting_price,
            selling_price,
            year_of_construction,
            size,
            p_type,
        )
        cursor.execute(query, values)
        con.commit()
        print("Property added successfully...")

    elif choice == "1":
        name = input("\tEnter name : ")
        password = input("\tEnter a password : ")
        designation = input("\tEnter designation : ")
        email_id = input("\tEnter email_id : ")
        contact = input("\tEnter contact : ")
        address_line_1 = input("\tEnter address_line_1 : ")
        address_line_2 = input("\tEnter address_line_2 : ")
        address_line_3 = input("\tEnter address_line_3 : ")

        # entry into login_details
        query = "INSERT INTO login_details (password) VALUES (%s)"
        values = (password,)
        cursor.execute(query, values)
        emp_id = cursor.lastrowid

        # entry into employee
        query = "INSERT INTO employee (emp_id,name,designation,email_id,contact,address_line_1,address_line_2,address_line_3) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            emp_id,
            name,
            designation,
            email_id,
            contact,
            address_line_1,
            address_line_2,
            address_line_3,
        )
        cursor.execute(query, values)
        con.commit()
        print("Employee added successfully...")

    elif choice == "2":
        flag = True
        while flag:
            print("\n\tEnter '0' : to go BACK'")
            print("\tEnter 'q1' : for query_1")
            print("\tEnter 'q2' : for query_2")
            print("\tEnter 'q3' : for query_3")
            print("\tEnter 'q4' : for query_4")
            print("\tEnter 'q5' : for query_5")
            print("\tEnter 'q6' : for query_6\n")

            query_num = input("Enter your query_number : ")

            if query_num == "0":
                flag = False
            elif query_num == "q1":
                query = "SELECT * FROM property WHERE address_line_3 = 'South Delhi' AND year_of_construction > 2020 AND mode = 'R'"
                cursor.execute(query)
                result = cursor.fetchall()
                for each in result:
                    print(each)
            elif query_num == "q2":
                query = "SELECT address_line_1, address_line_2, address_line_3 FROM property WHERE address_line_3 = 'West Delhi' AND selling_price >= 3000000 AND selling_price <= 5000000"
                cursor.execute(query)
                result = cursor.fetchall()
                for each in result:
                    print(each)
            elif query_num == "q3":
                query = "SELECT address_line_1, address_line_2, address_line_3 FROM property WHERE address_line_2 = 'Vijay Nagar'  AND mode = 'R'AND (p_type ='2BHK' or p_type='3BHK') AND renting_price < 15000"
                cursor.execute(query)
                result = cursor.fetchall()
                for each in result:
                    print(each)
            elif query_num == "q4":
                query = "SELECT e.name AS agent_name, SUM(p.selling_price) AS total_amount FROM employee e JOIN seller s ON e.emp_id = s.emp_id JOIN property p ON s.seller_id = p.seller_id JOIN status st ON p.p_id = st.p_id WHERE YEAR(st.date) = 2023 GROUP BY e.name ORDER BY total_amount DESC LIMIT 1"
                cursor.execute(query)
                result = cursor.fetchall()
                for each in result:
                    print(each)
            elif query_num == "q5":
                query = "SELECT s.seller_id, e.name AS agent_name, AVG(p.selling_price) AS avg_selling_price, AVG(DATEDIFF(st.date, p.date_of_reg)) AS avg_time_on_market_in_days FROM seller s JOIN employee e ON s.emp_id = e.emp_id JOIN property p ON s.seller_id = p.seller_id JOIN status st ON p.p_id = st.p_id WHERE YEAR(p.date_of_reg) = 2018 GROUP BY s.seller_id"
                cursor.execute(query)
                result = cursor.fetchall()
                for each in result:
                    print(each)
            elif query_num == "q6":
                print("Most expensive house sold : ")
                query = "SELECT * FROM property WHERE mode = 'Sold' ORDER BY selling_price DESC LIMIT 1"
                cursor.execute(query)
                result = cursor.fetchall()
                for each in result:
                    print(each)
                print("\nMost expensive house rented : ")
                query = "SELECT * FROM property WHERE mode = 'Rented' ORDER BY renting_price DESC LIMIT 1"
                cursor.execute(query)
                result = cursor.fetchall()
                for each in result:
                    print(each)
    elif choice == "3":
        print("exiting...")
        break
    else:
        print("invalid choice!")
con.close()
