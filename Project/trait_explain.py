# Thresholds and explanations for personality traits
TRAIT_THRESHOLDS = {
    "A": {"low": 40, "medium": 80},  # Agreeableness
    "C": {"low": 40, "medium": 80},  # Conscientiousness
    "E": {"low": 40, "medium": 80},  # Extraversion
    "N": {"low": 40, "medium": 80},  # Neuroticism
    "O": {"low": 40, "medium": 80},  # Openness
}

TRAIT_EXPLANATIONS = {
    "A": {  # Agreeableness
        "low": (
            "You tend to prioritize your own needs and opinions over those of others. "
            "This can make you appear less cooperative or empathetic in social situations. "
            "While this competitive edge can be advantageous in assertive or leadership roles, "
            "it may sometimes lead to conflicts in relationships."
        ),
        "medium": (
            "You strike a balance between cooperation and assertiveness. "
            "You are generally kind and understanding but are not afraid to stand your ground "
            "when necessary. This balanced approach helps you maintain healthy interpersonal relationships "
            "while achieving your goals."
        ),
        "high": (
            "You are deeply empathetic, cooperative, and considerate towards others. "
            "Your ability to connect with people emotionally makes you a reliable and trustworthy companion. "
            "While this fosters strong relationships, it may sometimes lead you to prioritize others' needs over your own."
        ),
    },
    "C": {  # Conscientiousness
        "low": (
            "You may find it challenging to maintain organization and stick to plans. "
            "This can lead to difficulties in meeting deadlines or achieving long-term goals. "
            "However, this relaxed approach can also make you adaptable and open to spontaneity."
        ),
        "medium": (
            "You have a balanced approach to organization and spontaneity. "
            "While you are reasonably disciplined, you also allow room for flexibility in your plans. "
            "This balance often enables you to adapt to unexpected changes while staying focused on your objectives."
        ),
        "high": (
            "You are highly disciplined, organized, and goal-oriented. "
            "You excel in planning and executing tasks efficiently, often exceeding expectations. "
            "This trait makes you reliable and driven, but it may sometimes lead to stress if you take on too much responsibility."
        ),
    },
    "E": {  # Extraversion
        "low": (
            "You are reserved, introspective, and tend to enjoy solitude or smaller social settings. "
            "Large gatherings or highly social environments may feel overwhelming, and you often prefer deeper, one-on-one interactions. "
            "This quiet demeanor allows you to focus on thoughtful reflection and close relationships."
        ),
        "medium": (
            "You have a balanced personality, enjoying both social interactions and personal downtime. "
            "You can be outgoing when needed but also appreciate moments of solitude to recharge. "
            "This versatility helps you adapt well to different social situations."
        ),
        "high": (
            "You are outgoing, energetic, and thrive in social environments. "
            "You enjoy meeting new people, participating in group activities, and expressing yourself openly. "
            "Your vibrant personality can make you the center of attention, but you may sometimes find it hard to enjoy alone time."
        ),
    },
    "N": {  # Neuroticism
        "low": (
            "You are emotionally stable, calm, and resilient under stress. "
            "Even in challenging situations, you maintain composure and rarely let emotions interfere with your decisions. "
            "This stability makes you a source of reassurance for others, though it may occasionally come across as emotional detachment."
        ),
        "medium": (
            "You experience occasional mood swings but generally manage your emotions well. "
            "You may feel stressed or anxious at times, but you recover quickly and maintain a level-headed approach to challenges. "
            "This balance allows you to empathize with others while staying grounded."
        ),
        "high": (
            "You experience frequent emotional ups and downs and are highly sensitive to stress. "
            "This heightened emotional awareness can make you empathetic and intuitive, but it may also lead to overthinking or worrying. "
            "Developing stress management techniques can help you channel this sensitivity constructively."
        ),
    },
    "O": {  # Openness
        "low": (
            "You prefer routine, tradition, and familiar ways of doing things. "
            "You may be less interested in exploring new ideas or experiences, focusing instead on practicality and reliability. "
            "While this provides stability, it may limit opportunities for personal growth or innovation."
        ),
        "medium": (
            "You appreciate new ideas and experiences while maintaining a comfort zone with familiar routines. "
            "You are open to exploring creative opportunities but prefer to weigh the risks carefully. "
            "This balanced approach helps you adapt to change without feeling overwhelmed."
        ),
        "high": (
            "You are highly creative, curious, and open to new experiences. "
            "You enjoy exploring diverse perspectives, engaging in imaginative thinking, and embracing innovation. "
            "This openness allows you to thrive in dynamic environments, though it may sometimes lead to overcommitment to novel ideas."
        ),
    },
}



FACET_THRESHOLDS = {"low": 5, "medium": 10}  # Default thresholds for facets

def get_trait_category_and_explanation(score, thresholds, explanations):
    if score <= thresholds["low"]:
        category = "low"
    elif score <= thresholds["medium"]:
        category = "medium"
    else:
        category = "high"
    explanation = explanations[category]
    return category, explanation

def get_facet_category(score, thresholds):
    if score <= thresholds["low"]:
        return "low"
    elif score <= thresholds["medium"]:
        return "medium"
    else:
        return "high"
