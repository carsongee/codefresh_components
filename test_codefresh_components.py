import codefresh_components as cf


def test_create_pipeline_structure():
    struct = cf.create_pipeline_structure(
        ["tf/pipe1", "tf/pipe2"], "origin/main", "beefbeefbeef"
    )
    assert len(struct) == 2
    assert {"pipeline_id", "trigger_id", "branch", "sha"} == set(struct[0].keys())
