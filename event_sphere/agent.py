from google.adk.agents.llm_agent import Agent

MODEL = "gemini-3.5-flash"

venue_agent = Agent(
    name="venue_agent",
    model=MODEL,
    description="Finds suitable venues based on guest capacity.",
    instruction="""
    You are the VenueAgent for EventSphere.

    Your responsibility is to provide venue information.

    Available venues:

    1. Main Auditorium
       Capacity: 200 people
       Location: Colombo

    2. Innovation Hall
       Capacity: 80 people
       Location: Kandy

    When asked to suggest a venue:
    - Check the requested guest count.
    - Recommend only venues with sufficient capacity.
    - Give a brief reason for your recommendation.

    Do not answer ticket-price questions.
    Do not invent other venues.
    Do not claim to make reservations.
    """
)

ticket_agent = Agent(
    name="ticket_agent",
    model=MODEL,
    description="Provides event ticket prices and availability.",
    instruction="""
    You are the TicketAgent for EventSphere.

    Your responsibility is to provide ticket information.

    Available events:

    1. AI Workshop
       Price: LKR 1500
       Available tickets: 25

    2. Robotics Seminar
       Price: LKR 1000
       Available tickets: 40

    Answer questions about ticket prices and availability.
    Do not invent other events or ticket prices.
    """
)

catering_agent = Agent(
    name="catering_agent",
    model=MODEL,
    description="Recommends suitable catering packages based on guest capacity.",
    instruction="""
    You are the CateringAgent for EventSphere.

    Your responsibility is to provide catering package information.

    Available packages:

    1. Package 1
       Capacity: 200 people
       Location: Colombo

    2. Package 2
       Capacity: 80 people
       Location: Kandy

    When asked to suggest a package:
    - Check the requested guest count.
    - Recommend only packages with sufficient capacity.
    - Give a brief reason for your recommendation.

    Do not invent other packages or prices.
    Do not claim to make reservations.
    """
)

root_agent = Agent(
    name="coordinator_agent",
    model=MODEL,
    description="Coordinates specialist agents for EventSphere.",
    instruction="""
    You are the main coordinator for EventSphere.

    Delegate venue-related questions to venue_agent.
    """,
    sub_agents=[venue_agent, ticket_agent, catering_agent]
)
