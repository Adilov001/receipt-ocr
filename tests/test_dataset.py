from receipt.dataset import is_text_source


def test_text_source_photo_and_its_synthetic_variants_are_skipped():
    gt = {"_text_source": "r17_a.jpg"}
    assert is_text_source("r17_a.jpg", gt)
    assert is_text_source("r17_a_x1.jpg", gt)
    assert is_text_source("r17_a_x2.jpg", gt)


def test_other_photos_of_the_receipt_are_scored():
    gt = {"_text_source": "r17_a.jpg"}
    assert not is_text_source("r17_c.jpg", gt)
    assert not is_text_source("r17_q.jpg", gt)
    assert not is_text_source("r17_c_x1.jpg", gt)


def test_labels_without_a_source_are_scored_everywhere():
    assert not is_text_source("r01_a.jpg", {"seller_name": "ERA"})
    assert not is_text_source("r01_a.jpg", None)


def test_holdout2_is_kept_out_of_dev_and_test():
    from receipt.config import load_config
    from receipt.dataset import rows_for
    cfg = load_config()
    new = {r["receipt_id"] for r in rows_for(cfg, "holdout2")}
    assert {"h07", "h08", "h09"} <= new
    for split in ("dev", "test", "holdout"):
        assert not new & {r["receipt_id"] for r in rows_for(cfg, split)}
