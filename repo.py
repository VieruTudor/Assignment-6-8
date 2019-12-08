from exceptions import RepoError


class Repo(object):
    def __init__(self):
        self.__objects = []

    def addUniqueObject(self, entity):
        if entity in self.__objects:
            raise RepoError("Entity already in list")
        self.__objects.append(entity)

    def addObject(self, entity):
        self.__objects.append(entity)

    def updateObject(self, entityID, newEntity):
        for entity in self.__objects:
            if entity.getID() == entityID:
                entity.setName(newEntity.getName())

    def removeObject(self, entityID):
        found = False
        for entity in self.__objects:
            if entity.getID() == entityID:
                found = True
        if not found:
            raise RepoError("Entity not in list")
        self.__objects[:] = [entity for entity in self.__objects if entity.getID() != entityID]

    def removeGradeByStudentID(self, entityID):
        found = False
        for entity in self.__objects:
            if entity.getStudentID() == entityID:
                found = True
        if not found:
            raise RepoError("Entity not in list")
        self.__objects[:] = [entity for entity in self.__objects if entity.getStudentID() != entityID]

    def removeGradeByDisciplineID(self, entityID):
        found = False
        for entity in self.__objects:
            if entity.getDisciplineID() == entityID:
                found = True
        if not found:
            raise RepoError("Entity not in list")
        self.__objects[:] = [entity for entity in self.__objects if entity.getDisciplineID() != entityID]

    def searchEntityByID(self, entityID):
        for entity in self.__objects:
            if entity.getID() == entityID:
                return entity
        raise RepoError("Entity not in list")

    def searchEntityByName(self, entityName):
        foundEntities = [entity for entity in self.__objects if entityName.lower() in entity.getName().lower()]
        if len(foundEntities) == 0:
            raise RepoError("No matches found")
        return foundEntities

    def getAllObjects(self):
        return self.__objects[:]

    def clearList(self):
        self.__objects.clear()
