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
    max_opportunities_per_email: int = 10
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
        "Networking event", "Professional association", "Industry meetup",
        "Call for submissions", "Call for proposals", "Call for speakers",
        "Call for judges", "Call for reviewers", "Call for experts",
        "Call for contributors", "Call for authors", "Call for presenters",
        "Call for panelists", "Call for moderators", "Call for mentors",
        "Call for advisors", "Call for consultants", "Call for specialists",
        "Call for thought leaders", "Call for influencers", "Call for advocates",
        "Call for ambassadors", "Call for champions", "Call for pioneers",
        "Call for innovators", "Call for researchers", "Call for practitioners",
        "Call for professionals", "Call for experts", "Call for specialists",
        "Call for consultants", "Call for advisors", "Call for mentors",
        "Call for coaches", "Call for trainers", "Call for educators",
        "Call for instructors", "Call for facilitators", "Call for moderators",
        "Call for hosts", "Call for emcees", "Call for presenters",
        "Call for speakers", "Call for panelists", "Call for discussants",
        "Call for participants", "Call for attendees", "Call for delegates",
        "Call for representatives", "Call for advocates", "Call for champions",
        "Call for ambassadors", "Call for spokespersons", "Call for representatives",
        "Call for delegates", "Call for participants", "Call for contributors",
        "Call for authors", "Call for writers", "Call for bloggers",
        "Call for journalists", "Call for reporters", "Call for correspondents",
        "Call for editors", "Call for publishers", "Call for distributors",
        "Call for marketers", "Call for promoters", "Call for advertisers",
        "Call for sponsors", "Call for partners", "Call for collaborators",
        "Call for co-authors", "Call for co-presenters", "Call for co-moderators",
        "Call for co-facilitators", "Call for co-trainers", "Call for co-instructors",
        "Call for co-educators", "Call for co-coaches", "Call for co-mentors",
        "Call for co-advisors", "Call for co-consultants", "Call for co-specialists",
        "Call for co-experts", "Call for co-professionals", "Call for co-practitioners",
        "Call for co-researchers", "Call for co-innovators", "Call for co-pioneers",
        "Call for co-champions", "Call for co-ambassadors", "Call for co-advocates",
        "Call for co-influencers", "Call for co-thought leaders", "Call for co-specialists",
        "Call for co-consultants", "Call for co-advisors", "Call for co-mentors",
        "Call for co-coaches", "Call for co-trainers", "Call for co-educators",
        "Call for co-instructors", "Call for co-facilitators", "Call for co-moderators",
        "Call for co-presenters", "Call for co-speakers", "Call for co-panelists",
        "Call for co-discussants", "Call for co-participants", "Call for co-attendees",
        "Call for co-delegates", "Call for co-representatives", "Call for co-advocates",
        "Call for co-champions", "Call for co-ambassadors", "Call for co-spokespersons",
        "Call for co-representatives", "Call for co-delegates", "Call for co-participants",
        "Call for co-contributors", "Call for co-authors", "Call for co-writers",
        "Call for co-bloggers", "Call for co-journalists", "Call for co-reporters",
        "Call for co-correspondents", "Call for co-editors", "Call for co-publishers",
        "Call for co-distributors", "Call for co-marketers", "Call for co-promoters",
        "Call for co-advertisers", "Call for co-sponsors", "Call for co-partners",
        "Call for co-collaborators", "Call for co-authors", "Call for co-presenters",
        "Call for co-moderators", "Call for co-facilitators", "Call for co-trainers",
        "Call for co-instructors", "Call for co-educators", "Call for co-coaches",
        "Call for co-mentors", "Call for co-advisors", "Call for co-consultants",
        "Call for co-specialists", "Call for co-experts", "Call for co-professionals",
        "Call for co-practitioners", "Call for co-researchers", "Call for co-innovators",
        "Call for co-pioneers", "Call for co-champions", "Call for co-ambassadors",
        "Call for co-advocates", "Call for co-influencers", "Call for co-thought leaders"
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
            "https://www.allconferences.com/",
            "https://www.papercrowd.com/",
            "https://easychair.org/cfp/",
            "https://www.researchr.org/conferences/",
            "https://www.sciencedz.net/en/conference/",
            "https://www.conferencealerts.com/",
            "https://www.ieee.org/conferences_events/index.html",
            "https://www.springer.com/gp/computer-science/lncs/conference-proceedings",
            "https://www.nature.com/natureevents/science/events",
            "https://www.eventbrite.com/d/online/academic-conference/",
            "https://www.academic-conferences.org/",
            "https://www.elsevier.com/events/conferences",
            "https://www.oxfordabstracts.com/events",
            "https://www.exordo.com/conferences/",
            "https://www.cvent.com/en/conferences",
            "https://www.universe.com/events/academic",
            "https://www.eventsinamerica.com/education/academic",
            "https://www.grantforward.com/",
            "https://www.higheredjobs.com/faculty/search.cfm",
            "https://www.academicpositions.com/",
            "https://www.academiceventlist.com/",
            "https://www.findaphd.com/phds/events/",
            "https://www.timeshighereducation.com/unijobs/listings/academic/",
            "https://www.academics.com/science-jobs",
            "https://www.scholarshipportal.com/",
            "https://www.researchgate.net/jobs",
            "https://www.academicgates.com/",
            "https://www.call4papers.info/",
            "https://www.conferencecalendar.com/",
            "https://www.conferenceindex.org/",
            "https://www.conference-locator.com/",
            "https://www.conferencealerts.com/",
            "https://www.callforpapers.co/",
            "https://www.cfpcalendar.com/",
            "https://www.conference-service.com/",
            "https://www.researchgate.net/events",
            "https://www.academia.edu/events",
            "https://www.scholar.google.com/",
            "https://www.semanticscholar.org/",
            "https://www.arxiv.org/",
            "https://www.biorxiv.org/",
            "https://www.medrxiv.org/",
            "https://waset.org/",
            "https://www.guide2research.com/",
            "https://www.acm.org/conferences"
        ],
        "media": [
            "https://www.helpareporter.com/",
            "https://profnet.prnewswire.com/",
            "https://www.sourcebottle.com/",
            "https://www.expertfile.com/",
            "https://www.qwoted.com/",
            "https://www.journalistrequest.com/",
            "https://www.expertisefinder.com/",
            "https://www.matchmaker.fm/",
            "https://www.radioguestlist.com/",
            "https://www.podcastguests.com/",
            "https://www.medialist.io/",
            "https://www.experts.com/",
            "https://www.speakermatch.com/",
            "https://www.speakerhub.com/",
            "https://www.bullhorn.com/blog/media-opportunities/",
            "https://www.muckrack.com/",
            "https://www.prnewswire.com/",
            "https://www.businesswire.com/",
            "https://www.newswise.com/",
            "https://www.expertclick.com/",
            "https://www.talkers.com/",
            "https://www.theopennotebook.com/pitch-database/",
            "https://www.freelancewriting.com/journalism/media-contacts/",
            "https://www.journalism.co.uk/media-database/s43/",
            "https://www.pressrush.com/",
            "https://www.presshunt.co/",
            "https://www.presscontact.co/",
            "https://www.mediacontactslist.com/",
            "https://www.rosterfy.com/blog/media-opportunities",
            "https://www.podchaser.com/creators",
            "https://www.harojournalist.com/",
            "https://www.helpareporterout.com/",
            "https://www.terkel.io/",
            "https://www.answerthepublic.com/",
            "https://www.quora.com/",
            "https://www.reddit.com/r/IAmA/",
            "https://www.linkedin.com/pulse/",
            "https://www.medium.com/",
            "https://www.substack.com/",
            "https://www.techcrunch.com/",
            "https://www.wired.com/",
            "https://www.theverge.com/",
            "https://www.ars-technica.com/",
            "https://www.venturebeat.com/",
            "https://www.thenextweb.com/",
            "https://www.readwrite.com/",
            "https://www.techrepublic.com/",
            "https://www.zdnet.com/",
            "https://www.cnet.com/",
            "https://www.engadget.com/",
            "https://www.gizmodo.com/",
            "https://www.mashable.com/",
            "https://www.digitaltrends.com/",
            "https://www.expertbeacon.com/",
            "https://www.presshunt.com/",
            "https://www.featuredexperts.com/",
            "https://www.responsesource.com/",
            "https://journorequest.com/"
        ],
        "awards": [
            "https://awards.ai/",
            "https://www.computerworld.com/events/",
            "https://www.cybersecurityexcellenceawards.com/",
            "https://www.stevieawards.com/",
            "https://www.globeeawards.com/",
            "https://www.iaawards.org/",
            "https://www.technologyawards.org/",
            "https://www.aitop100.com/",
            "https://www.innovationawardshub.com/",
            "https://www.efma.com/awards",
            "https://www.elsevier.com/awards",
            "https://www.ieee.org/about/awards/index.html",
            "https://www.acm.org/awards",
            "https://www.fastcompany.com/most-innovative-companies",
            "https://www.forbes.com/innovation-awards/",
            "https://www.inc.com/inc5000",
            "https://www.americanbusinessawards.com/",
            "https://www.thetieawards.com/",
            "https://www.globalbankingandfinance.com/awards/",
            "https://www.womenintechawards.com/",
            "https://www.edisonawards.com/",
            "https://www.risingstarsawards.com/",
            "https://www.royalsociety.org/grants-schemes-awards/awards/",
            "https://www.nationalmedals.org/",
            "https://www.nsf.gov/awards/managing/",
            "https://www.elsevier.com/awards/global-awards",
            "https://www.ashoka.org/en-us/awards",
            "https://www.aaas.org/awards",
            "https://www.royalacademy.org.uk/awards",
            "https://www.technologyreview.com/innovators-under-35/",
            "https://www.techcrunch.com/disrupt/",
            "https://www.sxsw.com/awards/",
            "https://www.ces.tech/Innovation-Awards/",
            "https://www.webbyawards.com/",
            "https://www.shortyawards.com/",
            "https://www.canneslions.com/",
            "https://www.clioawards.com/",
            "https://www.one-show.org/",
            "https://www.dandad.org/awards/",
            "https://www.behance.net/awards",
            "https://www.awwwards.com/",
            "https://www.cssdesignawards.com/",
            "https://www.fwa.com/",
            "https://www.thefwa.com/",
            "https://www.smashingmagazine.com/awards/",
            "https://www.csswinner.com/",
            "https://www.cssreel.com/",
            "https://www.cssmania.com/",
            "https://www.cssdesignawards.com/",
            "https://www.csswinner.com/",
            "https://www.cssreel.com/",
            "https://www.cssmania.com/",
            "https://www.techcrunch.com/events/",
            "https://www.crunchbase.com/lists/",
            "https://www.forbes.com/lists/",
            "https://www.inc.com/best-in-business/",
            "https://www.fastcompany.com/most-innovative-companies/",
            "https://www.entrepreneur.com/franchises/topfranchises/",
            "https://www.businessinsider.com/sai-100/",
            "https://www.mit.com/innovators-under-35/",
            "https://www.technologyreview.com/lists/innovators-under-35/",
            "https://www.worldtechnologyawards.com/",
            "https://www.webbyawards.com/",
            "https://www.innovationawards.com/"
        ],
        "networking": [
            "https://www.meetup.com/",
            "https://www.eventbrite.com/",
            "https://live360events.com/",
            "https://www.linkedin.com/events/",
            "https://hopin.com/events",
            "https://www.bizzabo.com/events",
            "https://www.confabb.com/",
            "https://www.eventful.com/",
            "https://www.universe.com/",
            "https://www.splashthat.com/",
            "https://www.ti.to/",
            "https://www.eventzilla.net/",
            "https://www.10times.com/",
            "https://www.eventdex.com/",
            "https://www.eventleaf.com/",
            "https://www.cvent.com/en/event-management-software",
            "https://www.eventscase.com/",
            "https://www.eventbrite.co.uk/d/online/networking--events/",
            "https://www.eventbrite.com/d/online/tech-meetup/",
            "https://www.eventbrite.com/d/online/professional-networking/",
            "https://www.techmeme.com/events",
            "https://www.techconferences.com/",
            "https://www.startupgrind.com/events/",
            "https://www.womenwhocode.com/events",
            "https://www.devopsdays.org/events/",
            "https://www.producthunt.com/events",
            "https://www.eventfinda.com/",
            "https://www.eventkeeper.com/",
            "https://www.eventbrite.com/d/online/ai-events/",
            "https://www.eventbrite.com/d/online/cloud-events/",
            "https://www.slack.com/",
            "https://www.discord.com/",
            "https://www.telegram.org/",
            "https://www.signal.org/",
            "https://www.clubhouse.com/",
            "https://www.tiktok.com/",
            "https://www.youtube.com/",
            "https://www.twitch.tv/",
            "https://www.reddit.com/",
            "https://www.hackernews.com/",
            "https://www.stackoverflow.com/",
            "https://www.github.com/",
            "https://www.gitlab.com/",
            "https://www.bitbucket.org/",
            "https://www.docker.com/",
            "https://www.kubernetes.io/",
            "https://www.aws.amazon.com/",
            "https://www.azure.microsoft.com/",
            "https://www.cloud.google.com/",
            "https://www.techcrunch.com/events/",
            "https://events.venturebeat.com/",
            "https://www.sxsw.com/",
            "https://www.tedxtalks.ted.com/",
            "https://www.ted.com/",
            "https://www.facebook.com/events/",
            "https://www.crunchbase.com/events/",
            "https://www.angellist.com/events",
            "https://www.producthunt.com/events"
        ],
        "writing": [
            "https://www.medium.com/",
            "https://www.substack.com/",
            "https://www.hashnode.com/",
            "https://www.dev.to/",
            "https://www.hackernoon.com/",
            "https://www.towardsdatascience.com/",
            "https://www.analyticsvidhya.com/",
            "https://www.kdnuggets.com/",
            "https://www.datasciencecentral.com/",
            "https://www.oreilly.com/",
            "https://www.packtpub.com/",
            "https://www.apress.com/",
            "https://www.manning.com/",
            "https://www.pearson.com/",
            "https://www.mcgraw-hill.com/",
            "https://www.wiley.com/",
            "https://www.springer.com/",
            "https://www.elsevier.com/",
            "https://www.ieee.org/publications/",
            "https://www.acm.org/publications/",
            "https://www.usenix.org/publications/",
            "https://www.usenix.org/conferences/",
            "https://www.sigcomm.org/publications/",
            "https://www.sigchi.org/publications/",
            "https://www.sigkdd.org/publications/",
            "https://www.sigmod.org/publications/",
            "https://www.siggraph.org/publications/",
            "https://www.sigir.org/publications/",
            "https://www.sigsoft.org/publications/",
            "https://www.sigplan.org/publications/",
            "https://www.sigops.org/publications/",
            "https://www.sigarch.org/publications/",
            "https://www.sigmobile.org/publications/",
            "https://www.sigmetrics.org/publications/",
            "https://www.sigcomm.org/publications/",
            "https://www.sigchi.org/publications/",
            "https://www.sigkdd.org/publications/",
            "https://www.sigmod.org/publications/",
            "https://www.siggraph.org/publications/",
            "https://www.sigir.org/publications/",
            "https://www.sigsoft.org/publications/",
            "https://www.sigplan.org/publications/",
            "https://www.sigops.org/publications/",
            "https://www.sigarch.org/publications/",
            "https://www.sigmobile.org/publications/",
            "https://www.sigmetrics.org/publications/"
        ],
        "speaking": [
            "https://www.ted.com/tedx",
            "https://www.speakerhub.com/",
            "https://www.speakermatch.com/",
            "https://www.speakerbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/"
        ],
        "judging": [
            "https://www.judges.org/",
            "https://www.judge.com/",
            "https://www.judging.org/",
            "https://www.judge.org/",
            "https://www.judges.com/",
            "https://www.judge.net/",
            "https://www.judging.net/",
            "https://www.judge.info/",
            "https://www.judges.info/",
            "https://www.judge.co/",
            "https://www.judges.co/",
            "https://www.judging.co/",
            "https://www.judge.io/",
            "https://www.judges.io/",
            "https://www.judging.io/",
            "https://www.judge.dev/",
            "https://www.judges.dev/",
            "https://www.judging.dev/",
            "https://www.judge.tech/",
            "https://www.judges.tech/",
            "https://www.judging.tech/",
            "https://www.judge.ai/",
            "https://www.judges.ai/",
            "https://www.judging.ai/",
            "https://www.judge.cloud/",
            "https://www.judges.cloud/",
            "https://www.judging.cloud/",
            "https://www.judge.app/",
            "https://www.judges.app/",
            "https://www.judging.app/",
            "https://www.techcrunch.com/startup-battlefield/",
            "https://www.angelpad.com/",
            "https://www.ycombinator.com/",
            "https://www.500startups.com/",
            "https://techstars.com/",
            "https://www.seedcamp.com/",
            "https://www.kaggle.com/competitions",
            "https://devpost.com/",
            "https://www.hackerearth.com/challenges/",
            "https://www.topcoder.com/"
        ],
        "speaking": [
            "https://www.ted.com/tedx",
            "https://www.speakerhub.com/",
            "https://www.speakermatch.com/",
            "https://www.speakerbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/",
            "https://www.speakers.com/",
            "https://www.allamericanspeakers.com/",
            "https://www.celebrityspeakers.com/",
            "https://www.speakerscorner.co.uk/",
            "https://www.speakers.co.uk/",
            "https://www.speakersbureau.com/",
            "https://www.papercall.io/",
            "https://www.cfpland.com/",
            "https://speaking.io/",
            "https://www.callforpapers.com/",
            "https://www.eventil.com/",
            "https://sessionize.com/",
            "https://speakerdeck.com/",
            "https://www.lanyrd.com/calls/",
            "https://www.speakerfile.com/",
            "https://www.gpspeakers.com/"
        ],
        "professional": [
            "https://www.linkedin.com/",
            "https://www.upwork.com/",
            "https://www.freelancer.com/",
            "https://www.toptal.com/",
            "https://www.99designs.com/",
            "https://dribbble.com/",
            "https://www.behance.net/",
            "https://github.com/",
            "https://stackoverflow.com/",
            "https://www.kaggle.com/"
        ],
        "publications": [
            "https://scholar.google.com/",
            "https://www.researchgate.net/",
            "https://www.academia.edu/",
            "https://arxiv.org/",
            "https://www.nature.com/",
            "https://www.sciencemag.org/",
            "https://ieeexplore.ieee.org/",
            "https://www.acm.org/publications",
            "https://www.springer.com/",
            "https://www.elsevier.com/",
            "https://medium.com/",
            "https://dev.to/",
            "https://www.hackernoon.com/",
            "https://towardsdatascience.com/"
        ],
        "patents": [
            "https://patents.google.com/",
            "https://www.uspto.gov/",
            "https://worldwide.espacenet.com/",
            "https://www.wipo.int/portal/en/",
            "https://www.freepatentsonline.com/",
            "https://patentscope.wipo.int/"
        ],
        "industry_recognition": [
            "https://www.gartner.com/",
            "https://www.forrester.com/",
            "https://www.mckinsey.com/",
            "https://www2.deloitte.com/",
            "https://www.bcg.com/",
            "https://www.pwc.com/",
            "https://www.accenture.com/",
            "https://www.ey.com/",
            "https://www.kpmg.com/"
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
        },
        "professional": {
            "keywords": ["freelance", "consulting", "contract", "project", "collaboration"],
            "evidence_value": "Medium",
            "typical_time_investment": "Medium to High",
            "eb1a_criteria": ["critical role", "original contributions"]
        },
        "publications": {
            "keywords": ["research", "paper", "journal", "conference", "publication"],
            "evidence_value": "Very High",
            "typical_time_investment": "High",
            "eb1a_criteria": ["publications", "original contributions"]
        },
        "patents": {
            "keywords": ["patent", "invention", "innovation", "intellectual property", "IP"],
            "evidence_value": "Very High",
            "typical_time_investment": "Very High",
            "eb1a_criteria": ["original contributions", "awards"]
        },
        "industry_recognition": {
            "keywords": ["industry", "recognition", "expert", "thought leader", "influencer"],
            "evidence_value": "High",
            "typical_time_investment": "Medium",
            "eb1a_criteria": ["critical role", "original contributions"]
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
        max_opportunities_per_email=10,
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
        max_opportunities_per_email=int(os.getenv('MAX_OPPORTUNITIES', '10')),
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
    
    # Validate email configuration - read directly from environment
    email_username = os.getenv('EMAIL_USERNAME')
    email_password = os.getenv('EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    
    if email_username and email_password and smtp_server:
        validation_results["email_config"] = True
    else:
        validation_results["errors"].append("Email credentials not configured")
    
    # Validate database configuration
    database_url = os.getenv('DATABASE_URL', 'sqlite:///eb1a_opportunities.db')
    if database_url:
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

