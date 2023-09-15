This is a Project Folder for "GUVI Intern" - "https://www.demoblaze.com” website.

There are two Folder:-

1. Test_Codes - It consists of Test File as mentioned below

                    > selenium_projects.py

                        > Test Case #1 (Homepage Verification):-
                             * Verifted that the homepage loads successfully.
                             * Check the presence of key elements, such as the website logo and navigation menus.

                        > Test Case #2 (Registration with valid data):-
                             * Clicked on the "Sign Up"  button.
                             * Filled the registration form with valid data.
                             * Clicked on the "Sign Up"  button.

                        > Test Case #3 (User Login):-
                             * Clicked on the "Login" button.
                             * Entered valid login details.
                             * Clicked the login button.
                             * Verifed that the user is logged in successfully.

                        > Test Case #4 (Product Selection and Cart Interaction):-
                             * Navigate to a product category Phones.
                             * Clicked on a product to view its details.
                             * Added the product to the cart.
                             * Verifed that the product is added to the cart successfully.

                        > Test Case #5(Placing an Order):-
                             * Clicked on the cart to go to the cart page.
                             * Reviewed the item in the cart.
                             * Clicked on the "Place Order" button
                             * Filled the shipping details and Purchase item.
                             * Verified that the Item is Purchased.

                        > Test Case #6 (Logout):-
                             * Clicked the "Logout" button.
                             * Verifed that the user is logged out and redirected to the homepage.


2. Test_Datas - It consists of Test Data's i.e. username, password, XPATH, ID, Send_keys, etc and file name mentioned below
                    > data

NOTE # If you want to run a Test File Kindly go to the Test_Codes to run a specific Python Selenium Automation File.


COMMAND TO RUN A TEST FILE USING PYTEST:-
--------------------------
            pytest -v -s selenium_projects.py

COMMAND TO RUN A TEST FILE REPORT USING PYTEST:-
---------------------------------
    pytest -v -s --capture=sys --html=C:/GUVI_Intern_report/selenium_projects.html selenium_projects.py
