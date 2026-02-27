# import streamlit as st
# import pandas as pd
# from scraper import run_scraper

# st.set_page_config(page_title="AI Recruiter Tool", layout="wide")

# st.title("🚀 AI Recruiter Automation Tool")

# # Inputs
# role = st.text_input("Job Role")
# skills = st.text_input("Skills (comma separated)")
# location = st.text_input("Location")
# limit = st.number_input("Number of candidates", 1, 30, 10)

# extract_contact = st.checkbox("Extract Contact Info (if available)")

# if "data" not in st.session_state:
#     st.session_state.data = None


# if st.button("🚀 Start Scraping"):

#     if not skills:
#         st.error("Enter skills")
#     else:
#         with st.spinner("Scraping..."):
#             df = run_scraper(role, skills, location, limit, extract_contact=True)

#         st.session_state.data = df


# # =========================
# # SHOW DATA IF EXISTS
# # =========================
# if st.session_state.data is not None:

#     df = st.session_state.data

#     st.success("✅ Data Ready")
#     st.dataframe(df)
#     st.dataframe(df, hide_index=True)
#     st.download_button(
#         label="📥 Download Excel",
#         data=df.to_csv(index=False),
#         file_name="linkedin_data.csv",
#         mime="text/csv"
#     )










# import streamlit as st
# import pandas as pd
# from scraper import run_scraper, wait_for_login, send_bulk_messages
# from selenium import webdriver


# st.set_page_config(layout="wide")

# st.title("🚀 LinkedIn Hiring Bot")

# # SESSION STATE
# if "data" not in st.session_state:
#     st.session_state.data = None


# # =========================
# # INPUTS
# # =========================
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     role = st.text_input("Role", "Python Developer")

# with col2:
#     skills = st.text_input("Skills", "python")

# with col3:
#     location = st.text_input("Location", "India")

# with col4:
#     limit = st.number_input("Limit", 5)


# # =========================
# # SCRAPER BUTTON
# # =========================
# if st.button("🔍 Run Scraper"):

#     with st.spinner("Scraping... Login in browser"):
#         df = run_scraper(role, skills, location, limit)

#         st.session_state.data = df

#     st.success("Scraping Done ✅")


# # =========================
# # SHOW DATA
# # =========================
# # if st.session_state.data is not None:
# #     st.dataframe(st.session_state.data, use_container_width=True, hide_index=True)


# # =========================
# # EDIT + DELETE TABLE
# # =========================



# import streamlit as st
# import pandas as pd
# from scraper import run_scraper, wait_for_login, send_bulk_messages
# from selenium import webdriver


# st.set_page_config(layout="wide")

# st.title("🚀 LinkedIn Hiring Bot")

# # SESSION STATE
# if "data" not in st.session_state:
#     st.session_state.data = None


# # =========================
# # INPUTS
# # =========================
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     role = st.text_input("Role", "Python Developer")

# with col2:
#     skills = st.text_input("Skills", "python")

# with col3:
#     location = st.text_input("Location", "India")

# with col4:
#     limit = st.number_input("Limit", 5)


# # =========================
# # SCRAPER BUTTON
# # =========================
# if st.button("🔍 Run Scraper"):

#     with st.spinner("Scraping... Login in browser"):
#         df = run_scraper(role, skills, location, limit)

#         st.session_state.data = df

#     st.success("Scraping Done ✅")


# # =========================
# # SHOW DATA
# # =========================
# # if st.session_state.data is not None:
# #     st.dataframe(st.session_state.data, use_container_width=True, hide_index=True)


# # =========================
# # EDIT + DELETE TABLE
# # =========================
# if st.session_state.data is not None:

#     st.subheader("📋 Edit Profiles (Delete unwanted)")

#     df = st.session_state.data.copy()

#     # Add Delete column if not exists
#     if "Delete" not in df.columns:
#         df["Delete"] = False

#     edited_df = st.data_editor(
#         df,
#         use_container_width=True,
#         num_rows="dynamic"
#     )

#     # Remove deleted rows
#     cleaned_df = edited_df[edited_df["Delete"] == False].drop(columns=["Delete"])

#     # Reset index + Sr No
#     cleaned_df.reset_index(drop=True, inplace=True)
#     # Remove existing Sr No if present
#     if "Sr No" in cleaned_df.columns:
#         cleaned_df = cleaned_df.drop(columns=["Sr No"])

#     # Add fresh Sr No
#     cleaned_df.insert(0, "Sr No", range(1, len(cleaned_df) + 1))

