# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # import time
# # import random
# # import pandas as pd

# # def random_delay():
# #     time.sleep(random.uniform(3, 6))

# # def run_scraper(role, skills, location, limit, extract_contact):

# #     driver = webdriver.Chrome()
# #     driver.maximize_window()

# #     # Step 1: Login
# #     driver.get("https://www.linkedin.com/login")
# #     input("👉 Login manually, then press ENTER here...")

# #     # Step 2: Search
# #     query = skills
# #     search_url = f"https://www.linkedin.com/search/results/people/?keywords={query}"

# #     driver.get(search_url)
# #     time.sleep(5)

# #     # Step 3: Scroll to load profiles
# #     for _ in range(4):
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         time.sleep(3)

# #     # Step 4: Collect profile links
# #     elements = driver.find_elements(By.XPATH, "//a[contains(@href,'/in/')]")

# #     links = []
# #     for el in elements:
# #         link = el.get_attribute("href")
# #         if link and "linkedin.com/in/" in link:
# #             links.append(link.split("?")[0])

# #     # Remove duplicates
# #     unique_links = list(set(links))

# #     print(f"Found {len(unique_links)} profiles")

# #     data = []

# #     # Step 5: Visit profiles
# #     for link in unique_links[:limit]:

# #         driver.get(link)
# #         random_delay()

# #         # NAME
# #         try:
# #             name = driver.find_element(By.XPATH, "//h1").text
# #         except:
# #             name = ""

# #         # HEADLINE (safe)
# #         try:
# #             headline = driver.find_element(By.XPATH, "//div[contains(@class,'text-body-medium')]").text
# #         except:
# #             headline = ""

# #         # LOCATION (FIXED - avoid pronouns)
# #         try:
# #             loc_elements = driver.find_elements(By.XPATH, "//span[contains(@class,'text-body-small')]")
# #             location = ""

# #             for el in loc_elements:
# #                 text = el.text.strip()

# #                 # Skip pronouns like He/Him, She/Her
# #                 if "/" in text:
# #                     continue

# #                 # Skip empty
# #                 if text == "":
# #                     continue

# #                 location = text
# #                 break

# #         except:
# #             location = ""

# #         # CONTACT INFO FIX
# #         email = ""
# #         phone = ""

# #         if extract_contact:
# #             try:
# #                 contact_btn = driver.find_element(By.XPATH, "//a[contains(@href,'contact-info')]")
# #                 contact_btn.click()
# #                 time.sleep(2)

# #                 # EMAIL
# #                 try:
# #                     email = driver.find_element(By.XPATH, "//a[starts-with(@href,'mailto')]").text
# #                 except:
# #                     email = ""

# #                 # PHONE (clean)
# #                 try:
# #                     phone_elements = driver.find_elements(By.XPATH, "//span")

# #                     for p in phone_elements:
# #                         text = p.text.strip()

# #                         if "+" in text and len(text) >= 10:
# #                             phone = text
# #                             break
# #                 except:
# #                     phone = ""

# #                 # Close popup properly
# #                 try:
# #                     close_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label,'Dismiss')]")
# #                     close_btn.click()
# #                 except:
# #                     pass

# #             except:
# #                 pass

# #         data.append({
# #             "Name": name,
# #             "Headline": headline,
# #             "Location": location,
# #             "Email": email,
# #             "Phone": phone,
# #             "Profile": link
# #         })

# #         print(f"Scraped: {name}")

# #     driver.quit()

# #     df = pd.DataFrame(data)

# #     return df




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import random
# import pandas as pd

# # =========================
# # UTIL
# # =========================
# def random_delay():
#     time.sleep(random.uniform(3, 6))

# def clean_text(text):
#     if not text:
#         return ""
#     return text.replace("Â·", "").replace("\n", " ").strip()

# # =========================
# # MAIN SCRAPER
# # =========================
# def run_scraper(role, skills, location, limit, extract_contact):

