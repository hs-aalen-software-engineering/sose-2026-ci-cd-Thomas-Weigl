"""Application entry point for the Road Profile Viewer."""

from road_profile_viewer.visualization import create_dash_app


def main() -> None:
    """
    Main function to run the Dash application.
    """
    app = create_dash_app()
    print("Starting Road Profile Viewer...")
    print("Open your browser and navigate to: http://127.0.0.1:8050/")
    print("Press Ctrl+C to stop the server.")
    app.run(debug=True)  # pyright: ignore[reportUnknownMemberType]


if __name__ == "__main__":
    main()
