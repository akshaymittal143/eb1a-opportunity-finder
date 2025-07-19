"""
EB-1A Email Templates Module
Comprehensive email templates for different scenarios and user preferences
"""

from typing import List, Dict, Any
from datetime import datetime
from src.opportunity_search import Opportunity, OpportunityType

class EmailTemplates:
    """Collection of email templates for different scenarios"""
    
    @staticmethod
    def get_daily_template() -> str:
        """Standard daily email template"""
        return """Subject: Daily EB-1A Opportunities - {date}

Dear {user_name},

Here are today's top {opportunity_count} opportunities to strengthen your extraordinary ability petition:

{opportunities}

## Quick Wins (15-30 min tasks):
{quick_wins}

## Long-term Opportunities Worth Tracking:
{long_term_opportunities}

## Action Items for Today:
- Review deadlines and add to your calendar
- Prioritize opportunities addressing your weak criteria: {weak_criteria}
- Consider your current workload and select 1-2 opportunities to pursue
- Track your response rate to improve future recommendations

## Your EB-1A Progress Tracker:
- Strong Criteria: {strong_criteria}
- Areas for Improvement: {weak_criteria}
- Opportunities Pursued This Month: {monthly_count}
- Success Rate: {success_rate}%

Best regards,
Your EB-1A Opportunity System

---
💡 Pro Tip: {daily_tip}

This email was generated automatically based on your profile. Reply with feedback to improve future recommendations.
Unsubscribe: {unsubscribe_link}
        """
    
    @staticmethod
    def get_weekly_summary_template() -> str:
        """Weekly summary email template"""
        return """Subject: Weekly EB-1A Summary - {week_range}

Dear {user_name},

Here's your weekly EB-1A opportunity summary:

## This Week's Highlights:
{weekly_highlights}

## Opportunities You Missed:
{missed_opportunities}

## Upcoming Deadlines (Next 7 Days):
{upcoming_deadlines}

## Your Progress This Week:
- Opportunities Identified: {opportunities_identified}
- Applications Submitted: {applications_submitted}
- Media Mentions Gained: {media_mentions}
- Speaking Engagements Secured: {speaking_engagements}

## Recommendations for Next Week:
{next_week_recommendations}

## Success Stories from Our Community:
{success_stories}

Keep up the excellent work!

Your EB-1A Opportunity System
        """
    
    @staticmethod
    def get_urgent_opportunity_template() -> str:
        """Template for urgent opportunities with tight deadlines"""
        return """Subject: 🚨 URGENT: High-Value EB-1A Opportunity - Deadline {deadline}

Dear {user_name},

We've identified a high-value opportunity that matches your profile perfectly, but it has a tight deadline:

## URGENT OPPORTUNITY:
{opportunity_details}

## Why This is Perfect for You:
{fit_analysis}

## Action Required:
{action_steps}

## Deadline: {deadline}
## Time Remaining: {time_remaining}

Don't miss this opportunity to strengthen your EB-1A petition!

Quick Apply: {quick_apply_link}

Your EB-1A Opportunity System
        """
    
    @staticmethod
    def get_success_follow_up_template() -> str:
        """Template for following up on successful applications"""
        return """Subject: 🎉 Congratulations! Next Steps for Your EB-1A Success

Dear {user_name},

Congratulations on your recent success with: {opportunity_name}

## What This Means for Your EB-1A Petition:
{impact_analysis}

## Next Steps to Maximize This Success:
{next_steps}

## Documentation Recommendations:
{documentation_tips}

## Related Opportunities to Consider:
{related_opportunities}

We're proud to be part of your EB-1A journey!

Your EB-1A Opportunity System
        """

