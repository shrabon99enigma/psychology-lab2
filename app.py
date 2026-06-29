import streamlit as st
import random
import time

from habits import MOBILE_HABITS
from verdict import get_score, get_verdict
from scanner import fake_scan
from style import apply_theme
apply_theme()