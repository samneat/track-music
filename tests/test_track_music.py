from lib.track_music import *
import pytest

def test_add_one_song():
    ipod = Music()
    ipod.add("song_name")
    result = ipod.view()
    assert result == ['song_name']

def test_adding_two_songs_returns_list_with_songs():
    ipod = Music()
    ipod.add("song1")
    ipod.add("song2")
    result = ipod.view()
    assert result == ["song1", "song2"]

def test_view_empty_playlist():
    ipod = Music()
    result = ipod.view()
    assert result == "No songs added yet"

def test_trying_to_add_empty_string_raises_error():
    ipod = Music()
    with pytest.raises(Exception) as e:
        ipod.add("")
    error_message = str(e.value)
    assert error_message == "You must provide a song"

def test_already_added_song_returns_error():
    ipod = Music()
    ipod.add("song1")
    result = ipod.add("song1")
    assert result == "You have already added this sing"

