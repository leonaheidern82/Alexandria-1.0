# Alexandria-1.0
# Python code for sending a form through e-mail

# Project Description
This project aims to collect information from a registration form and send it via email. It uses ipywidgets to create an interactive interface with input fields to gather data such as the client ID, delivery date and time, salesperson name, and additional information. When the user clicks the "Confirm" button, all entered data is formatted and sent to a specified email address.

# Features
Data input interface: Collects information through interactive fields created with ipywidgets.
Email sending: After confirmation, the form data is formatted and sent via email.
Customizable content: The email content is formatted to display each input on a separate line.
Form Structure
The form collects the following data:

Client ID: Unique identification for the client.
Delivery Date: The expected delivery date.
Delivery Time: The expected delivery time.
Salesperson Name: The name of the person responsible for the sale.
Additional Information: A field for extra notes, such as special observations regarding the order.
# Requirements
Ensure that the following libraries are installed in the environment where the project will be executed:

IPython
ipywidgets
requests
smtplib
email

# How to Run
Install Dependencies: Install the required libraries (in the case of Google Colab, use !pip install as shown above).
Run the Code: Load the project's main code into your Python environment.
Fill Out the Form: Provide the requested data in the interactive fields.
Send the Email: After filling in the fields, click the "Confirm" button to send the email with the information.

# License
This project is licensed under the MIT License. 
