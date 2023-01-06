import os
import tempfile
import subprocess
import time


def blast_sequence(
    sequence,
    blast_db=None,
    subject_sequences=None,
    subject=None,
    word_size=4,
    perc_identity=80,
    num_alignments=1000,
    ungapped=False,
    num_threads=3,
    culling_limit=None,
    e_value=None,
    task=None,
    dust="no",
):
    pass