#     # Save updated data
#     st.session_state.data = cleaned_df

# # =========================
# # DOWNLOAD
# # =========================
# from io import BytesIO

# if st.session_state.data is not None:

#     buffer = BytesIO()
#     st.session_state.data.to_excel(buffer, index=False, engine='openpyxl')
#     buffer.seek(0)

#     st.download_button(
#         label="⬇ Download Excel",
#         data=buffer,
#         file_name="linkedin_data.xlsx",
#         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#     )

# # =========================
# # MESSAGE TEMPLATE
# # =========================
# st.subheader("✉ Message Template")

# message_template = st.text_area(
#     "Edit Message",
#     value="Hi {name},\nWe are hiring for {role} in {location}. Are you interested?"
# )


# # =========================
# # SEND BUTTON
# # =========================
# if st.button("📨 Send Messages"):

#     if st.session_state.data is None:
#         st.error("Run scraper first")
#     else:
#         with st.spinner("Login again & sending messages..."):

#             driver = webdriver.Chrome()
#             driver.maximize_window()

#             driver.get("https://www.linkedin.com/login")
#             wait_for_login(driver)

#             df = send_bulk_messages(
#                 driver,
#                 st.session_state.data,
#                 role,
#                 location,
#                 message_template
#             )

#             driver.quit()

#             st.session_state.data = df

#         st.success("Messages sent ✅")
#         st.dataframe(df, hide_index=True)

# # =========================
# # DOWNLOAD
# # =========================
# from io import BytesIO

# if st.session_state.data is not None:

#     buffer = BytesIO()
#     st.session_state.data.to_excel(buffer, index=False, engine='openpyxl')
#     buffer.seek(0)

#     st.download_button(
#         label="⬇ Download Excel",
#         data=buffer,
#         file_name="linkedin_data.xlsx",
#         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#     )

# # =========================
# # MESSAGE TEMPLATE
# # =========================
# st.subheader("✉ Message Template")

# message_template = st.text_area(
#     "Edit Message",
#     value="Hi {name},\nWe are hiring for {role} in {location}. Are you interested?"
# )


# # =========================
# # SEND BUTTON
# # =========================
# if st.button("📨 Send Messages"):

#     if st.session_state.data is None:
#         st.error("Run scraper first")
#     else:
#         with st.spinner("Login again & sending messages..."):

#             driver = webdriver.Chrome()
#             driver.maximize_window()

#             driver.get("https://www.linkedin.com/login")
#             wait_for_login(driver)

#             df = send_bulk_messages(
#                 driver,
#                 st.session_state.data,
#                 role,
#                 location,
#                 message_template
#             )

#             driver.quit()

#             st.session_state.data = df

#         st.success("Messages sent ✅")
#         st.dataframe(df, hide_index=True)

































































# import streamlit as st
# import pandas as pd
# from scraper import run_scraper, wait_for_login, send_bulk_messages
# from selenium import webdriver
# from io import BytesIO

# st.set_page_config(layout="wide")

# st.title("🚀 LinkedIn Hiring Bot")

# # =========================
# # SESSION STATE
# # =========================
# if "data" not in st.session_state:
#     st.session_state.data = None


# # =========================
# # INPUTS
# # =========================
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     role = st.text_input("Role", "Python Developer", key="role")

# with col2:
#     skills = st.text_input("Skills", "python", key="skills")

# with col3:
#     location = st.text_input("Location", "India", key="location")

# with col4:
#     limit = st.number_input("Limit", 5, key="limit")


# # =========================
# # SCRAPER
# # =========================
# if st.button("🔍 Run Scraper"):

#     with st.spinner("Scraping... Login in browser"):
#         df = run_scraper(role, skills, location, limit)
#         st.session_state.data = df

#     st.success("Scraping Done ✅")


# # =========================
# # EDIT + DELETE TABLE
# # =========================
# if st.session_state.data is not None:

#     st.subheader("📋 Edit Profiles (Delete unwanted)")

#     df = st.session_state.data.copy()

#     # Ensure Delete column exists
#     if "Delete" not in df.columns:
#         df["Delete"] = False

#     edited_df = st.data_editor(
#         df,
#         use_container_width=True,
#         num_rows="dynamic",
#         key="data_editor"
#     )

#     # Apply delete filter
#     cleaned_df = edited_df[edited_df["Delete"] == False].drop(columns=["Delete"])

#     # Reset index
#     cleaned_df.reset_index(drop=True, inplace=True)

