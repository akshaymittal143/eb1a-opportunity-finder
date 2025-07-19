# EB-1A Opportunity System Documentation

## Overview

The EB-1A Opportunity System is an automated daily email service designed to identify and deliver personalized opportunities to strengthen an extraordinary ability petition for the EB-1A green card category. The system focuses on opportunities in AI/ML, Cloud Native, DevSecOps, and Cybersecurity fields.

## System Architecture

### Core Components

1. **Opportunity Search Engine** (`opportunity_search.py`)
   - Searches across multiple sources for relevant opportunities
   - Filters and ranks opportunities based on user profile
   - Supports multiple opportunity types: speaking, judging, media, awards, networking, writing

2. **Email Formatting System** (`email_formatter.py`, `email_templates.py`)
   - Multiple email templates for different scenarios
   - HTML and plain text formats
   - Personalization based on user profile and history

3. **Configuration Management** (`config.py`)
   - Centralized configuration for all system components
   - User profile management
   - System-wide settings and constants

4. **Flask Web Application** (`main.py`)
   - Web interface for system management
   - API endpoints for configuration and testing
   - Database integration for user data and history

### Data Flow

```
User Profile → Opportunity Search → Filtering & Ranking → Email Generation → Delivery
```

## User Profile Configuration

The system uses a comprehensive user profile to personalize opportunity recommendations:

```python
UserProfile(
    name="Dr. Alex Chen",
    email="user@example.com",
    field="Software Engineer, AI/ML research in Cloud Native, DevSecOps, Cybersecurity",
    role="Full Stack Software Engineer, doing AI/ML research as PhD Student",
    location="Austin, Texas, or Remote anywhere",
    weak_criteria=["judging", "media", "awards"],
    strong_criteria=["publications", "speaking", "critical role"],
    keywords=["AI", "ML", "Cloud Native", "DevSecOps", "Cybersecurity"],
    notification_frequency=NotificationFrequency.DAILY,
    email_format=EmailFormat.HTML,
    max_opportunities_per_email=7
)
```

## Opportunity Types and EB-1A Criteria Mapping

### 1. SPEAKING Opportunities
- **EB-1A Criteria:** Speaking, Critical Role
- **Examples:** Conference presentations, keynote speeches, panel discussions
- **Evidence Value:** High
- **Time Investment:** Medium to High

### 2. JUDGING Opportunities
- **EB-1A Criteria:** Judging
- **Examples:** Peer review, editorial boards, competition judging
- **Evidence Value:** High
- **Time Investment:** Medium

### 3. MEDIA Opportunities
- **EB-1A Criteria:** Media
- **Examples:** Expert commentary, interviews, press quotes
- **Evidence Value:** Medium to High
- **Time Investment:** Low to Medium

### 4. AWARDS Opportunities
- **EB-1A Criteria:** Awards
- **Examples:** Industry recognition, achievement awards, honors
- **Evidence Value:** Very High
- **Time Investment:** Low to Medium

### 5. NETWORKING Opportunities
- **EB-1A Criteria:** Critical Role, Membership
- **Examples:** Professional associations, industry meetups, conferences
- **Evidence Value:** Low to Medium
- **Time Investment:** Medium

### 6. WRITING Opportunities
- **EB-1A Criteria:** Publications, Media
- **Examples:** Industry articles, blog posts, journal publications
- **Evidence Value:** Medium to High
- **Time Investment:** Medium to High

## Email Templates

### Daily Email Template
The standard daily email includes:
- Top 5-7 personalized opportunities
- Quick wins (15-30 minute tasks)
- Long-term opportunities worth tracking
- Progress tracker
- Daily tips for EB-1A success

### Weekly Summary Template
- Week's highlights and missed opportunities
- Upcoming deadlines
- Progress metrics
- Recommendations for next week

### Urgent Opportunity Template
- High-value opportunities with tight deadlines
- Immediate action required
- Quick apply links

### Success Follow-up Template
- Congratulations on successful applications
- Impact analysis for EB-1A petition
- Next steps and documentation recommendations

## Opportunity Scoring Algorithm

The system uses a weighted scoring algorithm to rank opportunities:

```python
score = (
    keyword_matches * 2.0 +
    prestige_rating * 1.5 +
    evidence_value * 1.5 +
    weak_criteria_bonus * 3.0 +
    (6 - time_investment) * 0.5 +
    deadline_urgency * 1.0
)
```

### Scoring Factors

1. **Keyword Relevance** (Weight: 2.0)
   - Matches between opportunity keywords and user profile
   - Field-specific keyword matching

2. **Prestige Rating** (Weight: 1.5)
   - Reputation of the organization/publication
   - International vs. national vs. local scope

3. **Evidence Value** (Weight: 1.5)
   - Strength of evidence for EB-1A petition
   - Documentation potential

4. **Weak Criteria Bonus** (Weight: 3.0)
   - Extra points for opportunities addressing weak criteria
   - Prioritizes areas needing improvement

5. **Time Investment** (Weight: 0.5, inverted)
   - Lower time investment gets higher score
   - Balances effort vs. reward

