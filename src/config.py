"""
EB-1A Opportunity System Configuration
Centralized configuration for the entire system
"""

import os
from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum

class EmailFormat(Enum):
    PLAIN_TEXT = "plain_text"
    HTML = "html"
    BOTH = "both"

class NotificationFrequency(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    URGENT_ONLY = "urgent_only"

@dataclass
class UserProfile:
    """User profile configuration"""
    name: str
    email: str
    field: str
    role: str
    location: str
    weak_criteria: List[str]
    strong_criteria: List[str]
    keywords: List[str]
    notification_frequency: NotificationFrequency = NotificationFrequency.DAILY
    email_format: EmailFormat = EmailFormat.HTML
    max_opportunities_per_email: int = 7
    timezone: str = "America/Chicago"  # Austin, Texas timezone
    
class SystemConfig:
    """System-wide configuration"""
    
    # Email settings
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    EMAIL_USERNAME = os.getenv('EMAIL_USERNAME', '')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')
    FROM_EMAIL = os.getenv('FROM_EMAIL', 'eb1a-opportunities@example.com')
    
    # Search settings
    SEARCH_KEYWORDS = [
        "Call for papers", "CFP", "Conference", "Workshop", "Symposium",
        "Peer reviewer", "Editorial board", "Journal reviewer",
        "Expert commentary", "Media interview", "Press quote",
        "Award nomination", "Competition", "Recognition",
        "Speaking opportunity", "Keynote", "Panel discussion",
        "Networking event", "Professional association", "Industry meetup"
    ]
    
    # Field-specific keywords
    FIELD_KEYWORDS = {
        "AI/ML": [
            "Artificial Intelligence", "Machine Learning", "Deep Learning",
            "Neural Networks", "Computer Vision", "Natural Language Processing",
            "Reinforcement Learning", "MLOps", "AI Ethics"
        ],
        "Cloud Native": [
            "Kubernetes", "Docker", "Microservices", "Serverless",
            "Container Orchestration", "Cloud Architecture", "DevOps",
            "Infrastructure as Code", "Service Mesh"
        ],
        "DevSecOps": [
            "DevSecOps", "Security Automation", "CI/CD Security",
            "Infrastructure Security", "Application Security",
            "Security Testing", "Compliance Automation"
        ],
        "Cybersecurity": [
            "Information Security", "Cyber Defense", "Threat Intelligence",
            "Incident Response", "Security Architecture", "Risk Management",
            "Penetration Testing", "Security Governance"
        ]
    }
    
    # Opportunity sources
    OPPORTUNITY_SOURCES = {
        "academic": [
            "https://www.wikicfp.com/cfp/",
            "https://www.conference-service.com/",
            "https://academic.microsoft.com/",
        ],
        "media": [
            "https://www.helpareporter.com/",
            "https://profnet.prnewswire.com/",
            "https://www.sourcebottle.com/"
        ],
        "awards": [
            "https://awards.ai/",
            "https://www.computerworld.com/events/",
            "https://www.cybersecurityexcellenceawards.com/"
        ],
        "networking": [
            "https://www.meetup.com/",
            "https://www.eventbrite.com/",
            "https://live360events.com/"
        ]
    }
    
    # Scoring weights for opportunity ranking
    SCORING_WEIGHTS = {
        "keyword_match": 2.0,
        "prestige_rating": 1.5,
        "evidence_value": 1.5,
        "weak_criteria_bonus": 3.0,
        "time_investment_penalty": 0.5,
        "deadline_urgency": 1.0
    }
    
    # Database settings
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///eb1a_opportunities.db')
    
    # Logging settings
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'eb1a_system.log')
    
    # Rate limiting
    MAX_REQUESTS_PER_MINUTE = 60
    MAX_EMAILS_PER_DAY = 10
    
    # Cache settings
    CACHE_DURATION_HOURS = 24
    CACHE_DIRECTORY = os.getenv('CACHE_DIR', './cache')

class OpportunityCategories:
    """Categorization of opportunities for better filtering"""
    
    CATEGORIES = {
        "speaking": {
            "keywords": ["conference", "keynote", "presentation", "talk", "panel", "workshop"],
            "evidence_value": "High",
            "typical_time_investment": "Medium to High",
            "eb1a_criteria": ["speaking", "critical role"]
        },
        "judging": {
            "keywords": ["peer review", "editorial board", "judge", "reviewer", "committee"],
            "evidence_value": "High",
            "typical_time_investment": "Medium",
            "eb1a_criteria": ["judging"]
        },
        "media": {
            "keywords": ["interview", "commentary", "expert opinion", "quote", "article"],
            "evidence_value": "Medium to High",
            "typical_time_investment": "Low to Medium",
            "eb1a_criteria": ["media"]
        },
        "awards": {
            "keywords": ["award", "recognition", "honor", "prize", "achievement"],
            "evidence_value": "Very High",
            "typical_time_investment": "Low to Medium",
            "eb1a_criteria": ["awards"]
        },
        "networking": {
            "keywords": ["meetup", "networking", "community", "association", "group"],
            "evidence_value": "Low to Medium",
            "typical_time_investment": "Medium",
            "eb1a_criteria": ["critical role", "membership"]
        },
        "writing": {
            "keywords": ["article", "blog post", "publication", "journal", "magazine"],
            "evidence_value": "Medium to High",
            "typical_time_investment": "Medium to High",
            "eb1a_criteria": ["publications", "media"]
        }
    }

