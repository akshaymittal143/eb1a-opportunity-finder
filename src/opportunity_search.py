"""
EB-1A Opportunity Search Module
Searches for opportunities across various sources and filters them based on user profile
"""

import requests
import re
from datetime import datetime, timedelta
from typing import List, Dict, Any
import json
from dataclasses import dataclass
from enum import Enum

class OpportunityType(Enum):
    SPEAKING = "speaking"
    JUDGING = "judging"
    MEDIA = "media"
    AWARDS = "awards"
    NETWORKING = "networking"
    WRITING = "writing"
    QUICK_WINS = "quick_wins"

@dataclass
class Opportunity:
    title: str
    type: OpportunityType
    description: str
    deadline: str
    link: str
    prestige_rating: int  # 1-5 stars
    evidence_value: int   # 1-5 stars
    time_investment: int  # 1-5 stars
    why_fits: str
    keywords: List[str]
    date_found: str

class OpportunitySearcher:
    def __init__(self, user_profile: Dict[str, Any]):
        self.user_profile = user_profile
        self.keywords = self._extract_keywords()
        
    def _extract_keywords(self) -> List[str]:
        """Extract search keywords from user profile"""
        base_keywords = [
            "AI", "ML", "Machine Learning", "Artificial Intelligence",
            "Cloud Native", "DevSecOps", "Cybersecurity", "Security",
            "Software Engineering", "PhD", "Research"
        ]
        
        # Add location-specific keywords if needed
        if self.user_profile.get('location'):
            base_keywords.extend([
                self.user_profile['location'],
                "remote", "virtual", "online"
            ])
            
        return base_keywords
    
    def search_call_for_papers(self) -> List[Opportunity]:
        """Search for call for papers opportunities"""
        opportunities = []
        
        # Simulate search results based on our research
        cfp_opportunities = [
            {
                "title": "Workshop-ai-in-space | AI ML Systems - Call for Papers Industry Track",
                "description": "AI/ML in Space, Industry Track",
                "deadline": "TBD - requires investigation",
                "link": "https://www.aimlsystems.org/2025/workshop-ai-in-space/",
                "keywords": ["AI", "ML", "Space", "Industry"]
            },
            {
                "title": "ENTECH Online - Call for Articles",
                "description": "AI, Cyber Security, Engineering, AR/VR, Computer Science, Robotics, IoT",
                "deadline": "Ongoing",
                "link": "https://entechonline.com/tag/ai/",
                "keywords": ["AI", "Cybersecurity", "Engineering"]
            },
            {
                "title": "IEEE Security & Privacy - Call for Papers",
                "description": "Leading cybersecurity research conference",
                "deadline": "December 15, 2025",
                "link": "https://www.ieee-security.org/TC/SP2025/",
                "keywords": ["Cybersecurity", "Research", "IEEE"]
            },
            {
                "title": "ACM CCS 2025 - Call for Papers",
                "description": "ACM Conference on Computer and Communications Security",
                "deadline": "January 15, 2025",
                "link": "https://www.sigsac.org/ccs/CCS2025/",
                "keywords": ["Cybersecurity", "ACM", "Research"]
            }
        ]
        
        for opp in cfp_opportunities:
            opportunity = Opportunity(
                title=opp["title"],
                type=OpportunityType.SPEAKING if "Papers" in opp["title"] else OpportunityType.WRITING,
                description=opp["description"],
                deadline=opp["deadline"],
                link=opp["link"],
                prestige_rating=4,
                evidence_value=4,
                time_investment=4,
                why_fits=f"Aligns with {', '.join(opp['keywords'])} expertise",
                keywords=opp["keywords"],
                date_found=datetime.now().strftime("%Y-%m-%d")
            )
            opportunities.append(opportunity)
            
        return opportunities
    
    def search_judging_opportunities(self) -> List[Opportunity]:
        """Search for judging opportunities"""
        opportunities = []
        
        judging_opportunities = [
            {
                "title": "Awards.AI - Become a Judge",
                "description": "Judge AI awards and competitions",
                "deadline": "Ongoing",
                "link": "https://awards.ai/judges/become-a-judge/",
                "keywords": ["AI", "Awards", "Judging"]
            },
            {
                "title": "Baishideng Publishing Group - Peer Reviewer",
                "description": "Peer review for academic journals",
                "deadline": "Ongoing",
                "link": "https://www.wjgnet.com/",
                "keywords": ["Peer Review", "Academic", "Research"]
            },
            {
                "title": "IEEE Transactions - Peer Reviewer",
                "description": "Peer review for IEEE cybersecurity journals",
                "deadline": "Ongoing",
                "link": "https://www.ieee.org/publications/",
                "keywords": ["Peer Review", "IEEE", "Cybersecurity"]
            },
            {
                "title": "ACM Digital Library - Peer Reviewer",
                "description": "Peer review for ACM computer science journals",
                "deadline": "Ongoing",
                "link": "https://www.acm.org/publications",
                "keywords": ["Peer Review", "ACM", "Computer Science"]
            }
        ]
        
        for opp in judging_opportunities:
            opportunity = Opportunity(
                title=opp["title"],
                type=OpportunityType.JUDGING,
                description=opp["description"],
                deadline=opp["deadline"],
                link=opp["link"],
                prestige_rating=4,
                evidence_value=4,
                time_investment=2 if "Awards.AI" in opp["title"] else 3,
                why_fits=f"Direct opportunity to fulfill judging criterion in {', '.join(opp['keywords'])}",
                keywords=opp["keywords"],
                date_found=datetime.now().strftime("%Y-%m-%d")
            )
            opportunities.append(opportunity)
            
        return opportunities
    
    def search_media_opportunities(self) -> List[Opportunity]:
        """Search for media opportunities"""
        opportunities = []
        
        media_opportunities = [
            {
                "title": "HARO - Help A Reporter Out",
                "description": "Respond to journalist queries for expert commentary",
                "deadline": "Daily",
                "link": "https://www.helpareporter.com/",
                "keywords": ["Media", "Expert Commentary", "Journalism"]
            },
            {
                "title": "Dark Reading - Expert Commentary",
                "description": "Cybersecurity threat intelligence commentary",
                "deadline": "Ongoing",
                "link": "https://www.darkreading.com/threat-intelligence",
                "keywords": ["Cybersecurity", "Media", "Commentary"]
            },
            {
                "title": "TechCrunch - Guest Contributor",
                "description": "Write guest articles on AI and cybersecurity",
                "deadline": "Ongoing",
                "link": "https://www.techcrunch.com/",
                "keywords": ["Media", "Writing", "Technology"]
            },
            {
                "title": "Wired - Expert Source",
                "description": "Provide expert commentary for technology articles",
                "deadline": "Ongoing",
                "link": "https://www.wired.com/",
                "keywords": ["Media", "Expert Commentary", "Technology"]
            }
        ]
        
        for opp in media_opportunities:
            opportunity = Opportunity(
                title=opp["title"],
                type=OpportunityType.MEDIA if "HARO" in opp["title"] else OpportunityType.MEDIA,
                description=opp["description"],
                deadline=opp["deadline"],
                link=opp["link"],
                prestige_rating=3 if "HARO" in opp["title"] else 4,
                evidence_value=4,
                time_investment=3,
                why_fits=f"Addresses weak media criterion through {', '.join(opp['keywords'])}",
                keywords=opp["keywords"],
                date_found=datetime.now().strftime("%Y-%m-%d")
            )
            opportunities.append(opportunity)
            
        return opportunities
    
    def search_award_opportunities(self) -> List[Opportunity]:
        """Search for award opportunities"""
        opportunities = []
        
        award_opportunities = [
            {
                "title": "CSO Conference + Awards 2025",
                "description": "Recognizes organizations for exceptional security projects",
                "deadline": "TBD - requires investigation",
                "link": "https://www.computerworld.com/events/",
                "keywords": ["Cybersecurity", "Awards", "Security Projects"]
            },
            {
                "title": "Stevie Awards - Technology",
                "description": "International business awards for technology innovation",
                "deadline": "March 15, 2025",
                "link": "https://www.stevieawards.com/",
                "keywords": ["Awards", "Technology", "Innovation"]
            },
            {
                "title": "Fast Company Innovation Awards",
                "description": "Recognition for innovative technology solutions",
                "deadline": "April 30, 2025",
                "link": "https://www.fastcompany.com/",
                "keywords": ["Awards", "Innovation", "Technology"]
            }
        ]
        
        for opp in award_opportunities:
            opportunity = Opportunity(
                title=opp["title"],
                type=OpportunityType.AWARDS,
                description=opp["description"],
                deadline=opp["deadline"],
                link=opp["link"],
                prestige_rating=4,
                evidence_value=4,
                time_investment=4,
                why_fits=f"Directly relevant to {', '.join(opp['keywords'])} expertise",
                keywords=opp["keywords"],
                date_found=datetime.now().strftime("%Y-%m-%d")
            )
            opportunities.append(opportunity)
            
        return opportunities
    
    def search_networking_opportunities(self) -> List[Opportunity]:
        """Search for networking opportunities"""
        opportunities = []
        
        networking_opportunities = [
            {
                "title": "AILive! 360 - Live! 360 Events",
                "description": "Major AI/ML and Cybersecurity networking event",
                "deadline": "November 21, 2025",
                "link": "https://live360events.com/events/orlando-2025/ailive.aspx",
                "keywords": ["AI", "ML", "Cybersecurity", "Networking"]
            },
            {
                "title": "Black Hat USA 2025",
                "description": "Premier cybersecurity conference and networking",
                "deadline": "August 5-8, 2025",
                "link": "https://www.blackhat.com/us-25/",
                "keywords": ["Cybersecurity", "Networking", "Conference"]
            },
            {
                "title": "RSA Conference 2025",
                "description": "World's leading cybersecurity conference",
                "deadline": "May 6-9, 2025",
                "link": "https://www.rsaconference.com/",
                "keywords": ["Cybersecurity", "Networking", "Conference"]
            }
        ]
        
        for opp in networking_opportunities:
            opportunity = Opportunity(
                title=opp["title"],
                type=OpportunityType.NETWORKING,
                description=opp["description"],
                deadline=opp["deadline"],
                link=opp["link"],
                prestige_rating=4,
                evidence_value=3,
                time_investment=4,
                why_fits=f"Networking with key players in {', '.join(opp['keywords'])} can lead to collaborations",
                keywords=opp["keywords"],
                date_found=datetime.now().strftime("%Y-%m-%d")
            )
            opportunities.append(opportunity)
            
        return opportunities
    
    def search_all_opportunities(self) -> List[Opportunity]:
        """Search all types of opportunities"""
        all_opportunities = []
        
        all_opportunities.extend(self.search_call_for_papers())
        all_opportunities.extend(self.search_judging_opportunities())
        all_opportunities.extend(self.search_media_opportunities())
        all_opportunities.extend(self.search_award_opportunities())
        all_opportunities.extend(self.search_networking_opportunities())
        
        return all_opportunities
    
    def filter_opportunities(self, opportunities: List[Opportunity], max_count: int = 10) -> List[Opportunity]:
        """Filter and rank opportunities based on user profile and criteria"""
        
        # Score opportunities based on multiple factors
        scored_opportunities = []
        
        for opp in opportunities:
            score = 0
            
            # Keyword relevance score
            keyword_matches = sum(1 for keyword in opp.keywords 
                                if any(uk.lower() in keyword.lower() for uk in self.keywords))
            score += keyword_matches * 2
            
            # Prestige and evidence value
            score += opp.prestige_rating + opp.evidence_value
            
            # Prefer opportunities that address weak criteria
            weak_criteria = ["judging", "media", "awards"]
            if opp.type.value in weak_criteria:
                score += 3
                
            # Time investment (lower is better for quick wins)
            if opp.type == OpportunityType.QUICK_WINS:
                score += (6 - opp.time_investment)  # Invert time investment for quick wins
            
            scored_opportunities.append((score, opp))
        
        # Sort by score (descending) and return top opportunities
        scored_opportunities.sort(key=lambda x: x[0], reverse=True)
        
        return [opp for score, opp in scored_opportunities[:max_count]]