#     driver = webdriver.Chrome()
#     driver.maximize_window()

#     # -------------------------
#     # LOGIN (MANUAL)
#     # -------------------------
#     driver.get("https://www.linkedin.com/login")
#     input("👉 Login manually, then press ENTER...")

#     # -------------------------
#     # SEARCH (ONLY SKILLS)
#     # -------------------------
#     query = skills
#     search_url = f"https://www.linkedin.com/search/results/people/?keywords={query}"

#     driver.get(search_url)
#     time.sleep(5)

#     # -------------------------
#     # SCROLL
#     # -------------------------
#     for _ in range(5):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(3)

#     # -------------------------
#     # COLLECT PROFILE LINKS
#     # -------------------------
#     elements = driver.find_elements(By.XPATH, "//a[contains(@href,'/in/')]")

#     links = []
#     for el in elements:
#         link = el.get_attribute("href")
#         if link and "linkedin.com/in/" in link:
#             links.append(link.split("?")[0])

#     unique_links = list(set(links))

#     print(f"✅ Found {len(unique_links)} profiles")

#     data = []

#     # -------------------------
#     # VISIT PROFILES
#     # -------------------------
#     for link in unique_links[:limit]:

#         driver.get(link)
#         random_delay()

#         # NAME
#         try:
#             name = clean_text(driver.find_element(By.XPATH, "//h1").text)
#         except:
#             name = ""

#         # HEADLINE
#         try:
#             headline = clean_text(driver.find_element(By.XPATH, "//div[contains(@class,'text-body-medium')]").text)
#         except:
#             headline = ""

#         # =========================
#         # CONTACT INFO
#         # =========================
#         email = ""
#         phone = ""

#         if extract_contact:
#             try:
#                 contact_btn = driver.find_element(By.XPATH, "//a[contains(@href,'contact-info')]")
#                 contact_btn.click()
#                 time.sleep(2)

#                 # EMAIL
#                 try:
#                     email_el = driver.find_element(
#                         By.XPATH,
#                         "//section[contains(@class,'pv-contact-info')]//a[starts-with(@href,'mailto')]"
#                     )
#                     email = clean_text(email_el.text)
#                 except:
#                     email = ""

#                 # PHONE
#                 try:
#                     phone_els = driver.find_elements(
#                         By.XPATH,
#                         "//section[contains(@class,'pv-contact-info')]//span"
#                     )

#                     for p in phone_els:
#                         txt = p.text.strip()

#                         if txt.replace("+", "").replace(" ", "").isdigit() and len(txt) >= 10:
#                             phone = txt
#                             break
#                 except:
#                     phone = ""

#                 # CLOSE POPUP
#                 try:
#                     close_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label,'Dismiss')]")
#                     close_btn.click()
#                 except:
#                     pass

#             except:
#                 pass

#         # =========================
#         # EXPERIENCE (TOP 2)
#         # =========================
#         experience = ""

#         try:
#             exp_elements = driver.find_elements(By.XPATH, "//section[contains(@id,'experience')]//li")

#             exp_list = []
#             for exp in exp_elements[:2]:
#                 try:
#                     role_el = exp.find_element(By.XPATH, ".//span[contains(@class,'t-bold')]").text
#                     company_el = exp.find_element(By.XPATH, ".//span[contains(@class,'t-normal')]").text

#                     exp_list.append(f"{role_el} at {company_el}")
#                 except:
#                     continue

#             experience = " | ".join(exp_list)

#         except:
#             experience = ""

#         # =========================
#         # SKILLS
#         # =========================
#         skills_data = ""

#         try:
#             driver.get(link + "details/skills/")
#             time.sleep(3)

#             skill_elements = driver.find_elements(By.XPATH, "//span[contains(@class,'mr1')]")

#             skills_list = []
#             for s in skill_elements[:5]:
#                 txt = s.text.strip()
#                 if txt:
#                     skills_list.append(txt)

