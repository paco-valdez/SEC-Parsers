import typer
from sec_parsers import Filing, download_sec_filing, set_headers


app = typer.Typer()


def print_first_n_lines(text, n):
    lines = text.split("\n")
    for line in lines[:n]:
        print(line)


@app.command()
def cli(url: str):
    if not url:
        typer.echo("Please provide a URL")
        raise typer.Abort()
    if not url.startswith("http"):
        url = "https://www.sec.gov/Archives/" + url
    set_headers("John Test", "johntest@example.com")
    html = download_sec_filing(url)
    if not html:
        typer.echo("Failed to download filing")
        raise typer.Abort()
    filing = Filing(html, filing_type="DEF-14A")
    filing.parse()
    title = "Compensation Discussion and Analysis"
    item1a = filing.find_all_sections_from_text(title)
    if not item1a:
        print(filing.get_title_tree())
        filing.save_xml("test.xml")
        typer.echo(f"Failed to find Item {title}")
        raise typer.Abort()
    item1a_text = filing.get_text_from_section(item1a, include_title=True)
    print_first_n_lines(item1a_text, 10)


if __name__ == "__main__":
    app()
