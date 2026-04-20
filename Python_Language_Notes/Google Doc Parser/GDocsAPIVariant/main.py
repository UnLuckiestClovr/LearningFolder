import re
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SERVICE_ACCOUNT_CREDENTIALS_FILE = './gdocreadwriter_creds.json'

def get_gdoc_id(url: str) -> str:
    match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
    if not match:
        raise ValueError("Invalid Google Doc URL")
    return match.group(1)

def get_paragraph_text(paragraph) -> str:
    text = []
    for element in paragraph.get('elements', []):
        if 'textRun' in element:
            text.append(element['textRun']['content'])
    return ''.join(text).strip()

def get_table_array(table) -> list:
    table_array = []
    for row in table.get('tableRows', []):
        row_cells = []
        for cell in row.get('tableCells', []):
            cell_text = []
            for content in cell.get('content', []):
                if 'paragraph' in content:
                    cell_text.append(get_paragraph_text(content['paragraph']))
            row_cells.append(''.join(cell_text).strip())
        table_array.append(row_cells)
    table_array.pop(0)  # Remove header row
    return table_array
        

def fetch_gdoc_table_content(gdoc_url: str) -> list:
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_CREDENTIALS_FILE, scopes=SCOPES)
    service = build('docs', 'v1', credentials=credentials)
    gdoc_id = get_gdoc_id(gdoc_url)

    gdoc = service.documents().get(documentId=gdoc_id).execute()

    for element in gdoc.get('body', {}).get('content', []):
        if 'table' in element:
            return get_table_array(element['table'])    

def build_scode_grid(points):
    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, _, y in points)

    print(f"Max X: {max_x}, Max Y: {max_y}")

    # Create grid filled with spaces
    grid = [
        [" " for _ in range(int(max_x) + 1)]
        for _ in range(int(max_y) + 1)
    ]

    print("Initial grid:", grid)

    # Place characters
    for x, char, y in points:
        print(f"Placing '{char}' at ({x}, {y})")
        grid[int(y)][int(x)] = char

    print("Final grid:", grid)

    return "\n".join("".join(row).rstrip() for row in reversed(grid))

def assemble_scode(gdoc_url: str) -> str:
    table_content = fetch_gdoc_table_content(gdoc_url)

    return build_scode_grid(table_content)

if __name__ == "__main__":
    gdoc_url = input("Enter the Google Doc URL: ")
    scode = assemble_scode(gdoc_url)
    print(scode)