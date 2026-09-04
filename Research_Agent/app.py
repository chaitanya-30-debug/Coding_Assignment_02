import requests
from bs4 import BeautifulSoup
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")


def search_web(topic):
    url = "https://www.google.com/search"
    params = {"q": topic}

    response = requests.get(
        url,
        params=params,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.select("div"):
        text = result.get_text(" ", strip=True)

        if len(text) > 100:
            results.append(text)

        if len(results) >= 5:
            break

    return results


topic = input("Enter your research topic: ")

print("\nSearching for information...\n")

results = search_web(topic)

research = "\n\n".join(results)

prompt = f"""
You are a research assistant.

Research topic:
{topic}

Information collected:
{research}

Create a structured research report containing:

1. Introduction
2. Key Findings
3. Advantages
4. Challenges
5. Conclusion
6. References

Clearly separate each section.
"""

print("Generating report...\n")

report = llm.invoke(prompt)

print("=" * 60)
print("RESEARCH REPORT")
print("=" * 60)
print(report)
with open("research_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nReport saved as research_report.txt")python app.py
