# Experiment B1: Real-Time Undo/Redo System for Text Editor
# Group B: Stacks, Queues, and Linked List

class TextEditor:
    def __init__(self):
        self.doc = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, new_text):
        """Applies a new change and clears the redo history."""
        self.undo_stack.append(self.doc)
        self.doc = new_text
        self.redo_stack.clear()
        print(f"Change made -> '{self.doc}'")

    def undo(self):
        """Reverts the most recent change and stores it for redo."""
        if self.undo_stack:
            self.redo_stack.append(self.doc)
            self.doc = self.undo_stack.pop()
            print("Undo performed.")
        else:
            print("Nothing to undo.")

    def redo(self):
        """Reapplies the most recently undone change."""
        if self.redo_stack:
            self.undo_stack.append(self.doc)
            self.doc = self.redo_stack.pop()
            print("Redo performed.")
        else:
            print("Nothing to redo.")

    def display(self):
        """Displays the current document state."""
        print(f"Current Document State: '{self.doc}'")


if __name__ == "__main__":
    print("--- Text Editor Undo/Redo System ---")
    editor = TextEditor()
    editor.make_change("Hello")
    editor.make_change("Hello World")
    editor.display()

    editor.undo()
    editor.display()

    editor.redo()
    editor.display()
