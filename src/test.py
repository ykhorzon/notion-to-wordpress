from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2="")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/Promise-Javascript-Promise-5563aae6627840cf8d529c6124dd2bee")

print("title", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