6. **Deadline Urgency** (Weight: 1.0)
   - Bonus for opportunities with approaching deadlines
   - Prevents missed opportunities

## Installation and Setup

### Prerequisites
- Python 3.11+
- Flask
- SQLite (for development)
- SMTP server access (for email delivery)

### Environment Variables
```bash
# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
FROM_EMAIL=eb1a-opportunities@yourdomain.com

# User Configuration
USER_NAME="Dr. Alex Chen"
USER_EMAIL=user@example.com
USER_FIELD="Software Engineer, AI/ML research"
USER_ROLE="Full Stack Software Engineer, PhD Student"
USER_LOCATION="Austin, Texas, or Remote"
WEAK_CRITERIA=judging,media,awards
STRONG_CRITERIA=publications,speaking,critical role
USER_KEYWORDS=AI,ML,Cloud Native,DevSecOps,Cybersecurity

# System Configuration
DATABASE_URL=sqlite:///eb1a_opportunities.db
LOG_LEVEL=INFO
CACHE_DIR=./cache
```

### Installation Steps

1. **Clone and Setup**
   ```bash
   cd eb1a-opportunity-system
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Initialize Database**
   ```bash
   python src/main.py
   # Database will be created automatically
   ```

4. **Test the System**
   ```bash
   python src/opportunity_search.py
   python src/email_templates.py
   ```

## API Endpoints

### GET /api/opportunities
Returns current opportunities for the user
```json
{
  "opportunities": [...],
  "count": 7,
  "last_updated": "2025-07-19T10:00:00Z"
}
```

### POST /api/send-email
Manually trigger email sending
```json
{
  "email_type": "daily",
  "user_email": "user@example.com"
}
```

### GET /api/user/profile
Get current user profile
```json
{
  "name": "Dr. Alex Chen",
  "email": "user@example.com",
  "weak_criteria": ["judging", "media", "awards"],
  "strong_criteria": ["publications", "speaking", "critical role"]
}
```

### PUT /api/user/profile
Update user profile
```json
{
  "name": "Dr. Alex Chen",
  "notification_frequency": "daily",
  "max_opportunities_per_email": 7
}
```

## Customization Options

### Adding New Opportunity Sources
1. Extend the `OpportunitySearcher` class
2. Add new search methods for specific sources
3. Update the `OPPORTUNITY_SOURCES` in config.py

### Custom Email Templates
1. Create new template methods in `EmailTemplates` class
2. Add corresponding HTML generators in `HTMLEmailGenerator`
3. Update the template selection logic

### Scoring Algorithm Modifications
1. Adjust weights in `SCORING_WEIGHTS` configuration
2. Add new scoring factors in the `filter_opportunities` method
3. Test with sample data to validate changes

## Monitoring and Analytics

### Key Metrics to Track
- Email open rates
- Click-through rates on opportunities
- Application success rates
- User engagement metrics
- System performance metrics

### Logging
The system logs all major operations:
- Opportunity searches and results
- Email generation and delivery
- User interactions
- System errors and warnings

### Performance Optimization
- Caching of search results (24-hour default)
- Rate limiting for external API calls
- Database query optimization
- Email template caching

## Troubleshooting

### Common Issues

1. **No Opportunities Found**
   - Check keyword configuration
   - Verify search sources are accessible
   - Review filtering criteria

2. **Email Delivery Issues**
   - Verify SMTP configuration
   - Check email credentials
   - Review spam folder settings

3. **Performance Issues**
   - Check cache configuration
   - Monitor API rate limits
   - Review database performance

### Debug Mode
Enable debug mode for detailed logging:
```bash
export LOG_LEVEL=DEBUG
python src/main.py
```

## Future Enhancements

### Planned Features
1. **Machine Learning Integration**
   - Personalized opportunity ranking
   - Success prediction models
   - Automated keyword extraction

2. **Advanced Search Capabilities**
   - Real-time web scraping
   - Social media monitoring
   - RSS feed integration

3. **Mobile Application**
   - Push notifications
   - Quick application features
   - Progress tracking

4. **Analytics Dashboard**
   - Success metrics visualization
   - Trend analysis
   - Comparative benchmarking

### Integration Opportunities
- Calendar integration for deadline tracking
- CRM integration for relationship management
- Document management for application tracking
- Social media integration for networking

## Support and Maintenance

### Regular Maintenance Tasks
- Update opportunity sources
- Refresh keyword lists
- Monitor email deliverability
- Update user profiles
- Review and update scoring algorithms

### Support Channels
- System logs for technical issues
- User feedback collection
- Performance monitoring
- Regular system health checks

## Security Considerations

### Data Protection
- Encrypted storage of user credentials
- Secure email transmission
- Regular security updates
- Access logging and monitoring

### Privacy Compliance
- User data minimization
- Consent management
- Data retention policies
- Right to deletion

This documentation provides a comprehensive guide to understanding, deploying, and maintaining the EB-1A Opportunity System. For additional support or feature requests, please refer to the system logs or contact the development team.

