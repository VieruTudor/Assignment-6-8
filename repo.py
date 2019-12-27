from exceptions import RepoError


class Repo(object):
    def __init__(self):
        self.__objects = []
        self.__deletedObjects = []

    # Adds a unique entity passed by the service to the list
    # By unique, we mean that the entity has a unique ID that cannot be duplicate in the list

    def addUniqueObject(self, entity):
        if entity in self.__objects:
            raise RepoError("Entity already in list")
        self.__objects.append(entity)

    # Adds an entity passed by the service to the list
    # NOTE : Object doesn't have an ID and can be duplicated in the list, e.g : grades
    def addObject(self, entity):
        self.__objects.append(entity)

    # Updates an existing entity based on a given ID with a new one passed from the service
    def updateObject(self, entityID, newEntity):
        for entity in self.__objects:
            if entity.getID() == entityID:
                entity.setName(newEntity.getName())

    # Removes an entity from the list based on a given ID
    def removeObject(self, entityID):
        found = False
        for entity in self.__objects:
            if entity.getID() == entityID:
                found = True
        if not found:
            raise RepoError("Entity not in list")
        self.__objects[:] = [entity for entity in self.__objects if entity.getID() != entityID]

    # Removes grades associated to a student ID
    def removeGradeByStudentID(self, entityID):
        found = False
        for entity in self.__objects:
            if entity.getStudentID() == entityID:
                found = True
        if not found:
            raise RepoError("Entity not in list")
        self.__deletedObjects = [entity for entity in self.__objects if entity.getStudentID() == entityID]
        self.__objects = [entity for entity in self.__objects if entity.getStudentID() != entityID]
        # deletedObjects = self.objects - self.objects[:]
    # Removes grades associated to a discipline ID
    def removeGradeByDisciplineID(self, entityID):
        found = False
        for entity in self.__objects:
            if entity.getDisciplineID() == entityID:
                found = True
        if not found:
            raise RepoError("Entity not in list")
        self.__deletedObjects = [entity for entity in self.__objects if entity.getDisciplineID() == entityID]
        self.__objects = [entity for entity in self.__objects if entity.getDisciplineID() != entityID]

    # Searches an entity based on its ID
    def searchEntityByID(self, entityID):
        for entity in self.__objects:
            if entity.getID() == entityID:
                return entity
        raise RepoError("Entity not in list")

    # Searches an entity based on a partial or full name
    def searchEntityByName(self, entityName):
        foundEntities = [entity for entity in self.__objects if entityName.lower() in entity.getName().lower()]
        if len(foundEntities) == 0:
            raise RepoError("No matches found")
        return foundEntities

    # Returns a list containing all the objects in the repo
    def getAllObjects(self):
        return self.__objects[:]

    def getDeletedObjects(self):
        return self.__deletedObjects[:]

    # Wipes the entire list in the current repo
    def clearList(self):
        self.__objects.clear()
