import sqlite3
import datetime
conn = sqlite3.connect("exp.db")
cur = conn.cursor()
while True:

    print("1. Enter new expense")
    print("2. Enter expense history")
    print("select an option: ")

    choice = int(input())

    if choice == 1:
        date = input("enter the date(yyyy-mm-dd): ")
        description = input("enter the description of the expense: ")


        cur.execute("select distinct category from expenses")
        categories = cur.fetchall()
        print("select a category : ")
        for i, category in enumerate(categories):
            print(f"{i+1}.{category[0]}")
        print(f"{len(categories)+1}.create a new category")

        category_choice= int(input())
        if category_choice== len(categories) + 1:
            category = input("enter new category name: ")
        else:
            category = categories[category_choice-1][0]

        price= input("enter price  of the expense: ")

        cur.execute("insert into expenses values(date,description,category,price)")

        conn.commit()

    elif choice==2:
        print("select an option: ")
        print("1. view all expenses")
        print("2. view montly expense")

        view_choice = int(input())
        if view_choice== 1:
            cur.execute("select * from expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice == 2:
         month=input("enter month: ")
         year= input("enter year: ")
        cur.execute("select category,sum(price) from expenses where month(date)=month and year(date)=year group by category")
        expenses = cur.fetchall()
        for expense in expenses:
            print(f"category:{expense[0]},total:{expense[1]}")


conn.commit()
conn.close()