class EmailPersonalizer:
    """Personalizes email content based on user profile and history"""
    
    def __init__(self, user_profile: Dict[str, Any], user_history: Dict[str, Any] = None):
        self.user_profile = user_profile
        self.user_history = user_history or {}
    
    def personalize_daily_email(self, opportunities: List[Opportunity]) -> str:
        """Personalize the daily email template"""
        template = EmailTemplates.get_daily_template()
        
        # Separate opportunities by type
        regular_opportunities = [opp for opp in opportunities if opp.type != OpportunityType.QUICK_WINS]
        quick_wins = [opp for opp in opportunities if opp.type == OpportunityType.QUICK_WINS]
        long_term = [opp for opp in opportunities if self._is_long_term(opp)]
        
        # Format opportunities
        formatted_opportunities = self._format_opportunities_list(regular_opportunities)
        formatted_quick_wins = self._format_quick_wins(quick_wins)
        formatted_long_term = self._format_long_term(long_term)
        
        # Get daily tip
        daily_tip = self._get_daily_tip()
        
        # Calculate stats
        monthly_count = self.user_history.get('monthly_applications', 0)
        success_rate = self.user_history.get('success_rate', 0)
        
        return template.format(
            date=datetime.now().strftime("%Y-%m-%d"),
            user_name=self.user_profile.get('name', 'EB-1A Candidate'),
            opportunity_count=len(regular_opportunities),
            opportunities=formatted_opportunities,
            quick_wins=formatted_quick_wins,
            long_term_opportunities=formatted_long_term,
            weak_criteria=', '.join(self.user_profile.get('weak_criteria', [])),
            strong_criteria=', '.join(self.user_profile.get('strong_criteria', [])),
            monthly_count=monthly_count,
            success_rate=success_rate,
            daily_tip=daily_tip,
            unsubscribe_link="[Unsubscribe Link]"
        )
    
    def _format_opportunities_list(self, opportunities: List[Opportunity]) -> str:
        """Format opportunities for email display"""
        if not opportunities:
            return "No new opportunities match your criteria today. Check back tomorrow!"
        
        formatted = []
        for i, opp in enumerate(opportunities, 1):
            type_name = opp.type.value.upper().replace("_", " ")
            stars_prestige = "★" * opp.prestige_rating + "☆" * (5 - opp.prestige_rating)
            stars_evidence = "★" * opp.evidence_value + "☆" * (5 - opp.evidence_value)
            stars_time = "★" * opp.time_investment + "☆" * (5 - opp.time_investment)
            
            formatted.append(f"""
{i}. {type_name}: {opp.title}
   📋 Topic: {opp.description}
   ⏰ Deadline: {opp.deadline}
   🔗 Link: {opp.link}
   ⭐ Rating: Prestige {stars_prestige} | Evidence {stars_evidence} | Time {stars_time}
   💡 Why it fits: {opp.why_fits}
            """.strip())
        
        return "\n\n".join(formatted)
    
    def _format_quick_wins(self, quick_wins: List[Opportunity]) -> str:
        """Format quick wins for email display"""
        if not quick_wins:
            return "• Sign up for HARO/ProfNet and respond to daily queries (15-30 min)\n• Apply to be a judge for industry awards (15 min application)\n• Update your LinkedIn with recent achievements (20 min)"
        
        formatted = []
        for opp in quick_wins:
            formatted.append(f"• {opp.title}: {opp.description} ({opp.link})")
        
        return "\n".join(formatted)
    
    def _format_long_term(self, long_term: List[Opportunity]) -> str:
        """Format long-term opportunities"""
        if not long_term:
            return "No long-term opportunities currently tracked."
        
        formatted = []
        for opp in long_term:
            formatted.append(f"• {opp.title} (Deadline: {opp.deadline}) - {opp.link}")
        
        return "\n".join(formatted)
    
    def _is_long_term(self, opp: Opportunity) -> bool:
        """Determine if an opportunity is long-term"""
        long_term_keywords = ["2025", "November", "December", "Annual", "Yearly"]
        return any(keyword in opp.deadline for keyword in long_term_keywords)
    
    def _get_daily_tip(self) -> str:
        """Get a daily tip based on user profile"""
        tips = [
            "Focus on opportunities that address your weak criteria first - they'll have the biggest impact on your petition.",
            "Quality over quantity - it's better to excel in a few opportunities than to spread yourself too thin.",
            "Document everything - keep detailed records of your contributions and their impact.",
            "Network strategically - the connections you make can lead to future opportunities.",
            "Stay consistent - small daily actions compound into significant achievements.",
            "Leverage your PhD research - many opportunities can tie back to your academic work.",
            "Consider remote opportunities - they expand your reach beyond Austin, Texas.",
            "Follow up professionally - many opportunities require persistent but respectful follow-up."
        ]
        
        # Simple rotation based on day of year
        day_of_year = datetime.now().timetuple().tm_yday
        return tips[day_of_year % len(tips)]

