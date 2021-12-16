import streamlit as st
from template import *


title = create_title("SWAT Ops JSON")

q1 = create_question_text("What is the project's ID?")

q2 = create_select_box("Where is the project located at?",
                        ["Singapore", "Malaysia", "Thailand"])

q3 = create_radio_buttons("Select the environment",
                            ["Staging", "Production"])

q4 = create_question_text("What is total number of waypoints?")


json_view = create_json_view("Display JSON",
                             ["Project ID", "Country", "Environment", "Nos of waypoints"],
                             [q1, q2, q3, q4])