#     # Add Sr No cleanly
#     if "Sr No" in cleaned_df.columns:
#         cleaned_df = cleaned_df.drop(columns=["Sr No"])

#     cleaned_df.insert(0, "Sr No", range(1, len(cleaned_df) + 1))

#     # Save back
#     st.session_state.data = cleaned_df


# # =========================
# # DOWNLOAD
# # =========================
# if st.session_state.data is not None:

#     buffer = BytesIO()
#     st.session_state.data.to_excel(buffer, index=False, engine='openpyxl')
#     buffer.seek(0)

#     st.download_button(
#         label="⬇ Download Excel",
#         data=buffer,
#         file_name="linkedin_data.xlsx",
#         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#         key="download_btn"
#     )


# # =========================
# # MESSAGE TEMPLATE
# # =========================
# st.subheader("✉ Message Template")

# message_template = st.text_area(
#     "Edit Message",
#     value="Hi {name},\nWe are hiring for {role} in {location}. Are you interested?",
#     key="msg_template"
# )


# # =========================
# # SEND MESSAGES
# # =========================
# if st.button("📨 Send Messages", key="send_btn"):

#     if st.session_state.data is None:
#         st.error("Run scraper first")
#     else:
#         with st.spinner("Login again & sending messages..."):

#             driver = webdriver.Chrome()
#             driver.maximize_window()

#             driver.get("https://www.linkedin.com/login")
#             wait_for_login(driver)

#             df = send_bulk_messages(
#                 driver,
#                 st.session_state.data,
#                 role,
#                 location,
#                 message_template
#             )

#             driver.quit()

#             st.session_state.data = df

#         st.success("Messages sent ✅")
#         st.dataframe(df, use_container_width=True, hide_index=True)




























# import streamlit as st
# import pandas as pd
# from scraper import run_scraper, wait_for_login, send_bulk_messages
# from selenium import webdriver
# from io import BytesIO

# st.set_page_config(layout="wide")

# st.title("🚀 LinkedIn Hiring Bot")

# # =========================
# # SESSION STATE
# # =========================
# if "data" not in st.session_state:
#     st.session_state.data = None


# # =========================
# # INPUTS
# # =========================
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     role = st.text_input("Role", "Python Developer", key="role")

# with col2:
#     skills = st.text_input("Skills", "python", key="skills")

# with col3:
#     location = st.text_input("Location", "India", key="location")

# with col4:
#     limit = st.number_input("Limit", 5, key="limit")


# # =========================
# # SCRAPER
# # =========================
# # if st.button("🔍 Run Scraper", key="scraper_btn"):

# #     with st.spinner("Scraping... Login in browser"):
# #         df = run_scraper(role, skills, location, limit)

# #         df = df.reset_index(drop=True)
# #         df.insert(0, "Sr No", range(1, len(df) + 1))

# #         st.session_state.data = df

# #     st.success("Scraping Done ✅")

# if st.button("🔍 Run Scraper", key="scraper_btn"):

#     with st.spinner("Scraping... Login in browser"):
#         df = run_scraper(role, skills, location, limit)

#         # 🔥 FIX: remove Sr No if already exists
#         if "Sr No" in df.columns:
#             df = df.drop(columns=["Sr No"])

#         df = df.reset_index(drop=True)
#         df.insert(0, "Sr No", range(1, len(df) + 1))

#         st.session_state.data = df

#     st.success("Scraping Done ✅")

# # =========================
# # TABLE WITH ❌ AT END
# # =========================
# # =========================
# # DELETE WITH ❌ BUTTON
# # =========================
# if st.session_state.data is not None:

#     st.subheader("📋 Profiles (Click ❌ to delete)")

#     df = st.session_state.data.copy()

#     # Loop through rows
#     for i, row in df.iterrows():

#         cols = st.columns([4, 4, 4, 2, 1])  # adjust layout if needed

#         cols[0].write(row.get("Name", ""))
#         cols[1].write(row.get("Headline", ""))
#         cols[2].write(row.get("Location", ""))
#         cols[3].write(row.get("Profile", ""))

#         # ❌ Delete button
#         if cols[4].button("❌", key=f"delete_{i}"):

#             df = df.drop(index=i).reset_index(drop=True)

#             st.session_state.data = df
#             st.rerun()


# # =========================
# # DOWNLOAD
# # =========================
# if st.session_state.data is not None:

#     buffer = BytesIO()
#     st.session_state.data.to_excel(buffer, index=False, engine="openpyxl")
#     buffer.seek(0)

