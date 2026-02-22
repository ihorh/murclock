from __future__ import annotations

from datetime import datetime, timezone

import streamlit as st

st.set_page_config(page_title="Clock", layout="centered")

st.image("images/image.png")

st.title("MurClock")

r"""
Here will wll later add a clock and time operations.

Wait for updates!
"""


st.header("The Clock")


@st.fragment(run_every=1)
def fr_clock_autorefresh(tz: timezone | None = None) -> None:
    now = datetime.now(tz=tz)
    now_str = now.strftime("%H:%M:%S")
    st.markdown(
        f"""
    <div
        style="font-size:60px; text-align:center; font-family:  'Fira Code', monospace; font-variant-numeric: tabular-nums; letter-spacing: 4px; color: green;"
    >
        {now_str}
    </div>
    """,
        unsafe_allow_html=True,
    )


st.title("Current Time")

fr_clock_autorefresh()