#             skills_data = ", ".join(skills_list)

#         except:
#             skills_data = ""

#         # =========================
#         # SAVE DATA
#         # =========================
#         data.append({
#             "Name": name,
#             "Headline": headline,
#             "Email": email,
#             "Phone": phone,
#             "Experience": experience,
#             "Skills": skills_data,
#             "Profile": link
#         })

#         print(f"✅ Scraped: {name}")

#     driver.quit()

#     df = pd.DataFrame(data)
#     return df


# # =========================
# # RUN SCRIPT
# # =========================
# if __name__ == "__main__":

#     df = run_scraper(
#         role="tester",
#         skills="manual testing",
#         location="india",
#         limit=10,
#         extract_contact=True
#     )

#     df.to_excel("linkedin_data.xlsx", index=False)

#     print("🎉 Data saved to linkedin_data.xlsx")
























































































# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import random
# import pandas as pd

# # =========================
# # UTIL FUNCTIONS
# # =========================
# def random_delay():
#     time.sleep(random.uniform(3, 6))

# def clean_text(text):
#     if not text:
#         return ""
#     return text.replace("Â·", "").replace("\n", " ").strip()

# # =========================
# # MAIN SCRAPER
# # =========================
# def run_scraper(role, skills, location, limit, extract_contact):

#     driver = webdriver.Chrome()
#     driver.maximize_window()

#     # -------------------------
#     # LOGIN
#     # -------------------------
#     driver.get("https://www.linkedin.com/login")
#     input("👉 Login manually, then press ENTER...")

#     # -------------------------
#     # SEARCH (ONLY SKILLS)
#     # -------------------------
#     query = skills
#     search_url = f"https://www.linkedin.com/search/results/people/?keywords={query}"

#     driver.get(search_url)
#     time.sleep(5)

#     # -------------------------
#     # SCROLL
#     # -------------------------
#     for _ in range(5):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(3)

#     # -------------------------
#     # COLLECT PROFILE LINKS
#     # -------------------------
#     elements = driver.find_elements(By.XPATH, "//a[contains(@href,'/in/')]")

#     links = []
#     for el in elements:
#         link = el.get_attribute("href")
#         if link and "linkedin.com/in/" in link:
#             links.append(link.split("?")[0])

#     unique_links = list(set(links))

#     print(f"✅ Found {len(unique_links)} profiles")

#     data = []

#     # -------------------------
#     # VISIT PROFILES
#     # -------------------------
#     for link in unique_links[:limit]:

#         driver.get(link)
#         random_delay()

#         # =========================
#         # NAME
#         # =========================
#         try:
#             name = clean_text(driver.find_element(By.XPATH, "//h1").text)
#         except:
#             name = ""

#         # =========================
#         # HEADLINE
#         # =========================
#         try:
#             headline = clean_text(
#                 driver.find_element(By.XPATH, "//div[contains(@class,'text-body-medium')]").text
#             )
#         except:
#             headline = ""

#         # =========================
#         # ABOUT SECTION
#         # =========================
#         about = ""

#         try:
#             # Click "see more" if exists
#             try:
#                 more_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label,'See more about')]")
#                 more_btn.click()
#                 time.sleep(1)
#             except:
#                 pass

#             about_el = driver.find_element(
#                 By.XPATH,
#                 "//section[.//span[text()='About']]//div[contains(@class,'display-flex')]"
#             )

#             about = clean_text(about_el.text)

#         except:
#             about = ""

#         # =========================
#         # CONTACT INFO
#         # =========================
#         email = ""
#         phone = ""

#         if extract_contact:
#             try:
#                 contact_btn = driver.find_element(By.XPATH, "//a[contains(@href,'contact-info')]")
#                 contact_btn.click()
#                 time.sleep(2)

