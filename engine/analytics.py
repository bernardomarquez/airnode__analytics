
# CLASIFICACIÓN DE ESTADOS DE AERONAVES

def classify_aircraft_states(aircraft_states):
    """Clasifica las aeronaves según su estado operacional."""

    classification = {
        "airborne": [],
        "ground_stationary": [],
        "ground_moving": [],
        "unknown": []
    }

    for aircraft in aircraft_states:
        on_ground = aircraft["on_ground"]
        velocity = aircraft["velocity"]

        if on_ground is None:
            status = "unknown"
        elif not bool(on_ground):
            status = "airborne"
        elif velocity is not None and velocity > 1.5:
            status = "ground_moving"
        else:
            status = "ground_stationary"

        classification[status].append(aircraft)

    return classification


# INDICADORES DE TRÁFICO AÉREO

def calculate_traffic_metrics(history):
    """Calcula indicadores básicos del histórico de OpenSky."""

    if not history:
        return None

    aircraft_counts = [
        snapshot["total_aircraft"]
        for snapshot in history
    ]

    latest_aircraft = aircraft_counts[-1]

    return {
        "total_snapshots": len(aircraft_counts),
        "average_aircraft": round(sum(aircraft_counts) / len(aircraft_counts), 2),
        "maximum_aircraft": max(aircraft_counts),
        "minimum_aircraft": min(aircraft_counts),
        "latest_aircraft": latest_aircraft,
        "aircraft_variation": (
            latest_aircraft - aircraft_counts[-2]
            if len(aircraft_counts) > 1 else None
        )
    }
