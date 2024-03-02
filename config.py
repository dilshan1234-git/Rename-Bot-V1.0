import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "14631157")

API_HASH = os.environ.get("API_HASH", "aa7c2b3be68a7488abdb9de6ce78d311")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6898599695:AAE-rukB-OoPJgxOOOcKKuK_8gv55HiC4ww") 

FORCE_SUB = os.environ.get("FORCE_SUB", "WebXBots") 

DB_NAME = os.environ.get("DB_NAME","")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://dilfilter123:dilfilter123@cluster0.tq9uv2k.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