#                 # EMAIL
#                 try:
#                     email = driver.find_element(
#                         By.XPATH,
#                         "//section[contains(@class,'pv-contact-info')]//a[starts-with(@href,'mailto')]"
#                     ).text.strip()
#                 except:
#                     email = ""

#                 # PHONE
#                 try:
#                     phone_elements = driver.find_elements(
#                         By.XPATH,
#                         "//section[contains(@class,'pv-contact-info')]//span"
#                     )

#                     for el in phone_elements:
#                         txt = el.text.strip()

#                         if txt.replace("+", "").replace(" ", "").isdigit() and len(txt) >= 10:
#                             phone = txt
#                             break
#                 except:
#                     phone = ""

#                 # CLOSE POPUP
#                 try:
#                     driver.find_element(By.XPATH, "//button[contains(@aria-label,'Dismiss')]").click()
#                 except:
#                     pass

#             except:
#                 pass

#         # =========================
#         # SAVE DATA
#         # =========================
#         data.append({
#             "Name": name,
#             "Headline": headline,
#             "About": about,
#             "Email": email,
#             "Phone": phone,
#             "Profile": link
#         })

#         print(f"✅ Scraped: {name}")

#     driver.quit()

#     df = pd.DataFrame(data)
#     return df


# # =========================
# # RUN SCRIPT
# # =========================
# if __name__ == "__main__":

#     df = run_scraper(
#         role="tester",
#         skills="manual testing",
#         location="india",
#         limit=10,
#         extract_contact=True
#     )

#     df.to_excel("linkedin_data.xlsx", index=False)

#     print("🎉 Data saved to linkedin_data.xlsx")






































# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import random
# import pandas as pd


# # =========================
# # UTIL FUNCTIONS
# # =========================
# def random_delay():
#     time.sleep(random.uniform(3, 6))


# def clean_text(text):
#     if not text:
#         return ""
#     return text.replace("Â·", "").replace("\n", " ").strip()


# # =========================
# # LOGIN DETECTION (NEW)
# # =========================
# def wait_for_login(driver, timeout=120):
#     print("👉 Please login manually in browser...")

#     start_time = time.time()

#     while time.time() - start_time < timeout:
#         try:
#             # Detect login by presence of search bar
#             driver.find_element(By.XPATH, "//input[contains(@placeholder,'Search')]")
#             print("✅ Login successful, continuing...")
#             return True
#         except:
#             pass

#         time.sleep(2)

#     raise Exception("❌ Login timeout. Please login faster.")


# # =========================
# # MAIN SCRAPER
# # =========================
# def run_scraper(role, skills, location, limit, extract_contact):

#     driver = webdriver.Chrome()
#     driver.maximize_window()

#     # -------------------------
#     # LOGIN (UPDATED)
#     # -------------------------
#     driver.get("https://www.linkedin.com/login")

#     # ❌ removed input()
#     # ✅ added auto detection
#     wait_for_login(driver)

#     # -------------------------
#     # SEARCH (ONLY SKILLS)
#     # -------------------------
#     query = skills
#     search_url = f"https://www.linkedin.com/search/results/people/?keywords={query}"

#     driver.get(search_url)
#     time.sleep(5)

#     # -------------------------
#     # SCROLL
#     # -------------------------
#     for _ in range(5):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(3)

#     # -------------------------
#     # COLLECT PROFILE LINKS
#     # -------------------------
#     elements = driver.find_elements(By.XPATH, "//a[contains(@href,'/in/')]")

#     links = []
#     for el in elements:
#         link = el.get_attribute("href")
#         if link and "linkedin.com/in/" in link:
#             links.append(link.split("?")[0])

#     unique_links = list(set(links))

#     print(f"✅ Found {len(unique_links)} profiles")

#     data = []

#     # -------------------------
#     # VISIT PROFILES
#     # -------------------------
#     for link in unique_links[:limit]:

#         driver.get(link)
#         random_delay()

