# 🧠 AI Prompt Library — Generative AI & LangChain

**Author:** Baibhab

**Project:** Level 1 — Prompt Library Curation

**Focus:** Prompts for Generative AI applications using LangChain and LLMs

---

## 🧭 Overview

This document curates a structured collection of **effective AI prompts** developed and tested while learning **Generative AI and LangChain**.
Each prompt demonstrates how to leverage LLMs for programming, writing, productivity, and learning tasks.

Each entry includes:

* **Prompt pattern**
* **Use case**
* **Effectiveness rating (⭐ to ⭐⭐⭐⭐⭐)**
* **Example input/output**
* **Customization tips and best practices**

---

## ⚙️ 1. Coding & Development

### 💻 Code Generation

**Prompt:**

> Act as an experienced **Python & LangChain developer**.
> Write a script that **connects a LangChain LLM with an OpenAI API key**, takes user input, and returns model-generated responses.
> Include error handling and modular structure following **PEP8** standards.

**Use Case:** Rapidly generating LangChain pipeline code.
**Effectiveness:** ⭐⭐⭐⭐⭐

**Example Output:**

```python
from langchain.llms import OpenAI

def generate_response(prompt):
    try:
        llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        return llm(prompt)
    except Exception as e:
        return f"Error: {str(e)}"

print(generate_response("Explain Generative AI in 3 lines"))
```

**Tips:**

* Replace model name with `"gpt-4"` for better performance.
* Use in Jupyter for testing modularly.

**Best Practices:**
Always validate API key and handle exceptions gracefully.

---

### 🐞 Bug Fixing

**Prompt:**

> Analyze this Python code for LangChain and identify logical or syntax bugs.
> Explain each issue and rewrite corrected code:
>
> ```python
> llm = OpenAI(model="gpt-4")
> print(llm.invoke("Tell me about LangChain"))
> ```

**Use Case:** Debugging LangChain scripts.
**Effectiveness:** ⭐⭐⭐⭐

**Example Output:**

```
Issue: 'model' should be 'model_name' and 'invoke' not valid for OpenAI directly.
Fixed Code:
llm = OpenAI(model_name="gpt-4")
print(llm("Tell me about LangChain"))
```

**Best Practices:**
Always cross-check class methods in latest LangChain docs.

---

### 🧮 Code Optimization

**Prompt:**

> Optimize this LangChain pipeline to improve speed and reduce API calls.
> Suggest caching or async mechanisms.

**Use Case:** Enhance performance of large chains.
**Effectiveness:** ⭐⭐⭐⭐½

**Example Output:**

> * Implement `LangChain CallbackManager` to track usage
> * Use `Memory` to avoid redundant calls
> * Parallelize with `asyncio`

**Tips:**
For production, integrate with `LangChainHub` for caching chains.

---

### 🧾 Code Explanation

**Prompt:**

> Explain what this LangChain agent code does in step-by-step manner.
> Include roles of each component and flow between modules.

**Use Case:** Understanding complex LLM pipelines.
**Effectiveness:** ⭐⭐⭐⭐⭐

**Example Input:**

```python
from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")
agent.run("What is the square root of the number of countries in Africa?")
```

**Example Output (summary):**

> * Loads web search and math tools.
> * Creates an agent that decides which tool to use.
> * Uses LLM reasoning to answer dynamically.

**Best Practices:**
Always explain prompt flow to build conceptual clarity.

---

### 📚 Documentation Generation

**Prompt:**

> Generate project documentation for a LangChain chatbot project.
> Include overview, setup steps, and architecture summary.

**Use Case:** Auto-writing docs for AI projects.
**Effectiveness:** ⭐⭐⭐⭐½

**Example Output:**

> **Overview:** This project implements a conversational chatbot using LangChain and GPT models.
> **Setup:** Install `langchain`, `openai`, and configure `.env`.
> **Architecture:** Input → LLM Chain → Output Parser → Response.

**Tips:**

* Use “Include code examples” for richer docs.

---

## ✍️ 2. Writing & Content

### 🧠 Technical Writing

**Prompt:**

> Write a technical explanation of **Prompt Templates in LangChain**.
> Include use cases, syntax, and example code.

**Effectiveness:** ⭐⭐⭐⭐⭐

**Example Output:**

> Prompt Templates standardize how we feed data to LLMs.
>
> ```python
> from langchain import PromptTemplate
> template = PromptTemplate(input_variables=["topic"], template="Explain {topic} simply.")
> print(template.format(topic="Transformers"))
> ```

---

### 📰 Blog Post Creation

**Prompt:**

