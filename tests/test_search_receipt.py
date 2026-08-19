from utils.customer_utils import search_receipts_by_customer_id


def test_customer_receipt_history():

    receipts = [
        {
            "receipt_number": "RCP000001",
            "customer_id": "CUS000001"
        },
        {
            "receipt_number": "RCP000002",
            "customer_id": None
        },
        {
            "receipt_number": "RCP000003",
            "customer_id": "CUS000002"
        },
        {
            "receipt_number": "RCP000004",
            "customer_id": None
        },
        {
            "receipt_number": "RCP000005",
            "customer_id": "CUS000001"
        }
    ]

    results = search_receipts_by_customer_id(
        receipts,
        "CUS000001"
    )

    assert len(results) == 2

    assert results[0]["receipt_number"] == "RCP000001"
    assert results[1]["receipt_number"] == "RCP000005"

    print("Customer receipt history test passed.")


test_customer_receipt_history()