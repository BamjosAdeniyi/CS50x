# Big Five Personality Assessment
#### Video Demo:  <URL HERE>

---

## Description

This project is a **Big Five Personality Assessment Tool** that evaluates personality traits and facets using the widely recognized **Big Five Personality Model**. This model is extensively used in psychology due to its comprehensive framework, which categorizes human personality into five primary dimensions. The tool offers insights into these dimensions, helping individuals better understand their strengths, preferences, and interpersonal tendencies.

### The Five Traits and Their Facets:

1. **Agreeableness (A)**
   Reflects a person's tendency to prioritize harmony and cooperation in relationships.
   - **Facets**: Trust, Morality, Altruism, Cooperation, Modesty, Sympathy.

2. **Conscientiousness (C)**
   Measures self-discipline, organization, and goal-oriented behavior.
   - **Facets**: Self-Efficacy, Orderliness, Dutifulness, Achievement-Striving, Self-Discipline, Cautiousness.

3. **Extraversion (E)**
   Indicates how sociable, energetic, and outgoing an individual is.
   - **Facets**: Friendliness, Gregariousness, Assertiveness, Activity Level, Excitement-Seeking, Cheerfulness.

4. **Neuroticism (N)**
   Assesses emotional stability and how individuals handle stress.
   - **Facets**: Anxiety, Anger, Depression, Self-Consciousness, Immoderation, Vulnerability.

5. **Openness to Experience (O)**
   Captures intellectual curiosity, creativity, and openness to new ideas.
   - **Facets**: Imagination, Artistic Interest, Emotionality, Adventurousness, Intellect, Liberalism.

### Rationale for Using the IPIP-NEO-120 Inventory

The **IPIP-NEO-120 inventory** was chosen for this project due to its ability to assess not only the five major traits but also their respective facets. These facets provide a deeper understanding of individual differences within each personality dimension.

For instance:
- A high score in **Conscientiousness** could stem from strong **Self-Efficacy** (confidence in abilities) or **Orderliness** (preference for organization).
- Similarly, a high score in **Agreeableness** could result from high levels of **Trust** (confidence in others) or **Sympathy** (empathy for others).

By analyzing both traits and facets, the tool provides a comprehensive personality profile. This level of detail is particularly useful in applications like **roommate matching**, professional development, or personal growth.

This project draws inspiration from the [rubynor/bigfive-web](https://github.com/rubynor/bigfive-web) implementation and is a subset of my MSc project, **Development of a Roommate Matching System Using Personality Profiling**, which can be accessed on [GitHub](https://github.com/BamjosAdeniyi/roommate-matching-system).

---

## Features

### 1. Comprehensive Assessment
- Users are guided through 120 questions based on the **IPIP-NEO-120** framework.
- Each response contributes to scores for the Big Five traits and their facets.

### 2. Results Dashboard
- The dashboard displays:
  - **Overall Trait Scores** with categories: low, medium, and high.
  - **Detailed Explanations** for each trait, helping users interpret their scores.
  - **Facet-Level Scores**, providing deeper insights into personality dimensions.

### 3. Data Visualization
- Interactive bar charts generated using **Chart.js** visually represent trait and facet scores.

### 4. Unique ID System
- Upon completion, users receive a **unique ID** to access their results without requiring an account.

### 5. PDF Download
- Users can download their results page as a **PDF** for future reference.

### 6. Responsive Design
- The application is fully responsive, ensuring usability on both desktop and mobile devices.

---

## Design and Implementation

### Framework
The project is built using the **Flask** framework for its simplicity and flexibility. Flask allowed for rapid prototyping while supporting scalable architecture.

### Unique ID System
To ensure privacy, users are assigned a unique ID instead of creating accounts. This ID enables them to retrieve their results later.

### Chart.js Integration
**Chart.js** was integrated for data visualization, making results intuitive and engaging.

### AI Assistance
AI tools were employed for:
- Debugging complex issues.
- Optimizing the codebase.
- Making architectural decisions.

### Roommate Matching Integration
This project is a subset of a larger MSc project on roommate matching. Insights from the Big Five assessment directly influence the matching algorithm by identifying compatible personality traits and preferences.

---

## Acknowledgments

### Inspiration
This project was inspired by the [rubynor/bigfive-web](https://github.com/rubynor/bigfive-web) project, which implemented a similar personality assessment tool.

### Academic Connection
It is also a part of my MSc project titled **Development of a Roommate Matching System Using Personality Profiling**, available on [GitHub](https://github.com/BamjosAdeniyi/roommate-matching-system).

### AI Tools
ChatGPT was instrumental in ensuring a streamlined development process. It provided:
- Debugging assistance.
- Suggestions for optimization.
- Feedback on design choices.

---

## Future Improvements

1. **User Accounts**:
   Implementing optional user accounts for result storage and tracking over time.

2. **Custom Reports**:
   Providing users with personalized suggestions based on their personality profiles.

3. **Enhanced Visualizations**:
   Adding interactive visualizations for a more engaging user experience.

4. **Expanded Applications**:
   Extending the assessment to support use cases like career guidance, team-building, and educational planning.

---