#     st.download_button(
#         label="⬇ Download Excel",
#         data=buffer,
#         file_name="linkedin_data.xlsx",
#         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#         key="download_btn"
#     )


# # =========================
# # MESSAGE TEMPLATE
# # =========================
# st.subheader("✉ Message Template")

# message_template = st.text_area(
#     "Edit Message",
#     value="Hi {name},\nWe are hiring for {role} in {location}. Are you interested?",
#     key="msg_template"
# )


# # =========================
# # SEND MESSAGES
# # =========================
# if st.button("📨 Send Messages", key="send_btn"):

#     if st.session_state.data is None:
#         st.error("Run scraper first")
#     else:
#         with st.spinner("Login again & sending messages..."):

#             driver = webdriver.Chrome()
#             driver.maximize_window()

#             driver.get("https://www.linkedin.com/login")
#             wait_for_login(driver)

#             df = send_bulk_messages(
#                 driver,
#                 st.session_state.data,
#                 role,
#                 location,
#                 message_template
#             )

#             driver.quit()

#             st.session_state.data = df

#         st.success("Messages sent ✅")
#         st.dataframe(df, use_container_width=True, hide_index=True)


























import streamlit as st
import pandas as pd
from scraper import run_scraper, wait_for_login, send_bulk_messages
from selenium import webdriver
from io import BytesIO

st.set_page_config(layout="wide")

st.title("🚀 LinkedIn Hiring Bot")

# =========================
# SESSION STATE
# =========================
if "data" not in st.session_state:
    st.session_state.data = None


# =========================
# INPUTS
# =========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    role = st.text_input("Role", "Python Developer", key="role")

with col2:
    skills = st.text_input("Skills", "python", key="skills")

with col3:
    location = st.text_input("Location", "India", key="location")

with col4:
    limit = st.number_input("No. of Candidates", min_value=1, value=5, key="limit")


# =========================
# RUN SCRAPER
# =========================
if st.button("🔍 Run Scraper", key="scraper_btn"):

    with st.spinner("Scraping... Login in browser"):
        df = run_scraper(role, skills, location, limit)

        # Clean dataframe
        df = df.reset_index(drop=True)

        # Remove Sr No if exists (safe fix)
        if "Sr No" in df.columns:
            df = df.drop(columns=["Sr No"])

        st.session_state.data = df

    st.success("Scraping Done ✅")


# =========================
# PREVIEW + DELETE ROW
# =========================
if st.session_state.data is not None:

    st.subheader("📋 Profiles (Click ❌ to delete)")

    df = st.session_state.data.copy()

    for i in range(len(df)):
        row = df.iloc[i]

        cols = st.columns([3, 4, 3, 3, 1])

        cols[0].write(f"**{row.get('Name','')}**")
        cols[1].write(row.get("Headline", ""))
        cols[2].write(row.get("Location", ""))
        cols[3].write(row.get("Profile", ""))

        # ✅ UNIQUE KEY FIX (important)
        if cols[4].button("❌", key=f"delete_btn_{i}"):

            df = df.drop(index=i).reset_index(drop=True)

            # update session
            st.session_state.data = df

            st.rerun()


# =========================
# DOWNLOAD
# =========================
if st.session_state.data is not None:

    buffer = BytesIO()
    st.session_state.data.to_excel(buffer, index=False, engine="openpyxl")
    buffer.seek(0)

    st.download_button(
        label="⬇ Download Excel",
        data=buffer,
        file_name="linkedin_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key="download_btn"
    )


# =========================
# MESSAGE TEMPLATE
# =========================
st.subheader("✉ Message Template")

message_template = st.text_area(
    "Edit Message",
    value="Hi {name},\nWe are hiring for {role} in {location}. Are you interested?",
    key="msg_template"
)


# =========================
# SEND MESSAGES
# =========================
if st.button("📨 Send Messages", key="send_btn"):

    if st.session_state.data is None:
        st.error("Run scraper first")
    else:
        with st.spinner("Login again & sending messages..."):

            driver = webdriver.Chrome()
            driver.maximize_window()

            driver.get("https://www.linkedin.com/login")
            wait_for_login(driver)

            df = send_bulk_messages(
                driver,
                st.session_state.data,
                role,
                location,
                message_template
            )

            driver.quit()

            st.session_state.data = df

        st.success("Messages sent ✅")
        st.dataframe(df, use_container_width=True, hide_index=True)