#         # NAME
#         try:
#             name = clean_text(driver.find_element(By.XPATH, "//h1").text)
#         except:
#             name = ""

#         # HEADLINE
#         try:
#             headline = clean_text(
#                 driver.find_element(By.XPATH, "//div[contains(@class,'text-body-medium')]").text
#             )
#         except:
#             headline = ""

#         # ABOUT
#         about = ""

#         try:
#             try:
#                 more_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label,'See more about')]")
#                 more_btn.click()
#                 time.sleep(1)
#             except:
#                 pass

#             about_el = driver.find_element(
#                 By.XPATH,
#                 "//section[.//span[text()='About']]//div[contains(@class,'display-flex')]"
#             )

#             about = clean_text(about_el.text)

#         except:
#             about = ""

#         # CONTACT INFO
#         email = ""
#         phone = ""

#         if extract_contact:
#             try:
#                 contact_btn = driver.find_element(By.XPATH, "//a[contains(@href,'contact-info')]")
#                 contact_btn.click()
#                 time.sleep(2)

#                 # EMAIL
#                 try:
#                     email = driver.find_element(
#                         By.XPATH,
#                         "//section[contains(@class,'pv-contact-info')]//a[starts-with(@href,'mailto')]"
#                     ).text.strip()
#                 except:
#                     email = ""

#                 # PHONE (FIXED FILTER)
#                 try:
#                     phone_elements = driver.find_elements(
#                         By.XPATH,
#                         "//section[contains(@class,'pv-contact-info')]//span"
#                     )

#                     for el in phone_elements:
#                         txt = el.text.strip()

#                         cleaned = txt.replace("+", "").replace(" ", "")

#                         if cleaned.isdigit() and len(cleaned) >= 10:
#                             phone = txt
#                             break
#                 except:
#                     phone = ""

#                 # CLOSE POPUP
#                 try:
#                     driver.find_element(By.XPATH, "//button[contains(@aria-label,'Dismiss')]").click()
#                 except:
#                     pass

#             except:
#                 pass

#         # SAVE
#         data.append({
#             "Name": name,
#             "Headline": headline,
#             "About": about,
#             "Email": email,
#             "Phone": phone,
#             "Profile": link
#         })

#         print(f"✅ Scraped: {name}")

#     driver.quit()
    

#     df = pd.DataFrame(data)
#     df.insert(0, "Sr No", range(1, len(df)+1))
#     return df


# # =========================
# # RUN SCRIPT
# # =========================
# if __name__ == "__main__":

#     df = run_scraper(
#         role="tester",
#         skills="manual testing",
#         location="india",
#         limit=10,
#         extract_contact=True
#     )

#     df.to_excel("linkedin_data.xlsx", index=False)

#     print("🎉 Data saved to linkedin_data.xlsx")


















from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import pandas as pd


# =========================
# UTIL
# =========================
def random_delay():
    time.sleep(random.uniform(2, 4))


def clean_text(text):
    if not text:
        return ""
    return text.replace("Â·", "").replace("\n", " ").strip()


# =========================
# LOGIN DETECTION
# =========================
def wait_for_login(driver, timeout=120):
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            driver.find_element(By.XPATH, "//input[contains(@placeholder,'Search')]")
            return True
        except:
            time.sleep(2)

    raise Exception("Login timeout")


