# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add(self, music):
        # Parameters:
        #   music: string representing a track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the music into playlist 
        pass # No code here yet

    def view(self):
        # Returns:
        #   A list containing tracks you have listened to
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a song
will add song to playlist
"""
playlist = Music()
playlist.add("song_name")
playlist.view() => ["song_name"]

"""
Tring to view empty playlist
#view raises an exception
"""
playlist = Music()
playlist.view() # raises an error with the message "No songs added yet."

"""
Trying to add two songs
both songs added to playlist
"""
playlist = Music()
playlist.add("song1")
playlist.add("song2")
plasylist.view() => ["song1", "song2"]

"""
when given a none string
#raise error
"""
playlist = Music()
playlist.add(song) => error message: you cant add a none string

"""
when giving already added song
returns song already added
"""
playlist = Music()
playlist.add('song1')
playlist.add('song1') => song already added


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
