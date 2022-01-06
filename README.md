# Medical Insurance Web Application
![image](https://user-images.githubusercontent.com/63170874/148388603-4cd8d2f9-0301-485f-933b-75bd35a924d7.png)

Web application to manage a medical insurance company, implemented in python using Flask, Bootstrap5, MySQL database.



# Requirements

 - Python 3
 - MySQL server
 - Python libraries (Flask, mysql-connector-python)

## How to run

 1. Change MySQL connection server, credentials
2. Run `python3 app.py`
3. web app will be hosted at your local host [127.0.0.1:5000](127.0.0.1:5000)

## About authentication
Since this is a course project, a simple login, logout is emplemented with no authentication and one can view the web application as a customer or an admin without entering any login data.

## What can you do
#### As a custome: 

 - File claims
 - Add dependents
 - View available hospitals
 - view your claims
 - purchase a new plan (change current one)
 
#### As an admin: 

 - Add a new hospital and choose plans supported by it
 - View customers, their info, claims and have the ability to accept or deny these claims
 - view latest filed claims

#### As a visitor: 

 - Signup as a new customer

## Current rules
1.  Individual (customer/dependent) can only have one contract and a single contract is linked to only one Individual.​
    
2.  Contract holds the plan type and the beneficiary of that plan.​
    
3.  Hospital can support one or more plan.​
    
4.  Many claims can be filed under the same contract, but the single claim can't be filed by more than one contract.​
    
5.  The dependent is weak entity and depends mainly on the customer​
    
6.  Claim must be filed regarding to only one hospital.​
    
7.  Customers can purchase a new plan and replace the old one with it for themselves and their dependents one at a time.