class EmailTemplateConfig:
    """Configuration for email templates"""
    
    TEMPLATE_STYLES = {
        "professional": {
            "color_scheme": ["#2c3e50", "#3498db", "#ecf0f1"],
            "font_family": "Arial, sans-serif",
            "tone": "formal"
        },
        "modern": {
            "color_scheme": ["#667eea", "#764ba2", "#f8f9ff"],
            "font_family": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
            "tone": "friendly_professional"
        },
        "minimal": {
            "color_scheme": ["#333333", "#666666", "#f5f5f5"],
            "font_family": "Georgia, serif",
            "tone": "concise"
        }
    }
    
    DAILY_TIPS = [
        "Focus on opportunities that address your weak criteria first - they'll have the biggest impact on your petition.",
        "Quality over quantity - it's better to excel in a few opportunities than to spread yourself too thin.",
        "Document everything - keep detailed records of your contributions and their impact.",
        "Network strategically - the connections you make can lead to future opportunities.",
        "Stay consistent - small daily actions compound into significant achievements.",
        "Leverage your PhD research - many opportunities can tie back to your academic work.",
        "Consider remote opportunities - they expand your reach beyond your local area.",
        "Follow up professionally - many opportunities require persistent but respectful follow-up.",
        "Build relationships before you need them - networking is about giving, not just receiving.",
        "Track your metrics - know your response rates and success rates to improve over time."
    ]

def create_default_user_profile() -> UserProfile:
    """Create a default user profile based on the provided information"""
    return UserProfile(
        name="EB-1A Candidate",
        email="user@example.com",
        field="Software Engineer, AI/ML research in Cloud Native, DevSecOps, Cybersecurity",
        role="Full Stack Software Engineer, doing AI/ML research as PhD Student",
        location="Austin, Texas, or Remote anywhere",
        weak_criteria=["judging", "media", "awards"],
        strong_criteria=["publications", "speaking", "critical role"],
        keywords=["AI", "ML", "Cloud Native", "DevSecOps", "Cybersecurity", "Software Engineering"],
        notification_frequency=NotificationFrequency.DAILY,
        email_format=EmailFormat.HTML,
        max_opportunities_per_email=7,
        timezone="America/Chicago"
    )

def load_user_profile_from_env() -> UserProfile:
    """Load user profile from environment variables"""
    return UserProfile(
        name=os.getenv('USER_NAME', 'EB-1A Candidate'),
        email=os.getenv('USER_EMAIL', 'user@example.com'),
        field=os.getenv('USER_FIELD', 'Software Engineer, AI/ML research'),
        role=os.getenv('USER_ROLE', 'Full Stack Software Engineer, PhD Student'),
        location=os.getenv('USER_LOCATION', 'Austin, Texas, or Remote'),
        weak_criteria=os.getenv('WEAK_CRITERIA', 'judging,media,awards').split(','),
        strong_criteria=os.getenv('STRONG_CRITERIA', 'publications,speaking,critical role').split(','),
        keywords=os.getenv('USER_KEYWORDS', 'AI,ML,Cloud Native,DevSecOps,Cybersecurity').split(','),
        notification_frequency=NotificationFrequency(os.getenv('NOTIFICATION_FREQUENCY', 'daily')),
        email_format=EmailFormat(os.getenv('EMAIL_FORMAT', 'html')),
        max_opportunities_per_email=int(os.getenv('MAX_OPPORTUNITIES', '7')),
        timezone=os.getenv('USER_TIMEZONE', 'America/Chicago')
    )

def validate_config() -> Dict[str, Any]:
    """Validate system configuration and return status"""
    validation_results = {
        "email_config": False,
        "database_config": False,
        "user_profile": False,
        "errors": []
    }
    
    # Validate email configuration
    if SystemConfig.EMAIL_USERNAME and SystemConfig.EMAIL_PASSWORD:
        validation_results["email_config"] = True
    else:
        validation_results["errors"].append("Email credentials not configured")
    
    # Validate database configuration
    if SystemConfig.DATABASE_URL:
        validation_results["database_config"] = True
    else:
        validation_results["errors"].append("Database URL not configured")
    
    # Validate user profile
    try:
        profile = load_user_profile_from_env()
        if profile.email and "@" in profile.email:
            validation_results["user_profile"] = True
        else:
            validation_results["errors"].append("Invalid user email address")
    except Exception as e:
        validation_results["errors"].append(f"User profile validation error: {str(e)}")
    
    return validation_results

if __name__ == "__main__":
    # Test configuration
    print("=== EB-1A Opportunity System Configuration ===")
    
    # Test user profile creation
    default_profile = create_default_user_profile()
    print(f"Default Profile: {default_profile.name} ({default_profile.email})")
    print(f"Weak Criteria: {default_profile.weak_criteria}")
    print(f"Strong Criteria: {default_profile.strong_criteria}")
    
    # Test configuration validation
    validation = validate_config()
    print(f"\nConfiguration Validation:")
    print(f"Email Config: {'✓' if validation['email_config'] else '✗'}")
    print(f"Database Config: {'✓' if validation['database_config'] else '✗'}")
    print(f"User Profile: {'✓' if validation['user_profile'] else '✗'}")
    
    if validation["errors"]:
        print(f"Errors: {validation['errors']}")
    
    # Test opportunity categories
    print(f"\nOpportunity Categories: {list(OpportunityCategories.CATEGORIES.keys())}")
    
    # Test field keywords
    print(f"AI/ML Keywords: {SystemConfig.FIELD_KEYWORDS['AI/ML'][:3]}...")
    print(f"Cybersecurity Keywords: {SystemConfig.FIELD_KEYWORDS['Cybersecurity'][:3]}...")

