from src.core.processor import BoxAggregator

class MockResult:
    def __init__(self, data, type):
        self.data = data
        self.type = type

def test_add_multiple_unique_codes():
    """Test that multiple unique codes are correctly aggregated."""
    aggregator = BoxAggregator(box_id="box_1")
    results = [MockResult("code_1", "type_1"), MockResult("code_2", "type_2")]
    aggregator.add(results)
    payload = aggregator.payload()
    
    assert len(payload["barcodes"]) == 2
    assert payload["barcodes"] == [
        {"data": "code_1", "type": "type_1"},
        {"data": "code_2", "type": "type_2"}
    ]

def test_add_duplicate_codes():
    """Test that duplicate codes are deduplicated."""
    aggregator = BoxAggregator(box_id="box_2")
    results = [MockResult("code_1", "type_1"), MockResult("code_1", "type_1")]
    aggregator.add(results)
    payload = aggregator.payload()
    
    assert len(payload["barcodes"]) == 1
    assert payload["barcodes"][0] == {"data": "code_1", "type": "type_1"}

def test_mixed_unique_and_duplicates():
    """Test a mix of unique and duplicate codes."""
    aggregator = BoxAggregator(box_id="box_3")
    results = [
        MockResult("code_1", "type_1"),
        MockResult("code_2", "type_2"),
        MockResult("code_1", "type_1")  # Duplicate
    ]
    aggregator.add(results)
    payload = aggregator.payload()
    
    assert len(payload["barcodes"]) == 2
    barcodes = payload["barcodes"]
    data_values = [b["data"] for b in barcodes]
    assert "code_1" in data_values
    assert "code_2" in data_values
