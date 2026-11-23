import pytest
import media.audio_time_stretch as mod

CASES = [
    ("phase_continuity", (1)),
    ("window_by_rate", (1)),
    ("loudness_norm", (1)),
    ("boundary_crossfade", (1)),
    ("loop_align", (1)),
    ("resample_determinism", (1)),
    ("transient_guard", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("reverse_mode", (1)),
    ("metrics", (1)),
    ("overlap_add", (1)),
    ("pitch_shift", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
