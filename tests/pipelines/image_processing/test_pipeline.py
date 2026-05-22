from src.new_kedro_project.pipelines.image_processing.nodes import process_image


def test_process_image():
    result = process_image(
        "data/01_raw/marte.jpg",
        "data/03_primary/test_output.jpg",
        45,
        "FIND_EDGES",
        "TEST"
    )

    assert result == "data/03_primary/test_output.jpg"