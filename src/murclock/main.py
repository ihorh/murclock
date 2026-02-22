from __future__ import annotations

import zoneinfo
from datetime import datetime
from typing import TYPE_CHECKING

import streamlit as st

if TYPE_CHECKING:
    from collections.abc import Sequence

st.set_page_config(page_title="Clock", layout="centered")

st.image("images/image.png")

st.title("MurClock")

r"""
Here will wll later add a clock and time operations.

Wait for updates!
"""


st.header("The Clock")


@st.cache_data
def get_timezones() -> Sequence[str]:
    return sorted(zoneinfo.available_timezones())


@st.fragment(run_every=1)
def fr_clock_autorefresh(tz: zoneinfo.ZoneInfo | None = None) -> None:
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

tzname = st.selectbox("Choose your timezone 🕑", get_timezones())
tz = zoneinfo.ZoneInfo(tzname)

fr_clock_autorefresh(tz)
