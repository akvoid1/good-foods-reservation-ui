from typing import List, Dict, Any


# Tool definitions for LLM function calling
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_venues",
            "description": "Search for restaurants based on criteria like cuisine, location, party size, and preferences. Use this when users ask to find restaurants.",
            "parameters": {
                "type": "object",
                "properties": {
                    "cuisine": {
                        "type": "string",
                        "description": "Type of cuisine (e.g., Italian, Indian, Chinese, French). Leave empty if not specified."
                    },
                    "city": {
                        "type": "string",
                        "description": "City or location. Leave empty if not specified."
                    }
                },
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_venue_details",
            "description": "Get detailed information about a specific restaurant",
            "parameters": {
                "type": "object",
                "properties": {
                    "venue_id": {
                        "type": "string",
                        "description": "The unique ID of the venue"
                    }
                },
                "required": ["venue_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_availability",
            "description": "Check if a restaurant has availability for a specific date, time, and party size",
            "parameters": {
                "type": "object",
                "properties": {
                    "venue_id": {
                        "type": "string",
                        "description": "The unique ID of the venue"
                    },
                    "datetime": {
                        "type": "string",
                        "description": "Date and time in ISO format (e.g., 2024-12-25T19:00:00)"
                    },
                    "party_size": {
                        "type": "integer",
                        "description": "Number of people"
                    }
                },
                "required": ["venue_id", "datetime", "party_size"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_reservation",
            "description": "Create a reservation at a restaurant",
            "parameters": {
                "type": "object",
                "properties": {
                    "venue_id": {
                        "type": "string",
                        "description": "The unique ID of the venue"
                    },
                    "datetime": {
                        "type": "string",
                        "description": "Date and time in ISO format"
                    },
                    "party_size": {
                        "type": "integer",
                        "description": "Number of people"
                    },
                    "contact_name": {
                        "type": "string",
                        "description": "Customer's full name"
                    },
                    "contact_phone": {
                        "type": "string",
                        "description": "Customer's phone number"
                    },
                    "contact_email": {
                        "type": "string",
                        "description": "Customer's email address"
                    },
                    "notes": {
                        "type": "string",
                        "description": "Special requests or notes"
                    }
                },
                "required": ["venue_id", "datetime", "party_size", "contact_name", "contact_phone", "contact_email"]
            }
        }
    }
]
