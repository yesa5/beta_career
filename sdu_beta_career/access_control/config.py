from enum import IntFlag, Enum, auto


class Access(IntFlag):
    NONE = 0
    READ = 1
    WRITE = 2


class Policy(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    # APPLICATION
    JOB_APPLICATION = auto()

    # REPORTS
    REPORT = auto()
    REPORT_OWN = auto()

    # APPROVING
    APPROVE_REPORT = auto()

    # GRADING
    GRADING = auto()

    # PROFILE
    PROFILE_OWN = auto()


# Note for any changes call migrations.0002_*.create_default_access_controls function
# which will update access controls.
ACCESS_CONTROLS = {
    "student": {
        Policy.REPORT_OWN.name: Access.READ | Access.WRITE,
        Policy.PROFILE_OWN.name: Access.READ | Access.WRITE
    },
}

DEFAULT_ACCESS_CONTROL = "student"
