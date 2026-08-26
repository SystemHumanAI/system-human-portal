import os
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from google import genai

# Load custom icon
favicon = Image.open("favicon-96x96.png")

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SYSTEM HUMAN // Operations Portal",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GOOGLE ANALYTICS ---
components.html(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-C1H5BSKMFH"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-C1H5BSKMFH');
    </script>
    """,
    height=0,
    width=0
)

# --- BESPOKE SYSTEM HUMAN STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;800&family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    code, pre, .stCodeBlock {
        font-family: 'JetBrains Mono', monospace !important;
    }
    .stApp {
        background-color: #0b0d11;
        color: #e6edf3;
    }
    header, footer {visibility: hidden;}
    .main-header {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: -0.05em;
        color: #ffffff;
        border-bottom: 1px solid #21262d;
        padding-bottom: 0.75rem;
        margin-bottom: 1.5rem;
    }
    .badge {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        font-size: 0.75rem;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 600;
        border-radius: 4px;
        background-color: #161b22;
        border: 1px solid #30363d;
        color: #58a6ff;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- GEMINI CLIENT SETUP ---
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

def generate_output(prompt: str):
    if not api_key:
        st.error("API Key missing. Add GEMINI_API_KEY to Railway Variables or enter it in the sidebar.")
        return
    try:
        client = genai.Client(api_key=api_key)
        with st.spinner("Executing operational agent pipeline..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            st.markdown(response.text)
    except Exception as e:
        st.error(f"Execution failed: {str(e)}")

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("### SYSTEM HUMAN // OS")
st.sidebar.caption("Autonomous AI Infrastructure Suite")

selected_agent = st.sidebar.radio(
    "Select Engine:",
    [
        "01 // Vendor Invoice Auditor",
        "02 // Inbound Lead Qualifier",
        "03 // Discovery & SOW Extractor",
        "04 // Policy & Compliance RAG",
        "05 // Customer Escalation Triage"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("**Environment:** `Production / Live`")
st.sidebar.markdown("**Endpoint:** `systemhuman.co.uk`")

# --- ROUTING LOGIC ---

if "01 // Vendor Invoice Auditor" in selected_agent:
    st.markdown('<div class="main-header">SYSTEM HUMAN // 01. VENDOR INVOICE & CONTRACT AUDITOR</div>', unsafe_allow_html=True)
    st.markdown('<span class="badge">AP LEAK DETECTION & DISCREPANCY PARSER</span>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        invoice_text = st.text_area("Paste Raw Invoice Data / OCR Text:", height=200, placeholder="Vendor: Apex Supplies\nLine 1: 50x Pallet wrap - £1,200...")
    with col2:
        contract_text = st.text_area("Paste Governing Master Services Agreement (MSA) Clauses:", height=200, placeholder="Clause 4.2: Maximum unit price for pallet wrap fixed at £18.00...")
    
    if st.button("Run Invoice Audit Pipeline"):
        prompt = f"""
        You are the Chief Financial Auditor for SYSTEM HUMAN (systemhuman.co.uk).
        Analyze this invoice against the contract terms.

        ### INVOICE DATA:
        {invoice_text}

        ### CONTRACT CLAUSES:
        {contract_text}

        Generate a structured audit report detailing:
        1. Executive Invoice Summary
        2. Detected Discrepancies & Leaks (Table format with line items)
        3. Financial Impact & Recovery Calculation
        4. Remediation Email to Vendor Accounts Payable
        """
        generate_output(prompt)

elif "02 // Inbound Lead Qualifier" in selected_agent:
    st.markdown('<div class="main-header">SYSTEM HUMAN // 02. B2B INBOUND LEAD ENRICHER & QUALIFIER</div>', unsafe_allow_html=True)
    st.markdown('<span class="badge">COMMERCIAL TRIAGE & SOW FIT SCORING</span>', unsafe_allow_html=True)
    
    inquiry = st.text_area("Paste Inbound Message / Form Submission:", height=180, placeholder="Hi James, saw your post on LinkedIn. We are running 40 HGVs and spend 25 hrs/week matching invoices...")
    
    if st.button("Score & Triage Lead"):
        prompt = f"""
        You are the Chief Commercial Architect for SYSTEM HUMAN (systemhuman.co.uk).
        Evaluate and score this inbound lead inquiry:

        {inquiry}

        Generate:
        1. Prospect & Company Dossier
        2. Qualification Scorecard (Fit Score /100, Tier, Feasibility, Target Budget)
        3. Actionable Strategy & System Angle
        4. Tailored Executive Outreach Draft (From James Lewis)
        """
        generate_output(prompt)

elif "03 // Discovery & SOW Extractor" in selected_agent:
    st.markdown('<div class="main-header">SYSTEM HUMAN // 03. AUTONOMOUS DISCOVERY & SOW EXTRACTOR</div>', unsafe_allow_html=True)
    st.markdown('<span class="badge">TRANSCRIPT TO STATEMENT OF WORK PARSER</span>', unsafe_allow_html=True)
    
    transcript = st.text_area("Paste Raw Discovery Notes / Meeting Transcript:", height=200, placeholder="Discovery call with Sarah Jenkins, Crestline Property Management. Managing 320 leases...")
    
    if st.button("Generate Statement of Work"):
        prompt = f"""
        You are the Lead Solutions Architect at SYSTEM HUMAN (systemhuman.co.uk).
        Transform these discovery notes into an enterprise-grade Statement of Work (SOW):

        {transcript}

        Include:
        1. Executive Brief & KPIs
        2. System Architecture & Stack (Ascii diagram)
        3. Milestone Scope (Phase 1-3)
        4. Scope Boundaries & Out of Scope Guardrails
        5. Commercial Summary & Pricing
        """
        generate_output(prompt)

elif "04 // Policy & Compliance RAG" in selected_agent:
    st.markdown('<div class="main-header">SYSTEM HUMAN // 04. MULTI-DOC POLICY & COMPLIANCE VALIDATOR</div>', unsafe_allow_html=True)
    st.markdown('<span class="badge">CLAUSE-GROUNDED OPERATIONAL AUDITING</span>', unsafe_allow_html=True)
    
    policy_input = st.text_area("Policy Context / Guidelines:", height=150, placeholder="Section 3.1: Max allowable regional hotel cap is £130/night ex VAT...")
    question = st.text_area("Employee Inquiry / Expense Submission:", height=100, placeholder="Can I expense a last-minute hotel in Manchester for £165 and 2 beers?")
    
    if st.button("Run Compliance Cross-Examination"):
        prompt = f"""
        You are the Chief Compliance Officer at SYSTEM HUMAN (systemhuman.co.uk).
        Audit this inquiry against the policy context:

        ### POLICY:
        {policy_input}

        ### INQUIRY:
        {question}

        Generate:
        1. Compliance Determination (Status, Confidence, Risk Level)
        2. Clause-by-Clause Audit Citations
        3. Executive Verdict & Required Recovery Steps
        4. Internal Audit Log Entry
        """
        generate_output(prompt)

elif "05 // Customer Escalation Triage" in selected_agent:
    st.markdown('<div class="main-header">SYSTEM HUMAN // 05. ESCALATION & INCIDENT TRIAGE ENGINE</div>', unsafe_allow_html=True)
    st.markdown('<span class="badge">INCIDENT COMMAND & ARR CHURN DEFENSE</span>', unsafe_allow_html=True)
    
    escalation_text = st.text_area("Customer Complaint / Outage Ticket:", height=180, placeholder="Subject: UNACCEPTABLE - Automated sync failed again. We are pulling our £2,200/mo retainer...")
    
    if st.button("Triage Incident"):
        prompt = f"""
        You are the Incident Commander at SYSTEM HUMAN (systemhuman.co.uk).
        Triage this critical customer escalation:

        {escalation_text}

        Generate:
        1. Incident & Sentiment Dossier (P1-P3 Priority, Root Failure)
        2. Root Cause Category & Revenue at Risk (ARR)
        3. Internal Remediation & Target Resolution SLA
        4. Executive De-Escalation Draft from James Lewis
        """
        generate_output(prompt)
