"""
A simple PyperCard app to get a user's name, and then display a friendly
"Hello world!" type message.
"""
# We need to use the a pypercard App.
from pypercard import App


# Create the app as the object called hello_app.
hello_app = App()


# In the "get_name" card, when you "click" on the "submit" button...
@hello_app.transition("get_name", "click", "submit")
def hello(app, card):
    """
    Store the value in the card's input box, with the id "name", into the app's
    datastore, under the key "name".

    Then transition to the "say_hello" card.
    """
    app.datastore["name"] = card.get_by_id("name").value
    return "say_hello"


# In the "say_hello" card, when you "click" on the "again" button...
@hello_app.transition("say_hello", "click", "again")
def again(app, card):
    """
    Don't do anything except transition to the "get_name" card.
    """
    return "get_name"


# Start the hello_app
hello_app.start()
