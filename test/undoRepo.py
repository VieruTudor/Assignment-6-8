class Operation(object):
    def __init__(self, undoFunction, redoFunction):
        self._undo = undoFunction
        self._redo = redoFunction

    def undo(self):
        self._undo()

    def redo(self):
        self._redo()
    

class Undo(object):
    def __init__(self):
        self._history = []
        self._historyIndex = 0
        self._isUndo = False

    def recordOperation(self, operation):
        if self._isUndo:
            return
        if self._historyIndex == len(self._history):
            self._history.append(operation)
        else:
            self._history[self._historyIndex] = operation
            index = self._historyIndex + 1
            while index < len(self._history):
                self._history.pop(index)
        self._historyIndex += 1

    def undoFunction(self):
        if self._historyIndex < 0:
            raise IndexError("Cannot undo more")
        self._isUndo = True
        self._historyIndex -= 1
        self._history[self._historyIndex].undo()
        self._isUndo = False

    def redoFunction(self):
        if self._historyIndex == len(self._history):
            raise IndexError("No more redos")
        self._isUndo = True
        self._history[self._historyIndex].redo()
