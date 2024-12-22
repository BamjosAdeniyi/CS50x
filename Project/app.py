import os
from cs50 import SQL
from flask import Flask, render_template, request, redirect, url_for
import uuid
from questions import questions
from choices import choices
from facet_mapping import facet_mappings
from trait_explain import TRAIT_THRESHOLDS, TRAIT_EXPLANATIONS, FACET_THRESHOLDS, get_trait_category_and_explanation, get_facet_category

# Initialize the Flask app
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///personality_assessment.db")

# Trait name mappings
TRAIT_NAMES = {
    'A': 'Agreeableness',
    'C': 'Conscientiousness',
    'E': 'Extraversion',
    'N': 'Neuroticism',
    'O': 'Openness'
}

# Route: Home
@app.route("/")
def home():
    return render_template("home.html")

# Route: Assessment Page
@app.route("/assessment", methods=["GET"])
def assessment():
    # Generate a unique session ID for the user
    session_id = str(uuid.uuid4())
    return render_template("assessment.html", questions=questions, choices=choices, session_id=session_id)

# Route: Submit Responses
@app.route("/submit", methods=["POST"])
def submit():
    try:
        # Retrieve the session ID
        session_id = request.form.get("session_id")
        if not session_id:
            return render_template("apology.html", message="Session ID is missing from the form submission.")

        # Log received form data for debugging
        responses = request.form.to_dict(flat=False)
        print(f"Debug: Received responses: {responses}")

        # Validate that all questions are answered
        unanswered_questions = []
        for question in questions:
            response_key = f"responses[{question['id']}]"
            if response_key not in responses or not responses[response_key][0].strip():
                unanswered_questions.append(question['text'])

        if unanswered_questions:
            print(f"Debug: Unanswered questions: {unanswered_questions}")
            return render_template(
                "apology.html",
                message=f"Some questions were not answered: {', '.join(unanswered_questions)}"
            )

        # Initialize score accumulators
        trait_scores = {trait: 0 for trait in TRAIT_NAMES.keys()}
        facet_scores = {trait: {facet: 0 for facet in range(1, 7)} for trait in TRAIT_NAMES.keys()}

        # Process responses
        for question in questions:
            response_key = f"responses[{question['id']}]"
            if response_key in responses and responses[response_key]:
                score = int(responses[response_key][0])
                trait = question["domain"]
                facet = question["facet"]
                keyed = question["keyed"]

                # Apply scoring logic
                final_score = score if keyed == "plus" else (6 - score)

                # Update scores
                trait_scores[trait] += final_score
                facet_scores[trait][facet] += final_score

        # Insert scores into the database
        for trait, score in trait_scores.items():
            db.execute("INSERT INTO trait_scores (session_id, trait, score) VALUES (?, ?, ?)", session_id, trait, score)
        for trait, facets in facet_scores.items():
            for facet_number, score in facets.items():
                facet_name = facet_mappings[trait][facet_number]
                db.execute(
                    "INSERT INTO facet_scores (session_id, trait, facet, score) VALUES (?, ?, ?, ?)",
                    session_id, trait, facet_name, score
                )

        # Redirect to success page
        return redirect(url_for("success", session_id=session_id))

    except Exception as e:
        print(f"Error in /submit route: {e}")
        return render_template("apology.html", message="An unexpected error occurred. Please try again.")

# Route: Success Page
@app.route("/success/<session_id>")
def success(session_id):
    return render_template("success.html", session_id=session_id)

# Route: Check Results
@app.route("/check-results", methods=["GET", "POST"])
def check_results():
    if request.method == "GET":
        return render_template("check-results.html")

    if request.method == "POST":
        try:
            session_id = request.form.get("session_id")
            if not session_id:
                return render_template("apology.html", message="Session ID is required.")

            # Fetch traits
            traits = db.execute("SELECT trait, score FROM trait_scores WHERE session_id = ?", session_id)
            for trait in traits:
                trait_full_name = TRAIT_NAMES.get(trait["trait"], "Unknown")
                thresholds = TRAIT_THRESHOLDS.get(trait["trait"], {})
                explanations = TRAIT_EXPLANATIONS.get(trait["trait"], {})
                category, explanation = get_trait_category_and_explanation(
                    trait["score"], thresholds, explanations
                )
                trait.update({
                    "trait_full": trait_full_name,
                    "category": category,
                    "explanation": explanation
                })

            # Fetch facets
            facets = db.execute("SELECT trait, facet, score FROM facet_scores WHERE session_id = ?", session_id)
            facets_grouped_by_trait = {}
            for facet in facets:
                trait_full_name = TRAIT_NAMES.get(facet["trait"], "Unknown")
                if trait_full_name not in facets_grouped_by_trait:
                    facets_grouped_by_trait[trait_full_name] = []
                facet_category = get_facet_category(facet["score"], FACET_THRESHOLDS)
                facets_grouped_by_trait[trait_full_name].append({
                    "facet": facet["facet"],
                    "score": facet["score"],
                    "category": facet_category
                })

            # Debug output
            print("Traits:", traits)
            print("Facets Grouped by Trait:", facets_grouped_by_trait)

            return render_template(
                "results.html",
                traits=traits,
                facets_grouped_by_trait=facets_grouped_by_trait,
                session_id=session_id,
            )
        except Exception as e:
            print(f"Error in /check-results POST route: {e}")
            return render_template("apology.html", message="An unexpected error occurred. Please try again.")


# Print Result
@app.route("/results/<session_id>", methods=["GET"])
def results(session_id):
    try:
        # Fetch overall trait scores
        raw_traits = db.execute("SELECT trait, score FROM trait_scores WHERE session_id = ?", session_id)

        # Remove duplicates and map full trait names
        traits = {}
        for trait in raw_traits:
            full_name = TRAIT_NAMES.get(trait["trait"], trait["trait"])
            if full_name not in traits:
                traits[full_name] = trait["score"]

        # Fetch facet scores grouped by trait
        raw_facets = db.execute("SELECT trait, facet, score FROM facet_scores WHERE session_id = ?", session_id)
        facets_grouped_by_trait = {}
        for row in raw_facets:
            full_name = TRAIT_NAMES.get(row["trait"], row["trait"])
            if full_name not in facets_grouped_by_trait:
                facets_grouped_by_trait[full_name] = []
            facets_grouped_by_trait[full_name].append({
                "facet": row["facet"],
                "score": row["score"]
            })

        # Render results page
        return render_template(
            "results.html",
            traits=[{"trait_full": k, "score": v} for k, v in traits.items()],
            facets_grouped_by_trait=facets_grouped_by_trait,
            session_id=session_id
        )

    except Exception as e:
        print(f"Error in /results route: {e}")
        return render_template("apology.html", message="An unexpected error occurred. Please try again later.")

if __name__ == "__main__":
    app.run(debug=True)
