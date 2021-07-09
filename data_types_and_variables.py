little_mermaid = 3
brother_bear = 5
hercules = 1
print (3 * (little_mermaid + brother_bear + hercules))

google = 400
amazon = 380
facebook = 350
print ((10* facebook) + (6 * google) + (4 * amazon))
# this code is probably too vague. 
# remember that explicit is better than implicit.

# create a dictionary:
##google = {
#    "rate": 400,
#    "hours": 6
#}
#amazon = {
#    "rate": 380,
#    "hours": 4
#}











not_full = True
no_conflicts = True
enrolled = not_full and no_conflicts
print (enrolled)








more_than_2 = True
not_expired = True
product_offer = more_than_2 and not_expired
premium = not_expired
print (product_offer, premium)


username = 'codeup'
password = 'notastrongpassword'
# password must be at least 5 characters
# username must be no more than 20 characters
# password cannot be same as username

if (len(username) > 5): print ("This is a good username.")
if (len(password) <= 20): print ("This is a good password.")
if username == password: print ("Username and password cannot be the same.")


