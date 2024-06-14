import datetime
import re
import time

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def get_end_date():
    date_input = input("Enter end date and time in format YYYY-MM-DD HH:MM:SS:\n")
    try:
        return datetime.datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Incorrect format. Please try again.")
        return get_end_date()

def convert_url(url):
    match = re.search(r'https?://(www\.)?([^/]+)', url.strip())
    if match:
        domain = match.group(2)
        return f'www.{domain}'
    return url.strip()

def get_website_list():
    website_list = []
    print("Enter the websites you want to block (type 'done' to finish):")
    while True:
        url = input()
        if url.lower() == 'done':
            break
        website_list.append(convert_url(url))
    return website_list

def block_websites(website_list):
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in website_list:
            if website not in content:
                file.write(f"{redirect} {website}\n")

def unblock_websites(website_list):
    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

def main():
    end_date = get_end_date()
    try:
        print("End date: ", end_date)

        website_list = get_website_list()
        print("Websites to block:")
        for website in website_list:
            print(website)

        while True:
            current_time = datetime.datetime.now()
            if current_time < end_date:
                print(f"Working hours... (Current time: {current_time})")
                block_websites(website_list)
            else:
                unblock_websites(website_list)
                print(f"Fun hours... (Current time: {current_time})")
                break
            time.sleep(10) 
        print("Done!")
    except KeyboardInterrupt:
        unblock_websites(website_list)
        print("Program stopped.")

if __name__ == "__main__":
    main()
