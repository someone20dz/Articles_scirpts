# Registration system

"""
Author: Radhouane Mameri

Date: January 15, 2022 => January 22, 2022

Title: Registration System

Description:

This application is meant to run in the command line.
"""

# Importing required modules
import sqlite3
import getpass


def create_database():
    # Connect to a data base
    create_database.connection = sqlite3.connect("user.db")

    # Create a cursor (used to make the connection for executing SQL queries. It acts as middleware between SQLite database connection and SQL query)
    create_database.cursor = create_database.connection.cursor()


    # Create a table (includes user information)
    create_database.cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
            db_username text,
            db_email text,
            db_password text,
            db_age INTEGER,
            db_gender text
        ) """)


def guest():
    print("Hello You wish to 1.Register 2.Login")
    guest_choice = int(input("Choose a number: "))
    if guest_choice == 1:
        create_database()
        register()
    elif guest_choice == 2:
        create_database()
        login()


def register():
    register.username = input("Choose your username: ")
    register.email = input("Choose your Email: ")
    register.password = getpass.getpass("Choose your password: ")
    register.age = int(input("Choose your age: "))
    register.gender = input("Choose your gender(male/female): ")
    check()


def check():
    create_database.cursor.execute("SELECT db_username, db_email FROM users WHERE db_username = ? OR db_email = ? ", (register.username, register.email))
    result = create_database.cursor.fetchone()

    registerInProgress = True
    while registerInProgress:
        if result:
            print("User already exists Press 1 to register Press 2 to log in")
            user_choice = int(input("Press a number: "))
            if user_choice == 1:
                register()
            elif user_choice == 2:
                login()
                break
        else:
            registerInProgress = False
            print("Registration was successful!!!!")
            create_database.cursor.execute("INSERT INTO users VALUES (?,?,?,?,?) ", (register.username, register.email, register.password, register.age, register.gender))
            login()


    # Commit the command
    create_database.connection.commit()

    # Close the connection
    create_database.connection.close()


def login():
    print("Login :D")
    login_username = input("username: ")
    login_password = getpass.getpass("password: ")

    create_database.cursor.execute("SELECT db_username, db_password FROM users WHERE db_username = ? AND db_password = ? ", (login_username, login_password))
    login_result = create_database.cursor.fetchone()


    if login_result:
        print("Logged in successfully")
        main_menu()
    else:
        print("Error, Wrong informations")


def main_menu():
    print("Welcome to the menu!!!!")

guest()
