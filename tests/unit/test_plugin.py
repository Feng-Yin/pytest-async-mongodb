import pytest
from pytest_async_mongodb import plugin


@pytest.mark.asyncio
async def test_load(async_mongodb):
    collection_names = await async_mongodb.collection_names()
    assert 'players' in collection_names
    assert 'championships' in collection_names
    assert len(plugin._cache.keys()) == 2
    # check_players(async_mongodb.players)
    # check_championships(async_mongodb.championships)


def check_players(players):
    assert players.count() == 2
    check_keys_in_docs(players, ['name', 'surname', "position"])
    manuel = players.find_one({'name': 'Manuel'})
    assert manuel['surname'] == 'Neuer'
    assert manuel['position'] == 'keeper'


def check_championships(championships):
    assert championships.count() == 3
    check_keys_in_docs(championships, ['year', 'host', 'winner'])


def check_keys_in_docs(collection, keys):
    for doc in collection.find():
        for key in keys:
            assert key in doc


# def test_insert(mongodb):
#     mongodb.players.insert({
#         'name': 'Bastian',
#         'surname': 'Schweinsteiger',
#         'position': 'midfield'
#     })
#     assert mongodb.players.count() == 3
#     assert mongodb.players.find_one({'name': 'Bastian'})