> Write a 700-word blog post titled “How LangChain Simplifies LLM Application Development.”
> Include introduction, key benefits, and example use cases.

**Effectiveness:** ⭐⭐⭐⭐½

**Tips:**
Add “Optimize for SEO keywords: LangChain, LLM apps, prompt chaining.”

---

### 🧵 Social Media Content

**Prompt:**

> Write 3 engaging LinkedIn posts explaining why prompt engineering is the new essential AI skill in 2025.

**Effectiveness:** ⭐⭐⭐⭐

**Example Output:**

> “Prompt Engineering is not coding — it’s communication. The right words can unlock an LLM’s full intelligence.”

---

### ✉️ Email Template

**Prompt:**

> Draft an email inviting a research partner to collaborate on a Generative AI project using LangChain.
> Tone: professional and concise.

**Effectiveness:** ⭐⭐⭐⭐

**Example Output:**

> *Subject:* Collaboration Opportunity in LangChain Research
> *Body:*
> Hi [Name],
> I’m currently working on a Generative AI project exploring LangChain’s agent framework. Would you be interested in collaborating on fine-tuning and evaluation experiments?
> Regards,
> Baibhab

---

## 📊 3. Productivity & Analysis

### 📈 Data Analysis

**Prompt:**

> Analyze this text dataset and suggest preprocessing methods suitable for LLM training.
> Include cleaning, tokenization, and embedding strategies.

**Effectiveness:** ⭐⭐⭐⭐⭐

**Example Output:**

> * Remove stopwords, special symbols.
> * Apply SentencePiece tokenizer.
> * Convert to vector embeddings using OpenAI `text-embedding-ada-002`.

---

### 🧾 Summary Generation

**Prompt:**

> Summarize this LangChain documentation section in under 150 words:
> [PASTE TEXT HERE]

**Effectiveness:** ⭐⭐⭐⭐

**Tips:**
Add “List 3 takeaways at the end.”

---

### 🧠 Research Assistance

**Prompt:**

> Summarize top 3 recent papers on **Graph-based Alignment Models** for network analysis.
> Include citation-style references and brief contributions.

**Effectiveness:** ⭐⭐⭐⭐⭐

---

### 📝 Meeting Notes

**Prompt:**

> Convert this project meeting transcript into clear, structured meeting notes with action points and owner names.

**Effectiveness:** ⭐⭐⭐⭐

**Example Output:**

> **Decisions:** Use LangChain for chatbot framework
> **Actions:**
>
> * Baibhab: Connect OpenAI API by Oct 26
> * Team: Prepare demo slides

---

## 🎓 4. Learning & Explanation

### 🧩 Concept Explanation

**Prompt:**

> Explain **how LangChain memory works** in a chatbot application.
> Provide both conceptual and practical explanation.

**Effectiveness:** ⭐⭐⭐⭐⭐

**Example Output:**

> LangChain memory stores past conversations to provide context-aware replies.
> Example:
>
> ```python
> from langchain.memory import ConversationBufferMemory
> memory = ConversationBufferMemory()
> ```
>
> It allows multi-turn dialogue retention.

---

### 📘 Tutorial Creation

**Prompt:**

> Create a beginner tutorial for **building a LangChain chatbot** using OpenAI API.
> Include code, explanation, and expected outputs.

**Effectiveness:** ⭐⭐⭐⭐⭐

**Example Output:**

#### Step 1: Install Dependencies

```bash
pip install langchain openai python-dotenv
```

#### Step 2: Setup Environment

Create `.env` with API key.

#### Step 3: Define LLM Chain

```python
from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI

template = PromptTemplate(input_variables=["question"], template="Answer clearly: {question}")
llm_chain = LLMChain(prompt=template, llm=OpenAI())
print(llm_chain.run("What is Generative AI?"))
```

#### Step 4: Output

> "Generative AI refers to models that can create new content, such as text or images, by learning from data."

---

### 💡 Example Generation

**Prompt:**

> Generate 5 practical examples of using LangChain in real-world AI systems (e.g., chatbots, summarizers, tutors).

**Effectiveness:** ⭐⭐⭐⭐

**Example Output:**

1. Customer support chatbot
2. Research assistant summarizer
3. AI-driven study tutor
4. Automated FAQ responder
5. Conversational search tool

---

### 🧠 Analogy Building

**Prompt:**

> Create an analogy to explain **prompt chaining in LangChain**.
> Keep it simple for beginners.

**Effectiveness:** ⭐⭐⭐⭐⭐

**Example Output:**

> “Prompt chaining is like assembling Lego blocks — each prompt builds on the last to form a complete AI workflow.”

---
