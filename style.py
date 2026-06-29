CUSTOM_CSS = """
<style>

/* ===========================
   Background
=========================== */

.stApp {
    background: linear-gradient(135deg,#050816,#10172b);
    color: white;
}

/* ===========================
   Header
=========================== */

header{
    visibility:hidden;
}

/* ===========================
   Top Padding
=========================== */

.block-container{
    padding-top:0.5rem;
}

/* ===========================
   Title
=========================== */

h1{
    text-align:center;
    color:#00ff99;
    font-weight:bold;
}

h2,h3{
    color:#5de4ff;
}

/* ===========================
   Text Input
=========================== */

.stTextInput input{
    border-radius:12px;
    border:2px solid #00ff99;
    background:#10172b;
    color:white !important;
}

/* ===========================
   Buttons
=========================== */

.stButton>button{
    width:100%;
    border-radius:12px;
    border:none;
    background:#00c853;
    color:white;
    font-weight:bold;
    padding:12px;
    transition:0.3s;
}

.stButton>button:hover{
    background:#00e676;
    transform:scale(1.03);
}

/* ===========================
   Progress Bar
=========================== */

.stProgress > div > div > div{
    background:#00ff99;
}

/* ===========================
   Metric Card
=========================== */

div[data-testid="metric-container"]{
    border-radius:15px;
    border:1px solid #00ff99;
    padding:10px;
    background:#111827;
}

/* Metric Text */

div[data-testid="metric-container"] *{
    color:white !important;
}

/* ===========================
   Info / Success / Warning
=========================== */

div[data-testid="stInfo"]{
    background:#111827;
    color:white !important;
}

div[data-testid="stInfo"] *{
    color:white !important;
}

div[data-testid="stSuccess"] *{
    color:white !important;
}

div[data-testid="stWarning"] *{
    color:white !important;
}

div[data-testid="stAlert"]{
    border-radius:12px;
}

/* ===========================
   Slider
=========================== */

.stSlider{
    padding-top:10px;
}

/* ===========================
   Footer
=========================== */

footer{
    visibility:hidden;
}
/* ===========================
   White Text Fix
=========================== */

/* Metric */
div[data-testid="metric-container"] label,
div[data-testid="metric-container"] div,
div[data-testid="metric-container"] span,
div[data-testid="metric-container"] p{
    color:white !important;
}

/* Info Box */
div[data-testid="stInfo"]{
    color:white !important;
}

div[data-testid="stInfo"] *{
    color:white !important;
}

/* Warning Box */
div[data-testid="stWarning"]{
    color:white !important;
}

div[data-testid="stWarning"] *{
    color:white !important;
}
</style>
"""