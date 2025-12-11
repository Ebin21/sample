from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, 'MSc CA - July 2025 - Internal Assessment', 0, 1, 'R')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, self.sanitize(label), 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, self.sanitize(body))
        self.ln(1)

    def sanitize(self, text):
        """Replace problematic Unicode characters"""
        replacements = {
            '✓': '[CORRECT]',
            '✗': '[INCORRECT]',
            '☑': '[X]',
            '☐': '[ ]',
            '–': '-',
            '—': '--',
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

# Generate PDF
pdf = PDF()
pdf.add_page()
pdf.set_title("MSc CA Assessment - Research Methodology")

content_data = """
# MSC-CA Semester 1 - Research Methodology Internal Assessment
## Complete Question Bank with Answer Keys
**Course:** Master of Science in Computer Applications  
**Semester:** 1 (July 2025)  
**Subject:** Research Methodology & Introduction to Research (RM-IA)  
**Total Questions:** 30  
**Date:** December 11, 2025

---

## Questions with Answers

### Question 1
**What is the first step in the research process?**

- Defining Problem or Formulating a research question ✓ **CORRECT**
- Literature review
- Data collection
- Data analysis

**Explanation:** The foundation of any research begins with identifying and clearly defining the problem or research question. This guides all subsequent research activities.

---

### Question 2
**What type of research design involves the random assignment of participants to different conditions and the manipulation of one or more independent variables?**

- Descriptive research
- Experimental research ✓ **CORRECT**
- Correlational research
- Qualitative research

**Explanation:** Experimental research is characterized by controlled manipulation of variables and random assignment of participants to ensure validity and establish cause-and-effect relationships.

---

### Question 3
**Which type of research is primarily exploratory and is used to gain an understanding of underlying reasons, opinions, and motivations?**

- Descriptive research
- Correlational research
- Experimental research
- Qualitative research ✓ **CORRECT**

**Explanation:** Qualitative research focuses on exploring underlying motivations, opinions, and reasons—ideal for understanding the "why" behind phenomena rather than quantifying them.

---

### Question 4
**After collecting data, the next step in the research process is usually:**

- Formulating a hypothesis
- Data analysis ✓ **CORRECT**
- Defining the problem
- Conducting a literature review

**Explanation:** Once data is collected, it must be analyzed to extract meaningful patterns and insights. Data analysis transforms raw data into useful information.

---

### Question 5
**What is the primary purpose of a literature review?**

- Summarize and critically evaluate previous research ✓ **CORRECT**
- List all studies on a topic without evaluation
- Replace the need for conducting your own research
- Limit the scope of your research question

**Explanation:** A literature review synthesizes existing knowledge, identifies gaps, and critically evaluates previous findings to provide context for new research.

---

### Question 6
**Which of the following is NOT a recognized type of research?**

- Basic research
- Applied research
- Quantitative research
- Literary research ✓ **CORRECT**

**Explanation:** While "literary research" involves studying literature as a subject, it's not classified as a formal research type in research methodology. The recognized types are basic, applied, quantitative, and qualitative.

---

### Question 7
**What type of research examines the relationship between two variables without manipulating them?**

- Experimental research
- Descriptive research
- Correlational research ✓ **CORRECT**
- Qualitative research

**Explanation:** Correlational research identifies relationships and associations between variables without introducing any experimental manipulation or control.

---

### Question 8
**The process of grouping variables in a literature review can help in:**

- Refining the research questions or hypotheses ✓ **CORRECT**
- Making the review more subjective
- Avoiding critical analysis of the literature
- Limiting the scope to only one variable

**Explanation:** Grouping variables helps identify patterns and themes across studies, leading to refined research questions and clearer hypotheses.

---

### Question 9
**After collecting data, the next step in the research process is usually:**

- Formulating a hypothesis
- Data analysis ✓ **CORRECT**
- Defining the problem
- Conducting a literature review

**Explanation:** Data analysis is the logical next step after collection, where researchers examine and interpret the data to draw conclusions.

---

### Question 10
**Which characteristic is typical of quantitative research?**

- Focus on personal experiences
- Uses numerical data and statistical analysis ✓ **CORRECT**
- Emphasizes understanding context and meanings
- Relies on observational methods without measurement

**Explanation:** Quantitative research is defined by its use of numerical data, measurements, and statistical analysis to test hypotheses and establish relationships.

---

### Question 11
**What is the primary purpose of grouping variables in a literature review?**

- To simplify the writing process
- To identify patterns and themes across studies ✓ **CORRECT**
- To reduce the number of sources reviewed
- To make the review more objective

**Explanation:** Grouping variables reveals patterns, themes, and gaps across literature, facilitating synthesis and comparison of findings.

---

### Question 12
**Which of the following is a key difference between a systematic literature review and a traditional review?**

- Systematic reviews use rigorous and replicable methodology ✓ **CORRECT**
- Systematic reviews are faster to complete
- Systematic reviews focus only on qualitative data
- Traditional reviews are more objective

**Explanation:** Systematic reviews follow explicit, predetermined protocols and are exhaustive in scope, whereas traditional reviews are more narrative and subjective.

---

### Question 13
**Which type of literature review would typically require the registration of a review protocol?**

- Traditional literature review
- Systematic literature review ✓ **CORRECT**
- Critical literature review
- None of the above

**Explanation:** Systematic literature reviews require pre-registration of the protocol (PROSPERO, OSF) to ensure transparency and reduce bias.

---

### Question 14
**A traditional literature review typically:**

- Uses explicit inclusion/exclusion criteria
- Often lacks explicit inclusion/exclusion criteria ✓ **CORRECT**
- Follows a strict pre-registered protocol
- Requires meta-analysis

**Explanation:** Traditional reviews are narrative syntheses without pre-specified criteria, unlike systematic reviews which have explicit protocols.

---

### Question 15
**In which type of literature review is the subjective interpretation of the reviewer most apparent?**

- Systematic literature review
- Traditional literature review ✓ **CORRECT**
- Critical literature review
- Meta-analysis

**Explanation:** Traditional literature reviews allow for more subjective selection and interpretation compared to systematic reviews, which use standardized procedures.

---

### Question 16
**What is primary data?**

- Data that is collected by someone else and used in your research
- Data collected firsthand by the researcher for a specific purpose ✓ **CORRECT**
- Data that is found in books and articles
- Data that is outdated and no longer useful

**Explanation:** Primary data is original data collected directly by the researcher for their specific research objectives, ensuring relevance and control.

---

### Question 17
**The final step in the research process, where findings are communicated to others, is called:**

- Data collection
- Data analysis
- Literature review
- Reporting and publishing results ✓ **CORRECT**

**Explanation:** Reporting and publishing results complete the research cycle by sharing findings with the academic and professional community.

---

### Question 18
**Which approach is typically emphasized in a critical literature review?**

- A descriptive summary of studies
- An unbiased and rigorous search strategy
- A critical evaluation and synthesis of the literature ✓ **CORRECT**
- A focus on providing a comprehensive list of all studies

**Explanation:** Critical literature reviews emphasize critical evaluation and synthesis of findings, moving beyond mere description to interpret and evaluate quality.

---

### Question 19
**What type of research focuses on understanding fundamental aspects of phenomena without a specific application in mind?**

- Basic research ✓ **CORRECT**
- Applied research
- Descriptive research
- Exploratory research

**Explanation:** Basic research aims to advance fundamental knowledge and understanding without immediate practical application, emphasizing theoretical understanding.

---

### Question 20
**Which of the following is common to both systematic and critical literature reviews?**

- They both involve a rigorous and systematic search of the literature ✓ **CORRECT**
- They both avoid critical evaluation of the studies
- They both aim to provide a narrative summary of the literature
- They both allow for subjective interpretation without strict criteria

**Explanation:** Both systematic and critical reviews employ rigorous methodologies, though systematic reviews are more standardized while critical reviews emphasize evaluation.

---

### Question 21
**Which of the following is a key feature of a systematic literature review?**

- It aims to offer a general overview of the literature
- It includes an exhaustive and comprehensive search strategy ✓ **CORRECT**
- It allows for selective inclusion of studies based on the author's preference
- It focuses on presenting qualitative data only

**Explanation:** Systematic reviews are characterized by comprehensive, exhaustive search strategies with explicit inclusion/exclusion criteria to minimize bias.

---

### Question 22
**In which phase of the research process do researchers develop instruments or tools for data collection?**

- Research design ✓ **CORRECT**
- Literature review
- Formulating the problem
- Data analysis

**Explanation:** During the research design phase, researchers develop questionnaires, interview guides, observation protocols, or other measurement instruments.

---

### Question 23
**In which type of literature review is the subjective interpretation of the reviewer most apparent?**

- Traditional literature review ✓ **CORRECT**
- Systematic literature review
- Critical literature review
- Meta-analysis

**Explanation:** Traditional reviews rely heavily on the reviewer's subjective judgment in selecting and interpreting sources, unlike systematic approaches.

---

### Question 24
**Which type of research is designed to systematically describe a situation, problem, phenomenon, or population?**

- Exploratory research
- Descriptive research ✓ **CORRECT**
- Experimental research
- Longitudinal research

**Explanation:** Descriptive research systematically documents characteristics, conditions, and phenomena, providing detailed descriptions without manipulation.

---

### Question 25
**Which type of literature review is most likely to include a meta-analysis?**

- Traditional literature review
- Systematic literature review ✓ **CORRECT**
- Critical literature review
- None of the above

**Explanation:** Systematic literature reviews often include meta-analysis (quantitative synthesis of results) when data from studies are comparable.

---

### Question 26
**Empirical research is primarily based on:**

- Hypothesis
- Theory
- Observation and experimentation ✓ **CORRECT**
- Literature review

**Explanation:** Empirical research relies on direct observation, experimentation, and actual data collection rather than theory or literature alone.

---

### Question 27
**Which type of research establishes a cause-and-effect relationship between variables?**

- Correlational research
- Descriptive research
- Experimental research ✓ **CORRECT**
- Exploratory research

**Explanation:** Only experimental research, with controlled manipulation of variables and random assignment, can establish true cause-and-effect relationships.

---

### Question 28
**Which type of research aims to solve specific, practical problems?**

- Basic research
- Applied research ✓ **CORRECT**
- Quantitative research
- Qualitative research

**Explanation:** Applied research targets practical problems and aims for solutions with immediate application value in real-world contexts.

---

### Question 29
**Which type of research establishes a cause-and-effect relationship between variables?**

- Correlational research
- Descriptive research
- Experimental research ✓ **CORRECT**
- Exploratory research

**Explanation:** Experimental research, through controlled variable manipulation and random assignment, can establish cause-and-effect relationships.

---

### Question 30
**What is the primary focus of a traditional literature review?**

- To provide a comprehensive summary of the available literature on a specific topic ✓ **CORRECT**
- To critically evaluate and synthesize existing research on a topic
- To systematically search for and appraise research evidence
- To conduct a meta-analysis of quantitative studies

**Explanation:** Traditional literature reviews aim to provide a narrative summary of existing literature, highlighting key findings and gaps in knowledge.

---

## Summary of Answer Distribution

| Research Type | Count | Key Characteristics |
|---|---|---|
| **Experimental Research** | 4 | Random assignment, variable manipulation, cause-and-effect |
| **Qualitative Research** | 2 | Understanding reasons, opinions, motivations, context |
| **Descriptive Research** | 2 | Systematic description, documentation, observation |
| **Applied Research** | 2 | Practical problems, real-world solutions |
| **Literature Review Types** | 10 | Systematic, Traditional, Critical approaches |
| **Data & Methodology** | 5 | Primary data, data analysis, research design |
| **Research Process** | 3 | Steps and stages in research |

---

## Key Concepts Reference

### Research Types by Purpose
- **Basic Research:** Fundamental understanding without specific application
- **Applied Research:** Solving practical, specific problems
- **Quantitative:** Numerical data, statistical analysis
- **Qualitative:** Meanings, experiences, context

### Research Designs
- **Experimental:** Manipulation + Random Assignment + Control
- **Correlational:** Relationship identification without manipulation
- **Descriptive:** Systematic observation and documentation
- **Exploratory:** Initial investigation, understanding

### Literature Review Approaches
| Aspect | Traditional | Systematic | Critical |
|---|---|---|---|
| **Protocol Registration** | No | Yes | No |
| **Search Strategy** | Narrative | Exhaustive | Rigorous |
| **Inclusion Criteria** | Implicit | Explicit | Implicit but justified |
| **Subjectivity** | High | Low | Moderate-High |
| **Meta-Analysis** | Rare | Common | Possible |

### Research Process Sequence
1. **Define Problem** → Formulate research question
2. **Literature Review** → Understand existing knowledge
3. **Hypothesis Formulation** → Predict relationships
4. **Research Design** → Plan methodology & develop instruments
5. **Data Collection** → Gather primary or secondary data
6. **Data Analysis** → Extract meaningful insights
7. **Reporting & Publishing** → Share findings with community

---

## Important Notes for MSC-CA Students

This assessment tests foundational understanding of research methodology essential for:
- Thesis/project proposal development
- Literature review writing
- Research design selection
- Proper data collection and analysis
- Academic writing and publication

**Focus Areas for Exam Success:**
- Distinguish between research types (basic vs. applied, quantitative vs. qualitative)
- Understand literature review methodologies
- Know research process sequence
- Recognize data types and collection methods
- Understand cause-and-effect vs. correlation vs. description

---

**Document prepared:** December 11, 2025  
**All 30 Questions Covered**  
**Ready for MSC-CA Exam Preparation**
"""

lines = content_data.split('\n')
buffer = ""

for line in lines:
    line = line.strip()
    
    if not line:
        if buffer:
            pdf.chapter_body(buffer)
            buffer = ""
        pdf.ln(1)
        continue
    
    if line.startswith('# '):
        if buffer:
            pdf.chapter_body(buffer)
            buffer = ""
        pdf.set_font('Arial', 'B', 16)
        pdf.multi_cell(0, 10, pdf.sanitize(line.replace('# ', '')))
        pdf.ln(5)
    elif line.startswith('## '):
        if buffer:
            pdf.chapter_body(buffer)
            buffer = ""
        pdf.chapter_title(line.replace('## ', ''))
    else:
        buffer += (" " + line) if buffer else line

if buffer:
    pdf.chapter_body(buffer)

pdf.output("Research-Methodology.pdf")
print("✓ PDF generated successfully: Research-Methodology.pdf")
