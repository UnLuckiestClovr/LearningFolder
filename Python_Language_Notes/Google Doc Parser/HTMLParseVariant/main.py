import requests
from bs4 import BeautifulSoup

def fetch_gdoc_html(gdoc_url: str) -> str:
    response = requests.get(gdoc_url)
    response.raise_for_status()
    return response.text

def extract_table(html_content: str) -> list:
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    table_array = []

    if not table:
        return table_array

    rows = table.find_all('tr')
    for row in rows[1:]:  # Skip header row
        cells = row.find_all(['td', 'th'])
        row_cells = [cell.get_text(strip=True) for cell in cells]
        row_cells[0] = int(row_cells[0])
        row_cells[2] = int(row_cells[2]) 
        table_array.append(row_cells)

    return table_array

def build_scode_grid(points):
    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, _, y in points)

    # Create grid filled with spaces
    grid = [
        [" " for _ in range(max_x + 1)]
        for _ in range(max_y + 1)
    ]

    # Place characters
    for x, char, y in points:
        grid[y][x] = char

    return "\n".join("".join(row).rstrip() for row in reversed(grid))

def assemble_scode(gdoc_url: str) -> str:
    html_content = fetch_gdoc_html(gdoc_url)
    table_content = extract_table(html_content)

    return build_scode_grid(table_content)

if __name__ == "__main__":
    gdoc_url = input("Enter the Google Doc URL: ")

    scode = assemble_scode(gdoc_url)
    print(scode)