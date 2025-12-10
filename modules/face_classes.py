import face_recognition

class Person:
    def __init__(self, name, encoding):
        self.name = name
        self.encoding = encoding

class FaceRecognizer:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def recognize(self, unknown_encoding, tolerance=0.6):
        if not self.people:
            return "No registered faces"

        encodings = [p.encoding for p in self.people]
        names = [p.name for p in self.people]

        matches = face_recognition.compare_faces(encodings, unknown_encoding, tolerance=tolerance)
        if True in matches:
            return names[matches.index(True)]
        return "Unknown"
