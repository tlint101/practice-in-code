import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    title: Marimo Widgets
    subtitle: "Where I interact with my data"
    date: "2026-10-02"
    categories: [Coding, Python]
    engine: marimo
    execute:
      echo: true
    pyproject: |
      requires-python = ">=3.10"
      dependencies = [marimo-chem-utils", "pandas"]
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Introduction

    In my last post, I talked about Marimo. This post, I would like to focus on the widgets geared towards my area of study, Cheminformatics. If you've been following Marimo and Pat Walters, you'd know that they are putting in a lot of effort in creating interactive widgets geared towards cheminfomratics. Pat Walters has even created a nice package for people to get started. It comes with some handy tools. These are great to make interactive charts when communicating to others in the lab.

    Here I would like to demo teh package, [marimo_chem_utils](https://github.com/PatWalters/marimo_chem_utils/tree/main). These have some nice built in tools that most users in the field would like - handling a dataframe, creating fingerprints, and reducing dimension and plotting it as a scatterplot. These are great as they are already ƒormatted for interactive usage in Marimo.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Code

    Getting hte project working is straightforward. For the dataset, I used a dummy set setup by Pat Walters. It contains molecules and their associated pIC50. I don't know what activity it is for, but that is not important for this demo.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from marimo_chem_utils import add_fingerprint_column, add_image_column, add_inchi_key_column, add_tsne_columns, interactive_chart

    return (
        add_fingerprint_column,
        add_image_column,
        add_inchi_key_column,
        add_tsne_columns,
        interactive_chart,
        mo,
        pd,
    )


@app.cell
def _(pd):
    # Load some data
    df = pd.read_csv("https://raw.githubusercontent.com/PatWalters/datafiles/refs/heads/main/carbonic.csv")
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It is easy to process the dataset. Here I added a column for the molecular fingerprint, rendred the molecule as an RDKit image and appdend it as a column, added an inchi key column, and columns for the TSNE. That is a lot of stuff in only a few short lines of code!
    """)
    return


@app.cell
def _(
    add_fingerprint_column,
    add_image_column,
    add_inchi_key_column,
    add_tsne_columns,
    df,
):
    # Add fingerprints, images, and InChI keys
    df_fp = add_fingerprint_column(df, fp_type="counts_fp")
    data = add_image_column(df_fp, smiles_column="SMILES")
    data = add_inchi_key_column(data, smiles_column="SMILES")

    # Generate t-SNE coordinates
    data = add_tsne_columns(data)
    data
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, the molecules can be rendered as an interactive scatterplot. This is done from the calculated TSNE values above. It is easy to do since these values were added to the DataFrame. Parameters were set to allow for the image of the molecule and its associated pIC50 value to "pop up" as the mouse hovers each scatter point.
    """)
    return


@app.cell
def _(data, interactive_chart, mo):
    chart = interactive_chart(data, x_col="TSNE_x", y_col="TSNE_y", color_col="pIC50", image_col="image").properties(width=500, height=500)
    mo.ui.altair_chart(chart)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusion

    That's pretty much it. A really neat tool. As Marimo gains more traction, I'm sure neat tools will continue to be created for cheminformatics. A great way to share computational work for others. That is growing more and more improtant in the age of AI.
    """)
    return


if __name__ == "__main__":
    app.run()
