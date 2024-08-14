import streamlit as st
import pandas as pd
from datetime import datetime


def auto_refresh(interval_ms):
    js_code = f"""
        <script>
        setInterval(function() {{
            window.location.reload();
        }}, {interval_ms});
        </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)

date = datetime.now().strftime("%d-%m-%Y")


count = 0


if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")


try:
    df = pd.read_csv(f"Attendance/Attendance_{date}.csv")
    st.dataframe(df.style.highlight_max(axis=0))
except FileNotFoundError:
    st.write("File not found. No attendance data available for today.")


auto_refresh(2000)