def create_user_profile() -> Dict[str, Any]:
    """Create user profile based on the provided information"""
    return {
        "field": "Software Engineer, AI/ML research in Cloud Native, DevSecOps, Cybersecurity",
        "role": "Full Stack Software Engineer, doing AI/ML research as PhD Student",
        "location": "Austin, Texas, or Remote anywhere",
        "weak_criteria": ["judging", "media", "awards"],
        "strong_criteria": ["publications", "speaking", "critical role"],
        "keywords": ["AI", "ML", "Cloud Native", "DevSecOps", "Cybersecurity", "Software Engineering"]
    }

if __name__ == "__main__":
    # Test the opportunity searcher
    user_profile = create_user_profile()
    searcher = OpportunitySearcher(user_profile)
    
    opportunities = searcher.search_all_opportunities()
    filtered_opportunities = searcher.filter_opportunities(opportunities)
    
    print(f"Found {len(opportunities)} total opportunities")
    print(f"Filtered to top {len(filtered_opportunities)} opportunities")
    
    for i, opp in enumerate(filtered_opportunities, 1):
        print(f"\n{i}. {opp.title}")
        print(f"   Type: {opp.type.value}")
        print(f"   Rating: P:{opp.prestige_rating}/5, E:{opp.evidence_value}/5, T:{opp.time_investment}/5")
        print(f"   Why: {opp.why_fits}")

