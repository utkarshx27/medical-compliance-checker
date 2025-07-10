import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)

# Define response schema
class ComplianceResponse(BaseModel):
    classification: str
    explanation: Optional[str] = None


# FDA compliance system message
system_prompt = SystemMessage(
    content=(
        "You are an FDA compliance checker that strictly evaluates medical product claims. "
        "You classify each input as either 'Compliant' or 'Non-compliant' based on U.S. FDA regulations, advertising standards, and promotional labeling rules. "
        "Do not ask follow-up questions. Your response must be a single word: either 'Compliant' or 'Non-compliant' [brief explanation].\n\n"
        "If Non-compliant, then provide a brief explanation. "
        "Classify as Non-compliant if any of the following conditions are met:\n"
        "1. The claim promotes off-label use (e.g., unapproved conditions, dosages, patient groups, or administration routes).\n"
        "2. The claim makes superiority claims (e.g., 'better than competitors') without direct comparative study evidence.\n"
        "3. The benefits are mentioned without disclosing risks or side effects (lack of fair balance).\n"
        "4. The claim uses vague testimonials or anecdotes without clinical substantiation (e.g., 'miraculous recovery').\n"
        "5. The claim includes misleading or false statements, or implies FDA endorsement inappropriately.\n"
        "6. The claim appears in a direct-to-consumer context and omits risk disclosures for prescription drugs.\n"
        "7. The claim is on social media and promotes or amplifies off-label use (e.g., company 'likes' or retweets misleading content).\n"
        "8. The claim uses absolute, exaggerated, or unverifiable phrases (e.g., 'guaranteed', '100%', 'cures all', 'best').\n"
        "9. The claim lacks proper substantiation from peer-reviewed clinical trials or regulatory labeling.\n\n"
        "If a clinical study is mentioned and it quantifies the claim (e.g., success rate, effectiveness) without exaggeration, classify as Compliant. "
        "Classify as Compliant if the claim is truthful, evidence-based, and consistent with FDA-approved indications, while presenting both benefits and risks fairly, and complying with promotional standards. "
        "Return your response in exactly this JSON format:\n"
        "{\n"
        '  "classification": "Compliant" or "Non-compliant",\n'
        '  "explanation": "Reason for non-compliance (optional, only if non-compliant)"\n'
        "}"
    )
)

# Streamlit UI
st.title("Medical Claim Compliance Checker")
st.subheader("Agency: US (FDA)")
st.text(" ")
user_input = st.text_area("Enter a medical product claim:")

if st.button("Check Compliance"):
    if user_input.strip() == "":
        st.warning("Please enter a medical claim before submitting.")
    else:
        # Create human message
        messages = [system_prompt, HumanMessage(content=user_input)]
        
        # Invoke LLM
        response = llm.invoke(messages)
        
        # Show formatted JSON result
        st.subheader("Medical Compliance Checker")
        try:
            result = ComplianceResponse.model_validate_json(response.content)
            classification = result.classification
            explanation = result.explanation

            # Styled classification badge
            color = "#28a745" if classification.lower() == "compliant" else "#dc3545"
            badge_html = f"""
            <div style="display:inline-block;padding:0.4em 0.8em;border-radius:0.5rem;
                        background-color:{color};color:white;font-weight:bold;font-size:1.2rem;">
                {classification}
            </div>
            """
            st.markdown(badge_html, unsafe_allow_html=True)

            # Optional explanation
            if explanation:
                st.markdown("#### 📝 Explanation")
                st.markdown(f"<div style='font-size:1rem;color:#333;padding:0.5em 0.8em;background-color:#f8f9fa;border-radius:0.4rem;'>{explanation}</div>", unsafe_allow_html=True)

        except Exception:
            st.error("Error parsing LLM response. Raw output below:")
            st.text(response.content)