# =========================
# SCRAPER
# =========================
def run_scraper(role, skills, location, limit, extract_contact=True):

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.linkedin.com/login")
    wait_for_login(driver)

    # ONLY SKILL SEARCH
    search_url = f"https://www.linkedin.com/search/results/people/?keywords={skills}"
    driver.get(search_url)
    time.sleep(5)

    # SCROLL
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    elements = driver.find_elements(By.XPATH, "//a[contains(@href,'/in/')]")

    links = list(set([
        el.get_attribute("href").split("?")[0]
        for el in elements if el.get_attribute("href")
    ]))

    data = []

    for link in links[:limit]:

        driver.get(link)
        random_delay()

        # NAME
        try:
            name = clean_text(driver.find_element(By.XPATH, "//h1").text)
        except:
            name = ""

        # HEADLINE
        try:
            headline = clean_text(
                driver.find_element(By.XPATH, "//div[contains(@class,'text-body-medium')]").text
            )
        except:
            headline = ""

        # ABOUT
        about = ""
        try:
            try:
                driver.find_element(By.XPATH, "//button[contains(@aria-label,'See more about')]").click()
                time.sleep(1)
            except:
                pass

            about = clean_text(
                driver.find_element(
                    By.XPATH,
                    "//section[.//span[text()='About']]//div[contains(@class,'display-flex')]"
                ).text
            )
        except:
            pass

        # CONTACT
        email = ""
        phone = ""

        if extract_contact:
            try:
                driver.find_element(By.XPATH, "//a[contains(@href,'contact-info')]").click()
                time.sleep(2)

                # EMAIL
                try:
                    email = driver.find_element(
                        By.XPATH,
                        "//a[starts-with(@href,'mailto')]"
                    ).text.strip()
                except:
                    pass

                # PHONE
                try:
                    spans = driver.find_elements(By.XPATH, "//section[contains(@class,'pv-contact-info')]//span")
                    for el in spans:
                        txt = el.text.strip()
                        clean = txt.replace("+", "").replace(" ", "")
                        if clean.isdigit() and len(clean) >= 10:
                            phone = txt
                            break
                except:
                    pass

                # CLOSE
                try:
                    driver.find_element(By.XPATH, "//button[contains(@aria-label,'Dismiss')]").click()
                except:
                    pass

            except:
                pass

        data.append({
            "Name": name,
            "Headline": headline,
            "About": about,
            "Email": email,
            "Phone": phone,
            "Profile": link,
            "Status": ""
        })

        print("Scraped:", name)

    driver.quit()

    df = pd.DataFrame(data)
    df.insert(0, "Sr No", range(1, len(df) + 1))

    return df


# =========================
# SEND MESSAGE
# =========================
from selenium.webdriver.common.keys import Keys

def send_message(driver, profile_url, message):

    try:
        driver.get(profile_url)
        time.sleep(5)

        # Scroll (important)
        driver.execute_script("window.scrollTo(0, 300);")
        time.sleep(2)

        # FIND MESSAGE BUTTON (FIXED)
        message_buttons = driver.find_elements(
            By.XPATH,
            "//button[.//span[contains(@class,'artdeco-button__text') and normalize-space()='Message']]"
        )

        if not message_buttons:
            return "No Message Button"

        for button in message_buttons:
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                time.sleep(1)

                try:
                    button.click()
                except:
                    driver.execute_script("arguments[0].click();", button)

                time.sleep(3)

                # MESSAGE BOX (FIXED)
                msg_box = driver.find_element(
                    By.XPATH,
                    "//div[contains(@class,'msg-form__contenteditable')]"
                )

                msg_box.click()
                time.sleep(1)

                msg_box.clear()
                msg_box.send_keys(message)
                time.sleep(1)

                msg_box.send_keys(Keys.ENTER)

                time.sleep(2)

                return "Sent"

            except Exception as e:
                print("Loop error:", e)

        return "Failed"

    except Exception as e:
        print("Main error:", e)
        return "Failed"
# =========================
# BULK MESSAGING
# =========================
def send_bulk_messages(driver, df, role, location, template):

    statuses = []

    for _, row in df.iterrows():

        name = row["Name"]
        profile = row["Profile"]

        message = template.format(
            name=name,
            role=role,
            location=location
        )

        status = send_message(driver, profile, message)

        statuses.append(status)

        print(f"{name} → {status}")

        time.sleep(random.uniform(3, 6))

    df["Message Status"] = statuses
    return df