class HTMLEmailGenerator:
    """Generates HTML versions of emails with enhanced formatting"""
    
    @staticmethod
    def generate_html_daily_email(opportunities: List[Opportunity], user_profile: Dict[str, Any]) -> str:
        """Generate HTML version of daily email"""
        
        html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily EB-1A Opportunities</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .email-container {{
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 28px;
            font-weight: 300;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .content {{
            padding: 30px;
        }}
        .opportunity {{
            margin: 25px 0;
            padding: 20px;
            border-left: 5px solid #667eea;
            background-color: #f8f9ff;
            border-radius: 0 8px 8px 0;
        }}
        .opportunity h3 {{
            margin: 0 0 15px 0;
            color: #667eea;
            font-size: 20px;
        }}
        .opportunity-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin: 15px 0;
            font-size: 14px;
        }}
        .meta-item {{
            background-color: white;
            padding: 8px 12px;
            border-radius: 20px;
            border: 1px solid #e0e0e0;
        }}
        .rating {{
            color: #ff6b35;
            font-weight: bold;
        }}
        .link {{
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }}
        .link:hover {{
            text-decoration: underline;
        }}
        .section {{
            margin: 30px 0;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
        }}
        .section h2 {{
            margin: 0 0 15px 0;
            color: #333;
            font-size: 22px;
        }}
        .quick-wins {{
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border: none;
        }}
        .long-term {{
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            border: none;
        }}
        .progress-tracker {{
            background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%);
            border: none;
        }}
        .footer {{
            background-color: #333;
            color: white;
            padding: 20px 30px;
            text-align: center;
            font-size: 14px;
        }}
        .tip-box {{
            background-color: #e8f5e8;
            border-left: 4px solid #4caf50;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 5px 5px 0;
        }}
        .emoji {{
            font-size: 18px;
            margin-right: 8px;
        }}
        @media (max-width: 600px) {{
            .opportunity-meta {{
                flex-direction: column;
                gap: 10px;
            }}
            .content {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <h1>Daily EB-1A Opportunities</h1>
            <p>{date} • Personalized for {user_name}</p>
        </div>
        
        <div class="content">
            <p>Here are today's top opportunities to strengthen your extraordinary ability petition:</p>
            
            {opportunities_html}
            
            <div class="section quick-wins">
                <h2><span class="emoji">🚀</span>Quick Wins (15-30 min tasks)</h2>
                {quick_wins_html}
            </div>
            
            <div class="section long-term">
                <h2><span class="emoji">📅</span>Long-term Opportunities</h2>
                {long_term_html}
            </div>
            
            <div class="section progress-tracker">
                <h2><span class="emoji">📊</span>Your EB-1A Progress</h2>
                <p><strong>Strong Criteria:</strong> {strong_criteria}</p>
                <p><strong>Areas for Improvement:</strong> {weak_criteria}</p>
                <p><strong>Monthly Applications:</strong> {monthly_count}</p>
            </div>
            
            <div class="tip-box">
                <strong>💡 Pro Tip:</strong> {daily_tip}
            </div>
        </div>
        
        <div class="footer">
            <p>Your EB-1A Opportunity System • Powered by AI</p>
            <p><a href="#" style="color: #ccc;">Unsubscribe</a> | <a href="#" style="color: #ccc;">Update Preferences</a></p>
        </div>
    </div>
</body>
</html>"""
        
        # Generate content sections
        regular_opportunities = [opp for opp in opportunities if opp.type != OpportunityType.QUICK_WINS]
        quick_wins = [opp for opp in opportunities if opp.type == OpportunityType.QUICK_WINS]
        
        opportunities_html = HTMLEmailGenerator._format_opportunities_html(regular_opportunities)
        quick_wins_html = HTMLEmailGenerator._format_quick_wins_html(quick_wins)
        long_term_html = "<p>No long-term opportunities currently tracked.</p>"
        
        personalizer = EmailPersonalizer(user_profile)
        daily_tip = personalizer._get_daily_tip()
        
        return html_template.format(
            date=datetime.now().strftime("%B %d, %Y"),
            user_name=user_profile.get('name', 'EB-1A Candidate'),
            opportunities_html=opportunities_html,
            quick_wins_html=quick_wins_html,
            long_term_html=long_term_html,
            strong_criteria=', '.join(user_profile.get('strong_criteria', [])),
            weak_criteria=', '.join(user_profile.get('weak_criteria', [])),
            monthly_count=0,  # This would come from user history
            daily_tip=daily_tip
        )
    
    @staticmethod
    def _format_opportunities_html(opportunities: List[Opportunity]) -> str:
        """Format opportunities as HTML"""
        if not opportunities:
            return "<p>No new opportunities match your criteria today. Check back tomorrow!</p>"
        
        html_parts = []
        for i, opp in enumerate(opportunities, 1):
            type_name = opp.type.value.upper().replace("_", " ")
            stars_prestige = "★" * opp.prestige_rating + "☆" * (5 - opp.prestige_rating)
            stars_evidence = "★" * opp.evidence_value + "☆" * (5 - opp.evidence_value)
            stars_time = "★" * opp.time_investment + "☆" * (5 - opp.time_investment)
            
            html_parts.append(f"""
            <div class="opportunity">
                <h3>{i}. {type_name}: {opp.title}</h3>
                <p>{opp.description}</p>
                <div class="opportunity-meta">
                    <div class="meta-item">⏰ Deadline: {opp.deadline}</div>
                    <div class="meta-item rating">Prestige: {stars_prestige}</div>
                    <div class="meta-item rating">Evidence: {stars_evidence}</div>
                    <div class="meta-item rating">Time: {stars_time}</div>
                </div>
                <p><strong>Why it fits:</strong> {opp.why_fits}</p>
                <p><a href="{opp.link}" class="link">Apply Now →</a></p>
            </div>
            """)
        
        return "".join(html_parts)
    
    @staticmethod
    def _format_quick_wins_html(quick_wins: List[Opportunity]) -> str:
        """Format quick wins as HTML"""
        if not quick_wins:
            return """
            <ul>
                <li>Sign up for HARO/ProfNet and respond to daily queries (15-30 min)</li>
                <li>Apply to be a judge for industry awards (15 min application)</li>
                <li>Update your LinkedIn with recent achievements (20 min)</li>
            </ul>
            """
        
        html_parts = ["<ul>"]
        for opp in quick_wins:
            html_parts.append(f'<li><strong>{opp.title}:</strong> {opp.description} (<a href="{opp.link}" class="link">Start</a>)</li>')
        html_parts.append("</ul>")
        
        return "".join(html_parts)

if __name__ == "__main__":
    # Test the email templates
    from src.opportunity_search import OpportunitySearcher, create_user_profile
    
    user_profile = create_user_profile()
    user_profile['name'] = 'Dr. Alex Chen'  # Add a name for testing
    
    searcher = OpportunitySearcher(user_profile)
    opportunities = searcher.search_all_opportunities()
    filtered_opportunities = searcher.filter_opportunities(opportunities)
    
    # Test personalized email
    personalizer = EmailPersonalizer(user_profile)
    personalized_email = personalizer.personalize_daily_email(filtered_opportunities)
    
    print("=== PERSONALIZED DAILY EMAIL ===")
    print(personalized_email[:1000] + "..." if len(personalized_email) > 1000 else personalized_email)
    
    print("\n" + "="*50 + "\n")
    
    # Test HTML email
    html_email = HTMLEmailGenerator.generate_html_daily_email(filtered_opportunities, user_profile)
    print("=== HTML EMAIL (First 500 chars) ===")
    print(html_email[:500] + "...")

