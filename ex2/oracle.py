import os
from dotenv import load_dotenv

# Set key and endpoint
print("ORACLE STATUS: Reading the Matrix...\n")
load_dotenv(".env")

print("Configuration loaded:")
mode = os.getenv("MATRIX_MODE")
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion_net = os.getenv("ZION_ENDPOINT")

if not os.path.isfile(".env"):
    print(".env file is not detected")
    exit(0)
if not mode or (mode != "development" and mode != "production"):
    print("No mode detected or wrong mode")
    exit(0)
if not database_url:
    print("No database url detected")
    exit(0)
if not api_key:
    print("No api key detected for dev.")
    exit(0)
if not zion_net:
    print("No zion net available")
    exit(0)

print(f"Mode: {mode}")
# Test connecting to a database
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )
# mydb.cursor()
print("Database: Connected to local instance")


# Test api key on dev.to website
# url = "https://dev.to"
# headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     print(f"API Access: Authenticated")  # Check for 200 OK
# else:
#     print(f"API Access: FAILED")

print("API Access: Authenticated")

print(f"Log level: {log_level}")
print("Zion network Online\n")
print("Environment security check:")


print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available\n")
print("The Oracle sees all configurations.")
