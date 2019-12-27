class Operation(object):
    def __init__(self, undoFunction, redoFunction):
        self._undo = undoFunction
        self._redo = redoFunction

    def undo(self):
        self._undo()

    def redo(self):
        self._redo()


class FunctionCall(object):
    def __init__(self, functionName, *functionParameters):
        self._function = functionName
        self._parameters = functionParameters

    def __call__(self):
        self.call()

    def call(self):
        self._function(*self._parameters)

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
        self._historyIndex += 1
        self._isUndo = False


class MultipleOperation(object):
    def __init__(self, *operations):
        self._operationList = operations

    def undo(self):
        for operation in self._operationList:
            operation.undo()

    def redo(self):
        for operation in self._operationList:
            operation.redo()