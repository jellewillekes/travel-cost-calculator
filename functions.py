def bereken_weekkosten(
    dagen_amsterdam: int,
    dagen_rotterdam: int,
    dagen_thuis: int,
    prijs_naar_amsterdam: float,
    prijs_naar_rotterdam: float
) -> float:
    """
    Calculate the travel costs for 1 workweek:
      - dagen_amsterdam: number of days in Amsterdam per week
      - dagen_rotterdam: number of days in Rotterdam per week
      - dagen_thuis: number of days working from home per week
      - prijs_naar_amsterdam: one-way price from home to Amsterdam
      - prijs_naar_rotterdam: one-way price from home to Rotterdam

    Assumptions:
      - 2 rides per workday (heen + terug)
      - Working from home costs 0 euro for travel
    """
    kosten_ams = dagen_amsterdam * 2 * prijs_naar_amsterdam
    kosten_rdam = dagen_rotterdam * 2 * prijs_naar_rotterdam
    # Thuiswerken = 0 euro for travel
    kosten_thuis = 0

    return kosten_ams + kosten_rdam + kosten_thuis


def bereken_maandkosten(
    dagen_amsterdam: int,
    dagen_rotterdam: int,
    dagen_thuis: int,
    prijs_naar_amsterdam: float,
    prijs_naar_rotterdam: float,
    weken_per_maand: int = 4
) -> float:
    """
    Monthly travel costs (= 4 weeks).
    """
    return bereken_weekkosten(
        dagen_amsterdam,
        dagen_rotterdam,
        dagen_thuis,
        prijs_naar_amsterdam,
        prijs_naar_rotterdam
    ) * weken_per_maand


def test_scenarios():
    """
    Example function to test a few static scenarios.
    Adjust the prices below if your home city is different.
    """
    # Example: living in Den Haag
    prijs_naar_amsterdam = 16.21
    prijs_naar_rotterdam = 6.00

    # Scenario 1: 3 days Amsterdam, 2 days home
    days_ams = 3
    days_home = 2
    days_rdam = 0
    cost1 = bereken_maandkosten(
        days_ams, days_rdam, days_home,
        prijs_naar_amsterdam, prijs_naar_rotterdam
    )
    print(f"Scenario 1 (3 AMS, 2 home) => € {cost1:.2f} per month")

    # Scenario 2: 3 days Amsterdam, 2 days Rotterdam
    days_ams = 3
    days_rdam = 2
    days_home = 0
    cost2 = bereken_maandkosten(
        days_ams, days_rdam, days_home,
        prijs_naar_amsterdam, prijs_naar_rotterdam
    )
    print(f"Scenario 2 (3 AMS, 2 RDM) => € {cost2:.2f} per month")

    # Scenario 3: 5 days Amsterdam
    days_ams = 5
    days_rdam = 0
    days_home = 0
    cost3 = bereken_maandkosten(
        days_ams, days_rdam, days_home,
        prijs_naar_amsterdam, prijs_naar_rotterdam
    )
    print(f"Scenario 3 (5 AMS) => € {cost3:.2f} per month")


if __name__ == "__main__":
    test_scenarios()
