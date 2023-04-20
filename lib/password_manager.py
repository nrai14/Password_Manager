# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#   4. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of each of the following:
#       - It must be longer than 7 characters (8 is fine)
#       - It must contain at least one of the following special characters:
#         `!`, `@`, `$`, `%` or `&`
#
# We recommend that you store the passwords in a dictionary, where the keys are
# the service names and the values are the passwords.
#
# Example usage:
#   > password_manager = PasswordManager()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.get_for_service('not_real')
#   None
#   > password_manager.get_for_service('twitter')
#   None
#   > password_manager.list_services()
#   ['gmail', 'facebook']
#

# == YOUR CODE ==

class PasswordManager():
    def __init__(self):
    
        # Added self. to dicitonary so this 'blueprint' is accessible in the other methods
        self.dictionary = {

        }

    def add(self, service_name, string):
        self.service_name = service_name
        self.string = string

    #Updated the list of special characters so it's a proper list
        special_characters = ['!','@','$','%','&']
        
        # Needed to use any() to iterate over the special characters but I had it the wrong way around. Needed to check string in special characters 
        if len(string) > 7 and any(char in string for char in special_characters):
            #Need a placeholder reference name for key/service and then the string/value/password to the key 
            #Originally I used update with update({service_name:string}) which didn't work 
            self.dictionary[service_name] = string
        

    def get_for_service(self, service_name):
        
        return self.dictionary.get(service_name)
    
#items() should list all key value pairs 
# Here I realised that the instructions asked for a list of just the keys. So I needed to use list all the keys instead 
    def list_services(self):
        return list(self.dictionary.keys())