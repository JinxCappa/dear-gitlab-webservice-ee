"""
Constants for the GitLab WebService EE application.
"""

# GitLab versions that should be blocked from processing
BLOCKED_VERSIONS = {
    "16.5.5",
    "16.6.3", 
    "16.7.1",
    "17.1.5",
    "17.2.3",
    "17.2.6",
    "17.7.5",
    "17.8.3",
    "17.9.4",
    "17.10.2",
    "18.2.3"
}

# Minimum major version to process
MIN_MAJOR_VERSION = 12