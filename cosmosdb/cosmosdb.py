# read and write cosmosdb
from dotenv import load_dotenv
import os
from azure.cosmos import CosmosClient

load_dotenv()


def get_cosmos_client():
    endpoint = os.environ.get("COSMOS_ENDPOINT")
    key = os.environ.get("COSMOS_KEY")
    client = CosmosClient(endpoint, key)
    container_name = os.environ.get("COSMOS_RESULT_SESSION_CONTAINER")

    db = client.get_database_client(os.environ.get("COSMOS_DB"))
    container = db.get_container_client(container_name)

    return container


COSMOSDB = get_cosmos_client()
IMPORTANT_KEYS = [
    "solved_1",
    "solved_2",
    "solved_3_lauri",
    "solved_3_lisi",
    "solved_3_lui",
    "solved_3_julli",
    "solved_3",
    "locked_1",
    "locked_2",
    "locked_3",
    "solved_4",
    "locked_4",
]


def get_all_games():
    query = "SELECT distinct c.id FROM c"
    games = COSMOSDB.query_items(query=query, enable_cross_partition_query=True)
    games = [game["id"] for game in games]
    return games


def retrieve_session_state(game_id: str):
    query = f'SELECT * FROM c WHERE c.id="{game_id}"'
    items = list(COSMOSDB.query_items(query=query, enable_cross_partition_query=True))
    return_state = {}
    for key, value in items[0].items():
        if key in IMPORTANT_KEYS:
            return_state[key] = value
    return return_state


def save_session_state(game_id: str, session_state: dict):
    item = {"id": game_id}
    for key in IMPORTANT_KEYS:
        if key in session_state:
            item[key] = session_state[key]
    item["sessionId"] = game_id
    COSMOSDB.upsert_item(item)


def delete_game(game_id: str):
    COSMOSDB.delete_item(item=game_id, partition_key=game_id)
