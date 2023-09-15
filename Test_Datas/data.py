# It consists of Test Data's i.e. username, password, XPATH, ID, Send_keys, etc :-

class username_password:                            # Username and Password
    username            = 'Srinivasa Prabu R'       # Send_keys
    password            = "Srinivasa Prabu R"       # Send_keys
    
class Test_Case_1:                                  # Homepage Verification
    website_logo        = '//*[@id="nava"]/img'     # XPATH
    navigation_Contact  = 'Contact'                 # LINK_TEXT
    navigation_Monitors = 'Monitors'                # LINK_TEXT
    
class Test_Case_2:                                  # Registration with valid data
    sign_up = 'signin2'                             # ID
    sign_in_username    = 'sign-username'           # ID
    sign_in_password    = 'sign-password'           # ID
    sign_up_button      = '//*[@id="signInModal"]/div/div/div[3]/button[2]' # XPATH
    
class Test_Case_3:                                  # User Login
    navigation_login    = 'login2'                  # ID
    login_username      = 'loginusername'           # ID
    login_password      = 'loginpassword'           # ID
    login_button        = '//*[@id="logInModal"]/div/div/div[3]/button[2]'  # XPATH
    
class Test_Case_4:                                  # Product Selection and Cart Interaction
    phones_button       = 'itemc'                   # ID
    Samsung_galaxy_s6   = '//*[@id="tbodyid"]/div[1]/div/div/h4/a'          # XPATH
    add_to_cart         =  '//*[@id="tbodyid"]/div[2]/div/a'                # XPATH
    
class Test_Case_5:                                  # Placing an Order
    navigation_Cart     = 'cartur'                  # ID
    place_order         = '//*[@id="page-wrapper"]/div/div[2]/button'       # XPATH
    name                = 'name'                    # ID
    name_Send_keys      = 'R.srinivasa Prabu'       # Send_keys
    country             = 'country'                 # ID
    country_Send_keys   = 'India'                   # Send_keys
    city                = 'city'                    # ID
    city_Send_keys      = 'Chennai'                 # Send_keys
    card                = 'card'                    # ID
    card_Send_keys      = '5464 6524 3654 4665'     # Send_keys
    month               = 'month'                   # ID
    month_Send_keys     = 'September'               # Send_keys
    year                = 'year'                    # ID
    year_Send_keys      = '2023'                    # Send_keys
    purchase_button     = '//*[@id="orderModal"]/div/div/div[3]/button[2]'  # XPATH
    Ok_button           = '/html/body/div[10]/div[7]/div/button'            # XPATH
    
class Test_Case_6:                                  # Placing an Order
    logout_button       = 'logout2'                 # ID