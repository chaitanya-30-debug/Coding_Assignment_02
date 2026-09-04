from langchain_ollama import OllamaLLM

# Connect to AI model
llm = OllamaLLM(model="llama3.2")


# Agent 1: Research Agent
def research_agent(topic):
    prompt = f"""
    You are a Research Agent.

    Research topic:
    {topic}

    Give a short explanation of:
    - What it is
    - Important facts
    - Advantages
    - Challenges
    """
    return llm.invoke(prompt)


# Agent 2: Security Agent
def security_agent(topic, research):
    prompt = f"""
    You are a Cybersecurity Agent.

    Topic:
    {topic}

    Research information:
    {research}

    Analyze the cybersecurity risks related to this topic.
    Give:
    - Potential threats
    - Severity
    - Security recommendations
    """
    return llm.invoke(prompt)


# Agent 3: Report Agent
def report_agent(topic, research, security):
    prompt = f"""
    You are a Report Agent.

    Topic:
    {topic}

    Research Agent findings:
    {research}

    Security Agent findings:
    {security}

    Create a final structured report with:
    1. Introduction
    2. Research Findings
    3. Security Threats
    4. Security Recommendations
    5. Conclusion
    """
    return llm.invoke(prompt)


# Main program
topic = input("Enter a topic: ")

print("\nResearch Agent working...")
research = research_agent(topic)

print("\nSecurity Agent working...")
security = security_agent(topic, research)

print("\nReport Agent working...")
final_report = report_agent(topic, research, security)

print("\n" + "=" * 60)
print("FINAL MULTI-AGENT REPORT")
print("=" * 60)
print(final_report)
