import dotenv
import os
import sys
import getpass

# Using builtin sys module for command line arguments
# print(f"\n----  Python Builtin sys Module for argv  ----\n")
#
# print(f"\n---- Output of sys.argv is of type {type(sys.argv)}: ")
# print(sys.argv)


# Getting input
# print(f"\n---- Python Input ----\n")
# username = input("Enter Username: ")
# password = input("Enter Password: ")
# print(f"\nINPUT: Username {username} with password {password} was entered\n")
# exit("\n---- End of the Example")

# Getting input without echo on the Password
# print(f"\n---- Python Input ----\n")
# username = input("Enter Username: ")
# password = getpass.getpass("Enter Password: ")
# print(f"\nGETPASS: Username {username} with password {password} was entered\n")
# print(f"nWhy not use getpass.getuser()? Returns system login: {getpass.getuser()}\n")

# Load credentials from environment variables
print("Check Environment Variables BEFORE load_dotenv... ")
for evar in os.environ:
    print(f"ENV VAR NAME: {evar}\n\t VALUE: {os.getenv(evar)}")
evar = "CODE_RED_PASSWORD"
print(f"\nCheck the Specific Environment Variable: {evar}: {os.getenv(evar)}\n")

# The magic hapens here... witrh verbose set to true we will see whar is thart
# from outr env file.
dotenv.load_dotenv(verbose=True)

print("Check Environment Variables AFTER load_dotenv... ")
# for evar in os.environ:
#     print(f"NAME: {evar}\n\t VALUE: {os.getenv(evar)}")
evar = "CODE_RED_PASSWORD"
print(f"\nCheck the Specific Environment Variable: {evar}: {os.getenv(evar)}\n")

exit("\n----  End of >Example  ----\n")
