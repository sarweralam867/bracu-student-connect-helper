from bracu_seat_finder.browser import get_browser, select_existing_tab, ensure_logged_in
from bracu_seat_finder.capture import capture_api_data
from bracu_seat_finder.config import load_settings
from bracu_seat_finder.dashboard import write_dashboard


def main():
    settings = load_settings()
    student_id = settings["student_id"]

    print("=" * 70)
    print("BRACU COURSE SEAT FINDER")
    print("=" * 70)

    driver = get_browser()
    select_existing_tab(driver)
    ensure_logged_in(driver)

    api_data = capture_api_data(driver, student_id)
    seat_data = api_data.get("seat")
    schedule_data = api_data.get("schedule")

    print()
    print("-" * 70)
    print("API STATUS")
    print("-" * 70)
    print("Seat status :", "OK" if seat_data is not None else "FAILED")
    print("Schedule    :", "OK" if schedule_data is not None else "FAILED")

    if seat_data is None:
        raise RuntimeError("Seat-status API could not be loaded.")

    if schedule_data is None:
        raise RuntimeError("Course/schedule API could not be loaded.")

    dashboard_path, stats = write_dashboard(
        student_id=student_id,
        seat_data=seat_data,
        schedule_data=schedule_data,
    )

    print()
    print(f"Course sections : {stats['total_sections']}")
    print(f"Available       : {stats['available_sections']}")
    print(f"Full            : {stats['full_sections']}")
    print(f"Overbooked      : {stats['overbooked_sections']}")

    driver.get(dashboard_path.as_uri())

    print()
    print("=" * 70)
    print("DASHBOARD READY")
    print("=" * 70)
    print("Keep this Chrome window open to reuse the same BRACU login.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped.")
    except Exception as exc:
        print(f"\nERROR: {exc}")
        input("\nPress Enter to exit...")
