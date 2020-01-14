from ..models import State, Chamber, simple_numbered_districts

DE = State(
    name="Delaware",
    abbr="DE",
    capital="Dover",
    capital_tz="America/New_York",
    fips="10",
    unicameral=False,
    legislature_name="Delaware General Assembly",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        num_seats=41,
        title="Representative",
        districts=simple_numbered_districts(41),
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        num_seats=21,
        title="Senator",
        districts=simple_numbered_districts(21),
    ),
)