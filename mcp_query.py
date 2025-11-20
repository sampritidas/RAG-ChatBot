import json
import requests

def query_server(server, query):
    """Send the query to the remote MCP-style API endpoint."""
    try:
        url = server["url"]
        full_url = url + "&q=" + query if "?" in url else url + "?q=" + query

        res = requests.get(full_url, timeout=5)
        res.raise_for_status()

        data = res.json()
        return json.dumps(data, indent=2)[:2000]

    except Exception:
        return None


def query_all_mcps(query):
    """Loop over mcp_servers.json and try each API."""
    with open("mcp_servers.json") as f:
        servers = json.load(f)["servers"]

    for s in servers:
        print(f"Checking MCP server: {s['id']}")
        answer = query_server(s, query)
        if answer:
            return f"From MCP server {s['id']}:\n{answer}"

    return None
