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


def test_spent_holdout2_is_in_dev_and_the_holdout_stays_out():
    from receipt.config import load_config
    from receipt.dataset import rows_for
    cfg = load_config()
    dev = {r["receipt_id"] for r in rows_for(cfg, "dev")}
    test = {r["receipt_id"] for r in rows_for(cfg, "test")}
    assert {"h07", "h10", "h13"} <= dev and not {"h07", "h10", "h13"} & test
    old = {r["receipt_id"] for r in rows_for(cfg, "holdout")}
    assert old and not old & (dev | test)
