"""
EB-1A Email Formatter Module
Formats opportunities into daily email format
"""

from typing import List
from datetime import datetime
from src.opportunity_search import Opportunity, OpportunityType

class EmailFormatter:
    def __init__(self):
        self.template = self._load_email_template()
    
    def _load_email_template(self) -> str:
        """Load the email template"""
        return """
Subject: Daily EB-1A Opportunities - {date}

Dear EB-1A Candidate,

Here are today's top opportunities to strengthen your extraordinary ability petition:

{opportunities}

## Long-term Opportunities:
{long_term_opportunities}

## Quick Action Items:
- Review deadlines and mark your calendar
- Prioritize opportunities that address your weak criteria: judging, media, awards
- Track your response rate to improve future suggestions

Best regards,
EB-1A Opportunity System

---
This email was generated automatically. Reply with feedback to improve future recommendations.
        """.strip()
    
    def format_opportunity(self, opp: Opportunity, index: int) -> str:
        """Format a single opportunity"""
        type_mapping = {
            OpportunityType.SPEAKING: "SPEAKING",
            OpportunityType.JUDGING: "JUDGING", 
            OpportunityType.MEDIA: "MEDIA",
            OpportunityType.AWARDS: "AWARDS",
            OpportunityType.NETWORKING: "NETWORKING",
            OpportunityType.WRITING: "WRITING",
            OpportunityType.QUICK_WINS: "QUICK WINS"
        }
        
        stars = "★" * opp.prestige_rating + "☆" * (5 - opp.prestige_rating)
        
        formatted = f"""
**{index}. {type_mapping[opp.type]}:** {opp.title}
- **Topic/Field:** {opp.description}
- **Deadline:** {opp.deadline}
- **Link:** {opp.link}
- **Rating:** Prestige: {stars}, Evidence Value: {"★" * opp.evidence_value}{"☆" * (5 - opp.evidence_value)}, Time Investment: {"★" * opp.time_investment}{"☆" * (5 - opp.time_investment)}
- **Why it fits:** {opp.why_fits}
        """.strip()
        
        return formatted
    
    def format_daily_email(self, opportunities: List[Opportunity]) -> str:
        """Format the complete daily email"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Separate quick wins from regular opportunities
        regular_opportunities = [opp for opp in opportunities if opp.type != OpportunityType.QUICK_WINS]
        quick_wins = [opp for opp in opportunities if opp.type == OpportunityType.QUICK_WINS]
        
        # Format regular opportunities
        formatted_opportunities = []
        for i, opp in enumerate(regular_opportunities, 1):
            formatted_opportunities.append(self.format_opportunity(opp, i))
        
        # Format quick wins
        formatted_quick_wins = []
        for opp in quick_wins:
            formatted_quick_wins.append(f"- {opp.title}: {opp.description} ({opp.link})")
        
        # Long-term opportunities (those with deadlines far in the future)
        long_term = [opp for opp in opportunities if self._is_long_term(opp)]
        formatted_long_term = []
        for opp in long_term:
            formatted_long_term.append(f"- {opp.title} (Deadline: {opp.deadline}) - {opp.link}")
        
        opportunities_text = "\n\n".join(formatted_opportunities)
        quick_wins_text = "\n".join(formatted_quick_wins) if formatted_quick_wins else "No quick wins available today."
        long_term_text = "\n".join(formatted_long_term) if formatted_long_term else "No long-term opportunities tracked."
        
        return self.template.format(
            date=today,
            opportunities=opportunities_text,
            long_term_opportunities=long_term_text
        ) + f"\n\n## Quick Wins (15-30 min tasks):\n{quick_wins_text}"
    
    def _is_long_term(self, opp: Opportunity) -> bool:
        """Determine if an opportunity is long-term"""
        # Simple heuristic: if deadline is more than 30 days away or contains certain keywords
        long_term_keywords = ["2025", "November", "December", "Annual", "Yearly"]
        return any(keyword in opp.deadline for keyword in long_term_keywords)
    
    def format_html_email(self, opportunities: List[Opportunity]) -> str:
        """Format email as HTML for better presentation"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        html_template = """<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .header {{ background-color: #f4f4f4; padding: 20px; border-radius: 5px; }}
        .opportunity {{ margin: 20px 0; padding: 15px; border-left: 4px solid #007cba; background-color: #f9f9f9; }}
        .rating {{ color: #ff6b35; }}
        .link {{ color: #007cba; text-decoration: none; }}
        .quick-wins {{ background-color: #e8f5e8; padding: 15px; border-radius: 5px; }}
        .long-term {{ background-color: #fff3cd; padding: 15px; border-radius: 5px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Daily EB-1A Opportunities - {date}</h1>
        <p>Your personalized opportunities to strengthen your extraordinary ability petition</p>
    </div>
    
    <div class="content">
        {opportunities_html}
    </div>
    
    <div class="quick-wins">
        <h2>🚀 Quick Wins (15-30 min tasks)</h2>
        {quick_wins_html}
    </div>
    
    <div class="long-term">
        <h2>📅 Long-term Opportunities</h2>
        {long_term_html}
    </div>
    
    <hr>
    <p><small>This email was generated automatically. Track your progress and provide feedback to improve future recommendations.</small></p>
</body>
</html>"""
        
        # Format opportunities as HTML
        opportunities_html = ""
        regular_opportunities = [opp for opp in opportunities if opp.type != OpportunityType.QUICK_WINS]
        
        for i, opp in enumerate(regular_opportunities, 1):
            type_name = opp.type.value.upper().replace("_", " ")
            stars_prestige = "★" * opp.prestige_rating + "☆" * (5 - opp.prestige_rating)
            stars_evidence = "★" * opp.evidence_value + "☆" * (5 - opp.evidence_value)
            stars_time = "★" * opp.time_investment + "☆" * (5 - opp.time_investment)
            
            opportunities_html += f"""
            <div class="opportunity">
                <h3>{i}. {type_name}: {opp.title}</h3>
                <p><strong>Topic/Field:</strong> {opp.description}</p>
                <p><strong>Deadline:</strong> {opp.deadline}</p>
                <p><strong>Link:</strong> <a href="{opp.link}" class="link">{opp.link}</a></p>
                <p class="rating"><strong>Rating:</strong> Prestige: {stars_prestige}, Evidence: {stars_evidence}, Time: {stars_time}</p>
                <p><strong>Why it fits:</strong> {opp.why_fits}</p>
            </div>
            """
        
        # Format quick wins
        quick_wins = [opp for opp in opportunities if opp.type == OpportunityType.QUICK_WINS]
        quick_wins_html = ""
        for opp in quick_wins:
            quick_wins_html += f'<p>• <strong>{opp.title}:</strong> {opp.description} (<a href="{opp.link}" class="link">Apply</a>)</p>'
        
        if not quick_wins_html:
            quick_wins_html = "<p>No quick wins available today.</p>"
        
        # Format long-term opportunities
        long_term = [opp for opp in opportunities if self._is_long_term(opp)]
        long_term_html = ""
        for opp in long_term:
            long_term_html += f'<p>• <strong>{opp.title}</strong> (Deadline: {opp.deadline}) - <a href="{opp.link}" class="link">Details</a></p>'
        
        if not long_term_html:
            long_term_html = "<p>No long-term opportunities tracked.</p>"
        
        return html_template.format(
            date=today,
            opportunities_html=opportunities_html,
            quick_wins_html=quick_wins_html,
            long_term_html=long_term_html
        )

if __name__ == "__main__":
    # Test the email formatter
    from src.opportunity_search import OpportunitySearcher, create_user_profile
    
    user_profile = create_user_profile()
    searcher = OpportunitySearcher(user_profile)
    opportunities = searcher.search_all_opportunities()
    filtered_opportunities = searcher.filter_opportunities(opportunities)
    
    formatter = EmailFormatter()
    
    # Test plain text email
    plain_email = formatter.format_daily_email(filtered_opportunities)
    print("=== PLAIN TEXT EMAIL ===")
    print(plain_email)
    
    print("\n" + "="*50 + "\n")
    
    # Test HTML email
    html_email = formatter.format_html_email(filtered_opportunities)
    print("=== HTML EMAIL ===")
    print(html_email[:500] + "..." if len(html_email) > 500 else html_email)

