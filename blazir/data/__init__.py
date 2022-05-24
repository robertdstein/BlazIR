import os
import pandas as pd

data_dir = os.path.dirname(__file__)

bzb_path = os.path.join(data_dir, "bzcat5.dat")

bzb_cat = pd.read_fwf(
    bzb_path, sep="\t", header=None, names=[
        "Seq", "prefix", "Name", "RAh", "RAm", "RAs",
        "DEd", "DEm", "DEs", "GLON", "GLAT",
        "z", "Rmag", "Class",
        "FR", "F143", "FX", "FF", "aro"
    ],
    index_col="Seq"
)

mag_cut = 16.

bright_bzb_cat = bzb_cat[bzb_cat["Rmag"] < 16.]
