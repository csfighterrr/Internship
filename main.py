import streamlit as st
from datetime import datetime
from streamlit_calendar import calendar

# Set page title
st.title('Calendar App')

# Calendar configuration
calendar_options = {
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridMonth,timeGridWeek,timeGridDay",
    },
    "initialView": "dayGridMonth",
    "selectable": True,
    "selectMirror": True,
    "dayMaxEvents": True,
    "weekNumbers": True,
    "navLinks": True,
}

# Display the calendar
calendar = calendar(events=[], options=calendar_options, key="calendar")

# Show selected date info if a date was clicked
if calendar.get("dateClick"):
    clicked_date = datetime.fromisoformat(calendar.get("dateClick")["date"])
    st.write("Selected date:", clicked_date.strftime("%Y-%m-%d"))