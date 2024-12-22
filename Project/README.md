# Big Five Personality Assessment
#### Video Demo:  <URL HERE>

#### Description:
This project is a Big Five Personality Assessment Tool that leverages the well-established Big Five Personality Model to evaluate personality traits and facets. The Big Five Personality Model is widely recognized in psychology for its comprehensive approach to personality assessment. It categorizes personality into five major dimensions:

1. **Agreeableness (A)**
Reflects an individual's tendency to be compassionate, cooperative, and harmonious in relationships.

Facets: Trust, Morality, Altruism, Cooperation, Modesty, Sympathy.

2. **Conscientiousness (C)**
Measures a person's self-discipline, organization, and goal-oriented behavior.

Facets: Self-Efficacy, Orderliness, Dutifulness, Achievement-Striving, Self-Discipline, Cautiousness.

3. **Extraversion (E)**
Indicates how outgoing, energetic, and sociable a person is.

Facets: Friendliness, Gregariousness, Assertiveness, Activity Level, Excitement-Seeking, Cheerfulness.

4. **Neuroticism (N)**
Assesses emotional stability and sensitivity to stress.

Facets: Anxiety, Anger, Depression, Self-Consciousness, Immoderation, Vulnerability.

5. **Openness to Experience (O)**
Captures intellectual curiosity, creativity, and openness to new experiences.

Facets: Imagination, Artistic Interest, Emotionality, Adventurousness, Intellect, Liberalism.

#### Rationale for Using the IPIP-NEO-120 Inventory
This project utilizes the IPIP-NEO-120 inventory, a widely used questionnaire designed to assess the Big Five personality traits. The rationale for choosing this inventory is its comprehensive structure. Unlike many other personality assessment tools that only evaluate the five broad traits, the IPIP-NEO-120 goes a step further by delving into the facets that make up each trait. This facet-level detail provides a more nuanced understanding of an individual's personality, enabling insights into specific strengths and characteristics within each dimension.

For example:

While a high score in Conscientiousness indicates a disciplined individual, the facet scores (e.g., Self-Efficacy or Dutifulness) reveal whether their discipline stems from confidence in their abilities, adherence to rules, or both.
Similarly, facets like Trust or Sympathy in Agreeableness allow for more precise insights into how an individual interacts with others.
By implementing the IPIP-NEO-120, this tool not only evaluates high-level traits but also provides a deeper layer of analysis, which is particularly valuable for applications like roommate matching or professional development. This enhanced level of detail is critical for addressing the project's broader goals, including its connection to my MSc project on **Development of a Roommate Matching System Using Personality Profiling**.

This project was inspired by a similar implementation available at [rubynor/bigfive-web](https://github.com/rubynor/bigfive-web) and is a subset of a larger MSc project titled **Development of a Roommate Matching System Using Personality Profiling**, which can be found on [GitHub](https://github.com/BamjosAdeniyi/roommate-matching-system). AI assistance was used during this project’s development for debugging, optimization, and ensuring a seamless user experience.

---

### Features:
1. **Comprehensive Assessment**:
   - Users are guided through a series of questions designed to evaluate their personality based on the Big Five model.
   - Responses are scored using the IPIP-NEO-120 framework.

2. **Results Dashboard**:
   - Displays overall scores for each trait with categorizations (low, medium, high) and detailed explanations.
   - Breaks down facet-level scores for each trait and provides additional insights.

3. **Data Visualization**:
   - Charts for both trait and facet scores are generated using Chart.js, offering users a visual representation of their results.

4. **Unique ID System**:
   - Each user receives a unique ID upon completing the assessment, enabling them to retrieve their results later.

5. **PDF Download**:
   - The result page can be printed or downloaded as a PDF for future reference.

### Design Choices:
1. **Framework**: Flask was chosen for its simplicity and flexibility, allowing rapid prototyping while ensuring scalability.
2. **Chart.js Integration**: Charts were integrated for data visualization to make results more intuitive and engaging.
3. **Responsive Design**: Bootstrap and custom CSS were used to ensure that the application looks good on both desktop and mobile devices.
4. **AI Assistance**: Throughout the project, AI tools were utilized for debugging, code optimization, and architectural decisions. This approach significantly enhanced development efficiency and reduced errors.
5. **Unique ID System**: This ensures user privacy while allowing results to be retrieved without requiring user accounts.

---

### Acknowledgments:
1. **Inspiration**:
   - This project draws inspiration from [rubynor/bigfive-web](https://github.com/rubynor/bigfive-web), which implemented a similar personality assessment system.
2. **Academic Integration**:
   - This project is a subset of the larger MSc project, **Development of a Roommate Matching System Using Personality Profiling**, available at [GitHub](https://github.com/BamjosAdeniyi/roommate-matching-system).
3. **AI Tools**:
   - AI assistance was instrumental in streamlining the development process, particularly in debugging and optimizing the application.


