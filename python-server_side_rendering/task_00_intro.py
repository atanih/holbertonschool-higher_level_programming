#!/usr/bin/python3
"""Module that generates personalized invitation files from a template."""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template containing placeholders
            {name}, {event_title}, {event_date}, {event_location}.
        attendees (list): A list of dictionaries, each holding the data
            for a single attendee.

    For each attendee, an output file named `output_X.txt` (where X is
    the attendee's position starting from 1) is created with the
    placeholders in the template replaced by the corresponding values.
    Any missing value is replaced with "N/A".
    """
    # Validate input types
    if not isinstance(template, str):
        logger.error("Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        logger.error("Attendees must be a list of dictionaries.")
        return

    # Handle empty template
    if not template:
        logger.error("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            output_content = output_content.replace(
                "{" + placeholder + "}", str(value)
            )

        output_filename = "output_{}.txt".format(index)
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(output_content)
        except IOError as e:
            logger.error("Error writing to file %s: %s", output_filename, e)
